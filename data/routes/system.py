import os

from flask import Blueprint, render_template, send_from_directory

system = Blueprint('system', __name__)


@system.errorhandler(404)
def page_not_found(e):
    """
    Custom Error 404 page
    Shows a custom page instead of the server 404, also sends a notification to
    Slack so that we can monitor and rectify any legitimate 404s
    :return: Render template
    """
    print(e)
    return render_template('layouts/404.html'), 404


@system.errorhandler(500)
def server_error(e):
    """
    Custom Error 500 page
    Shows a custom page instead of the server 500, also sends a notification to
    Slack so that we can monitor and rectify any legitimate 500s
    :return: Render template
    """
    print(e)
    return render_template('layouts/500.html'), 500


@system.route('/favicon.ico')
def favicon():
    """
    Need to make sure Internet Explorer can find the favicon
    :return:
    """
    return send_from_directory(os.path.join(system.root_path, 'static'),
                               'favicon.ico')
