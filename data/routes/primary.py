import json
from flask import Blueprint, render_template
from data.cms import CMSRequest
from data.controllers import cache
from data.models import EventsList
from config_app import CONST

primary = Blueprint('primary', __name__)
cms = CMSRequest()


@cache.cached(timeout=200)
@primary.route('/')
def home():
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """
    # acct = cms.read_account()
    news = cms.read_all_news()

    dat = cms.read_index()
    page_title = dat['page_title']
    _meta = {
        "title": dat['page_title'],
        "description": dat['page_subtitle']
    }
    return render_template('layouts/home.html', **locals())


@primary.route('/devotions')
def devotion():
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """

    # Upcoming church events
    # Service information
    # {{ Information for this page }}
    # Additional sidebar information
    # Latest Sermon (pending) with links to sermon list
    # Daily devotions
    # Questions? Answers from God’s Word
    # Pastor and Staff information
    _meta = {
        "title": "Who we serve",
        "description": ""
    }

    return render_template('layouts/page_devotion.html', **locals())


@primary.route('/contact')
def contact():
    """
    Homepage.  The main traffic control page.  This page includes the following
    dynamic modules:

    :return:
    """
    _data = {}
    _meta = {
        "title": "Who we serve",
        "description": "CI Security is your leading managed detection and "
                       "response cyber security consulting company providing "
                       "managed IT security services for Healthcare."
    }

    return render_template('layouts/contact.html', **locals())
