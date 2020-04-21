from flask import Blueprint, render_template

from config import CONST
from data.cms import CMSRequest
from data.models import EventsList

cms = CMSRequest()
school = Blueprint('school', __name__)
calendar = EventsList(CONST.CALENDAR_SCHOOL)


@school.route('/')
def home():
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """

    _data = cms.read_home_page('school')
    _staff = cms.read_people('school')
    _events = calendar.get_events(5)

    _meta = {
        "title": _data['meta_title'],
        "description": _data['meta_description']
    }

    return render_template('layouts/page_home_school.html', **locals())


@school.route('/events')
def events():
    _events_calendar = calendar.group_events()
    _context = 'school'
    _events = calendar.get_events(1)
    _calendar_id = CONST.CALENDAR_SCHOOL
    _meta = {
        "title": "School Events",
        "description": ""
    }
    return render_template('layouts/events.html', **locals())


@school.route('/<string:slug>')
def school_cms_page(slug):
    """
    :return:
    """

    _data = cms.read_page_by_slug(section='school', slug=slug)[0]
    _events = calendar.get_events(1)
    _context = 'school'
    _meta = {
        "title": _data['meta_title'],
        "description": _data['meta_description']
    }
    return render_template('layouts/page_standard.html', **locals())


@school.route('/staff')
def school_staff_all():
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """
    _data = cms.read_people('school')
    _events = calendar.get_events(1)

    _events = calendar.get_events(1)
    _meta = {
        "title": "School Staff",
        "description": ""
    }

    return render_template('layouts/page_staff_school.html', **locals())


@school.route('/staff/<string:staff>')
def school_staff(staff):
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """
    _data = cms.read_staff_page(staff)['data'][0]

    updates = cms.read_staff_updates(staff)['data']
    _meta = {
        "title": _data['page_title'],
        "description": ""
    }

    return render_template('layouts/person_page.html', **locals())


@school.route('/staff/<string:staff>/<string:update>')
def school_staff_update(staff, update):
    """
    A blog post from a staff member

    :return:
    """

    _meta = {
        "title": "Who we serve",
        "description": ""
    }

    return render_template('layouts/home.html', **locals())


@school.route('/news')
def school_news():
    """
    :return:
    """
    _data = cms.read_news_index(section='school')
    _events = calendar.get_events(1)

    _meta = {
        "title": 'NEWS'
    }
    return render_template('layouts/page_school_news_index.html', **locals())


@school.route('/news/<string:slug>')
def school_news_article(slug):
    """
    :return:
    """
    _data = cms.read_article_by_slug(section='school', slug=slug)[0]
    _meta = {
        "title": _data['title']
    }

    return render_template('layouts/page_news_article.html', **locals())

