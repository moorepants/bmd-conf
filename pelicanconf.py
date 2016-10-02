#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BMD Committee'
SITENAME = u'Bicycle and Motorcycle Dynamics Conference'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
BOOTSTRAP_THEME = 'cerulean'
CC_LICENSE = "CC-BY"
PAGE_ORDER_BY = 'sortorder'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

PASTCONFS = (
    ('BMD 2010 (Delft)', 'https://web.archive.org/web/20100529174822/http://bicycle.tudelft.nl/bmd2010'),
    ('BMD 2013 (Narashino)', 'http://www.bmd2013.org/'),
    ('BMD 2016 (Milwaukee)', 'http://www.bmd2016mke.org/'),
)

LINKS = (
    (r'University of Padua<br>Motorcycle Dynamics<br>Research Group', 'http://www.dinamoto.it/'),
    ('Polytechnic University<br>of Milan MOVE', 'https://www.move.deib.polimi.it/'),
    ('TU Delft Bicycle Dynamics', 'http://bicycle.tudelft.nl'),
    ('Cornell Bicyce Mechanics', 'http://ruina.tam.cornell.edu/research/topics/bicycle_mechanics/overview.php'),
    ('UCD Bicycle Research', 'http://biosport.ucdavis.edu/research-projects/bicycle'),
    ('Good Bicycle Science Blog', 'https://goodbicyclescience.com/'),
    ('Bad Bicycle Science Blog', 'https://badbicyclescience.com/'),
)

# Social widget
SOCIAL = (
    ('STVDY Listserv', 'https://groups.google.com/forum/#!forum/stvdy'),
    ('G+ Community', 'https://plus.google.com/communities/111776350998223174138'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
