from flask import Blueprint, render_template
from data.cms import CMSRequest
from config_app import CONST
from data.models import EventsList

cms = CMSRequest()
church = Blueprint('church', __name__)


@church.route('/')
def home():
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """
    # Introduction to CtK
    # Upcoming church events
    # Service information
    # Latest Sermon (pending) with links to sermon list
    # Links to
    # Plan your visit
    # Daily devotions
    # Questions? Answers from God’s Word
    # Pastor and Staff information
    # calendar = EventsList(CONST.CALENDAR_CHURCH)
    calendar = EventsList(CONST.CALENDAR_CHURCH)

    _data = cms.read_home_page('church')
    _events = calendar.get_events(5)
    _context = 'church'
    _meta = {
        "title": _data['meta_title'],
        "description": _data['meta_description']
    }

    return render_template('layouts/page_home_church.html', **locals())


@church.route('/events')
def events():
    _context = 'church'
    calendar = EventsList(CONST.CALENDAR_CHURCH)

    _events_calendar = calendar.group_events()
    _events = calendar.get_events(1)
    _calendar_id = CONST.CALENDAR_CHURCH
    _meta = {
        "title": "Church Events",
        "description": ""
    }
    return render_template('layouts/events.html', **locals())


@church.route('/<string:slug>')
def church_cms_page(slug):
    """
    :return:
    """
    _data = cms.read_page_by_slug(section='church', slug=slug)[0]
    calendar = EventsList(CONST.CALENDAR_CHURCH)
    _events = calendar.get_events(1)
    _meta = {
        "title":_data['meta_title'],
        "description":_data['meta_description']
    }
    _context = 'church'

    return render_template('layouts/page_standard.html', **locals())


@church.route('/news')
def church_news():
    """
    :return:
    """
    _data = cms.read_news_index(section='church')
    calendar = EventsList(CONST.CALENDAR_CHURCH)
    _events = calendar.get_events(1)

    _meta = {
        "title": 'News Updates'
    }
    return render_template('layouts/page_church_news_index.html', **locals())


@church.route('/news/<string:slug>')
def church_news_article(slug):
    """
    :return:
    """
    _data = cms.read_article_by_slug(section='church', slug=slug)[0]
    _meta = {
        "title":_data['title']
    }

    return render_template('layouts/page_news_article.html', **locals())
