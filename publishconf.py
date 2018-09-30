#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__))
)
<<<<<<< HEAD
from pelicanconf import *   # noqa
=======
from pelicanconf import *
>>>>>>> 3d2d610ffa15e1bbbeaf4c0dfe12dc7ca32277a8

SITEURL = 'https://ferrine.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'ferrine'
GOOGLE_ANALYTICS = "UA-98661135-1"
