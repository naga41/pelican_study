#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shuhei Nagata'
SITENAME = 'Barca.fm'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = (('Podcast', './feeds/podcasts.atom.xml'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['audio',]

### Settings for podcast
# Podcast
PODCAST_FEED_PATH = 'feeds/podcasts.atom.xml'
PODCAST_FEED_AUTHOR = AUTHOR
PODCAST_FEED_COPYRIGHT = AUTHOR
PODCAST_FEED_LANGUAGE = 'ja'
PODCAST_FEED_CATEGORY = 'Sports & Recreation'
PODCAST_FEED_EXPLICIT = 'No'
PODCAST_FEED_SUMMARY = "Talking about FC Barcelona in Japanese"
PODCAST_FEED_IMAGE = "http://hogehoge/hoge.png"


# Plugin
PLUGIN_PATHS = ['plugins',]
PLUGINS = ['pelican-podcast-feed',]
