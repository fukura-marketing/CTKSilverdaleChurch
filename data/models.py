import re
import requests
import xml.etree.ElementTree as ET
import datetime
import dateutil
from collections import defaultdict
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
from pandas.io.json import json_normalize


class EventsList:
    def __init__(self, calendar_id):
        self.limit = 25
        self.calendar_id = calendar_id
        self.credentials = service_account.Credentials\
            .from_service_account_file('client_secrets.json')
        self.project = self.credentials.with_scopes(
            scopes=['https://www.googleapis.com/auth/calendar.readonly'])
        self.service = build('calendar', 'v3', credentials=self.project)

    def get_events(self, limit: int = 10):
        # 'Z' indicates UTC time
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = self.service.events()\
            .list(calendarId=self.calendar_id, timeMin=now,
                  maxResults=limit, singleEvents=True,
                  orderBy='startTime').execute()
        return events_result.get('items', [])

    def group_events(self):
        events = self.get_events(self.limit)
        for row in events:
            print(row)
            if 'date' in row['start']:
                start = dateutil.parser.parse(row['start']['date'])
                row['start']['year'] = start.year
                row['start']['month'] = start.month
                row['start']['day'] = start.day

            else:
                start = dateutil.parser.parse(row['start']['dateTime'])
                row['start']['year'] = start.year
                row['start']['month'] = start.month
                row['start']['day'] = start.day

            if 'date' in row['end']:
                end = dateutil.parser.parse(row['end']['date'])
                row['end']['year'] = end.year
                row['end']['month'] = end.month
                row['end']['day'] = end.day

            else:
                end = dateutil.parser.parse(row['end']['dateTime'])
                row['end']['year'] = end.year
                row['end']['month'] = end.month
                row['end']['day'] = end.day

        raw = json_normalize(events, errors='ignore')

        df = pd.DataFrame(raw, columns=['summary',
                                        'location',
                                        'start.dateTime',
                                        'start.year',
                                        'start.month',
                                        'htmlLink',
                                        'start.day',
                                        'end.year',
                                        'end.month',
                                        'end.day',
                                        'end.dateTime'])

        grp = df.groupby(['start.year', 'start.month', 'start.day']).apply(lambda x: x.to_json(orient='records'))
        levels = len(grp.index.levels)
        dicts = [{} for i in range(levels)]
        last_index = None

        for index, value in grp.iteritems():

            if not last_index:
                last_index = index

            for (ii, (i, j)) in enumerate(zip(index, last_index)):
                if not i == j:
                    ii = levels - ii - 1
                    dicts[:ii] = [{} for _ in dicts[:ii]]
                    break

            for i, key in enumerate(reversed(index)):
                dicts[i][key] = value
                value = dicts[i]

            last_index = index

        result = dicts[-1]

        return result


class RSSRequest:

    @staticmethod
    def load_rss():
        url = 'http://wels.net/dev-daily/feed/pt-dev-daily/?redirect=no'
        headers = {'User-Agent': 'Mozilla/5.0 '
                                 '(Macintosh; Intel Mac OS X 10_11_5) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/50.0.2661.102 Safari/537.36'}
        # creating HTTP response object from given url
        resp = requests.get(url, headers=headers)

        with open('devotions.xml', 'wb') as f:
            f.write(resp.content)

    @staticmethod
    def parse_votd(xmlfile):
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for node in root.findall("channel/item[1]/{http://purl.org/rss/1.0"
                                 "/modules/content/}encoded"):
            return re.search('<blockquote>(.+\s<.+)</blockquote>',
                             node.text).group(1)

    @staticmethod
    def parse_devotion(xmlfile):
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        title = root.findall("channel/item[1]/title")[0].text
        sub = title.find(' – ')

        for node in root.findall("channel/item[1]/{http://purl.org/rss/1.0"
                                 "/modules/content/}encoded"):
            return {'title': title[:sub],
                    'body': node.text}

    @staticmethod
    def main():
        RSSRequest.load_rss()
        return RSSRequest.parse_votd('devotions.xml')
