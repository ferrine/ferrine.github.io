#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
import os

# Simple hack to do modular development with themes
sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__))
)
from themesconf.blue_penguin import *
DEFAULT_DATE_FORMAT = '%b %d, %Y'

AUTHOR = 'Kochurov Maxim'
SITENAME = 'In Search Of The Holy Posterior'
SITEURL = 'https://ferrine.github.io'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'
STATIC_PATHS = ['images', 'figures', 'favicon.ico']


TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_EXCLUDES = ['pages']

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ferrine96'),
          ('GitHub', 'https://github.com/ferrine'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAULT_METADATA = {
    'add_comments': True
}


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'googleplus_comments', 'render_math']

SUMMARY_USE_FIRST_PARAGRAPH = True

if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read()
