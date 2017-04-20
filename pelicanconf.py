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

AUTHOR = 'Kochurov Maxim'
SITENAME = 'In Search Of The Holy Posterior'
SITEURL = 'https://ferrine.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Twitter', 'https://twitter.com/ferrine96'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('GitHub', 'https://github.com/ferrine'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAULT_METADATA = {
    'status': 'draft',
}
