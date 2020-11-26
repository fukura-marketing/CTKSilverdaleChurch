import json

import requests
import datetime
from config_app import CONST

# In the future we will need this for teachers authenticating...but for now...
# @staticmethod
# def get_token():
#     return requests.post(CONST.CMS_AUTH, json={"email": CONST.CMS_USR,
#                                                "password": CONST.CMS_PSS})


class CMSRequest:

    def __init__(self):
        # self.token = CMSRequest.get_token()
        self.today = datetime.datetime.now()

    def get_request(self, endpoint, options):
        """
        We aren't making this static just yet...
        :param endpoint:
        :param options:
        :return:
        """
        print(CONST.CMS_API + endpoint + options)
        return requests.get(CONST.CMS_API + endpoint + options)

    def read_account(self):
        endpoint = 'items/account/1'
        options = '?fields=*.*'
        response = self.get_request(endpoint, options)

        return response.json()['data']

    def read_navigation(self):
        endpoint = 'items/home_navigation/1'
        options = '?fields=church_pages.meta_title,church_pages.slug,' \
                  'school_pages.meta_title,school_pages.slug'
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_index(self):
        endpoint = 'items/home_page/1'
        options = ''
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_home_page(self, node):
        endpoint = 'items/{}_home/1'.format(node)
        options = '?fields=*,featured_news.title,featured_news.slug,' \
                  'featured_news.primary_image.*'
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_page_by_slug(self, section, slug):
        endpoint = 'items/{}_pages'.format(section)
        options = '?fields=*.*&filter[slug][eq]={}'.format(slug)
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_news_from_section(self, section, limit: int = 3, offset: int = 0):
        endpoint = 'items/{}_news'.format(section)
        options = '?fields=title,slug,publish_date,primary_image.*' \
                  '&offset={}&limit={}'.format(str(offset), str(limit))
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_all_news(self, limit: int = 2, offset: int = 0):
        news = self.read_news_from_section('church', limit, offset)
        for item in news:
            item['section'] = 'Church'
        news2 = self.read_news_from_section('school', limit, offset)
        for item in news2:
            item['section'] = 'School'
        news.extend(news2)
        return sorted(news, key=lambda k: k.get('publish_date', 0),
                      reverse=True)

    def read_news_index(self, section):
        return {'featured_news':
                self.read_featured_articles(section)['featured_news'],
                'news': self.read_articles(section, limit=20)}

    def read_articles(self, section, limit: int = 3, offset: int = 0):
        endpoint = 'items/{}_news'.format(section)
        options = '?fields=*.*&offset={}&limit={}'\
            .format(str(offset), str(limit))
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_featured_articles(self, section):
        endpoint = 'items/{}_home/1'.format(section)
        options = '?fields=featured_news.*.*'
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_article_by_slug(self, section, slug):
        endpoint = 'items/{}_news'.format(section)
        options = '?filter[slug][eq]={}&fields=*.*'.format(slug)
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_people(self, section):
        endpoint = 'items/{}_staff'.format(section)
        options = '?fields=*.*.*'
        response = self.get_request(endpoint, options)
        return response.json()['data']

    def read_user_id(self, staff):
        endpoint = 'users'
        options = '?filter[first_name][like]={}' \
                  '&filter[last_name][like]={}'\
            .format(staff.split('-')[0], staff.split('-')[1])
        response = self.get_request(endpoint, options)
        return response.json()

    def read_staff_page(self, staff):
        user_id = self.read_user_id(staff)['data'][0]['id']
        endpoint = 'items/staff_page'
        options = '?fields=*.*.*&filter[staff_member][eq]={}'.format(user_id)
        response = self.get_request(endpoint, options)
        return response.json()

    def read_staff_updates(self, staff):
        user_id = self.read_user_id(staff)['data'][0]['id']
        endpoint = 'items/classroom_updates'
        options = '?fields=*.*.*&filter[created_by][eq]={}'.format(user_id)
        response = self.get_request(endpoint, options)
        return response.json()
