#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carl Hattingh'
SITENAME = 'Tech stuff'
SITEURL = ''
SITESUBTITLE = 'A space to dump some info before I forget it'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

MENUITEMS = [
    ('Posts', ''),
    ('Tags', 'tags.html')
]
DISPLAY_PAGES_ON_MENU = True

# THEME = 'themes/notmyidea'
THEME = 'themes/03'
CSS_FILE = 'style.css'
DELETE_OUTPUT_DIRECTORY = True


#DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
