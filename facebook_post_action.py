#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from utils import s

# inputs
ACCESS_TOKEN = os.environ['INPUT_ACCESS_TOKEN']
MESSAGE = os.environ['INPUT_MESSAGE']
PAGE_ID = os.environ['INPUT_PAGE_ID']
URL = os.getenv('INPUT_URL', None)

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
