import json
from datetime import datetime
from dateutil import parser
from htmlmin.main import minify
from flask import Blueprint
from flask_caching import Cache

cache = Cache()

processors = Blueprint('processors', __name__)


@processors.before_app_request
def clear_trailing():
    from flask import redirect, request
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@processors.app_context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@processors.app_template_filter('strftime')
def _jinja2_filter_datetime(date):
    """
    Format time into different states
    :param date:
    :return: object of different datetime blocks
    """
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    month = native.strftime('%b')
    date = native.strftime('%d')
    dblock = native.strftime('%B %-d')
    yblock = native.strftime('%Y')
    timeblock = native.strftime('%-I:%M %p')
    hour = native.strftime('%H')
    minute = native.strftime('%M')
    return {'dateblock': dblock, 'yblock': yblock, 'month': month, 'date': date,
            'timeblock': timeblock, 'hour': hour, 'minute': minute}


@processors.app_template_filter('minify')
def _jinja2_filter_minify(content):
    """
    Strip the line breaks in content
    :param content:
    :return:
    """
    return minify(content)


@processors.app_template_filter('to_json')
def _jinja2_filter_json(string):
    return json.loads(string)


@processors.app_template_filter('to_month_name')
def _jinja2_filter_monthname(float_month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    return months[int(float_month) - 1]
