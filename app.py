import coloredlogs
import data
from flask import Flask
from flask_compress import Compress
from flask_navigation import Navigation
from flask_sitemap import Sitemap
from config import CONST


coloredlogs.install(level='DEBUG')

app = Flask(__name__)
Compress(app)

nav = Navigation(app)

ext = Sitemap(app)
cms = data.cms.CMSRequest()
rss = data.models.RSSRequest()
# events = data.models.EventsList()

app.secret_key = CONST.SECRET
app.url_map.strict_slashes = False
app.config['SITEMAP_URL_SCHEME'] = 'https'
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
app.config['COMPRESS_MIMETYPES'] = ['text/html', 'text/css', 'text/xml',
                                    'application/json', 'image/svg+xml',
                                    'application/javascript']

data.controllers.cache.init_app(app, config={'CACHE_TYPE': 'simple'})

# Grab basic Global Variables
app.jinja_env.globals['NONCE'] = CONST.NONCE
app.jinja_env.globals['ACCOUNT'] = cms.read_account()
app.jinja_env.globals['VOTD'] = rss.main()
app.jinja_env.globals['DEVOTION'] = rss.parse_devotion('devotions.xml')
# app.jinja_env.globals['EVENTSLIST_SHORT'] = events.get_events(5)
app.jinja_env.cache = {}

# @app.before_first_request
# def get_basics():
#     pass


# Register the Blueprints for Routes
app.register_blueprint(data.controllers.processors)
app.register_blueprint(data.routes.primary.primary)
app.register_blueprint(data.routes.church.church, url_prefix="/church")
app.register_blueprint(data.routes.school.school, url_prefix="/school")


# @ext.register_generator
# def sitemap_article():
#     """
#     Register the news articles on the fly
#     Automatically generate the news article links into the sitemap so that it
#     is up to date.
#     :return:
#     """
#     article = CMSRequest.read_all_articles(100, 0)
#     for item in article['data']:
#         yield 'resources.news_article', {'article_slug': item['slug']}, \
#               item['updated'], 'monthly', '0.8'

@app.before_request
def create_context():

    cms_pages = cms.read_navigation()

    church_pages = [
        nav.Item('Home', 'church.home'),
        nav.Item('Events', 'church.events'),
        nav.Item('News', 'church.church_news')
    ]
    school_pages = [
        nav.Item('Home', 'school.home'),
        nav.Item('Events', 'school.events'),
        nav.Item('Staff', 'school.school_staff_all'),
        nav.Item('News', 'school.school_news')
    ]

    for page in cms_pages['church_pages']:
        church_pages.append(nav.Item(page['meta_title'], 'church.church_cms_page',
                                     {'slug': page['slug']}))

    for page in cms_pages['school_pages']:
        school_pages.append(nav.Item(page['meta_title'], 'school.school_cms_page',
                                     {'slug': page['slug']}))

    nav.Bar('top', [
        nav.Item('Home', 'primary.home'),
        nav.Item('Church', 'church.home',
                 items=church_pages),
        nav.Item('School', 'school.home',
                 items=school_pages),
        nav.Item('Devotion', 'primary.devotion'),
        nav.Item('Contact', 'primary.contact')
    ])


if __name__ == '__main__':
    app.run()
