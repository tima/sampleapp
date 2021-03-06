# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Timothy Appnel <tappnel@redhat.com>'
SITENAME = u'Application Demo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

THEME = os.getcwd() + '/clean-blog'
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


GITHUB_URL = 'https://github.com/ansible'
TWITTER_URL = 'https://twitter.com/ansible'
FACEBOOK_URL = 'https://facebook.com/ansibleautomation'

# Blogroll
LINKS = (('Ansible', 'https://ansible.com/'),
         ('Red Hat', 'https://redhat.com/'))

# Social widget
SOCIAL = (('@ansible', 'https://twitter.com/ansible'),
          ('@redhatnews', 'https://twitter.com/RedHatNews'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
