#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from utils import s

inputs = [
    'ACCESS_TOKEN',
    'MESSAGE',
    'PAGE_ID',
    'URL'
]

# get the input values
for key in inputs:
    try:
        globals()[key] = os.environ['INPUT_%s' % key] or os.environ[key]
    except KeyError:
        print('%s input has not been set.' % key)
        x = None

FACEBOOK_API_END = 'https://graph.facebook.com/{0}/feed'.format(PAGE_ID)

if URL:
    FACEBOOK_API_DATA = {'message': MESSAGE,
                         'link': URL,
                         'access_token': ACCESS_TOKEN}
else:
    FACEBOOK_API_DATA = {'message': MESSAGE,
                         'access_token': ACCESS_TOKEN}

HTTP_REQUEST = Request(url=FACEBOOK_API_END,
                       data=s(urlencode(FACEBOOK_API_DATA)))

while True:

    RESULT = json.loads(urlopen(HTTP_REQUEST).read())

    if 'error' not in RESULT:
        print('Post successful!')
        break
