#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import sys

from dotenv import load_dotenv
load_dotenv()

# inputs
ACCESS_TOKEN = os.environ['INPUT_ACCESS_TOKEN']
MESSAGE = os.environ['INPUT_MESSAGE']
PAGE_ID = os.environ['INPUT_PAGE_ID']
URL = os.getenv('INPUT_URL', None)
FAIL_ON_ERROR = os.getenv('INPUT_FAIL_ON_ERROR', 'true')

FACEBOOK_API_END = 'https://graph.facebook.com/{0}/feed'.format(PAGE_ID)

if URL:
    FACEBOOK_API_DATA = {'message': MESSAGE,
                         'link': URL,
                         'access_token': ACCESS_TOKEN}
else:
    FACEBOOK_API_DATA = {'message': MESSAGE,
                         'access_token': ACCESS_TOKEN}

r = requests.post(url=FACEBOOK_API_END, json=FACEBOOK_API_DATA)

result = r.json()

if 'error' not in result:
    print('Post successful')
else:
    print('Post error')
    if FAIL_ON_ERROR.lower() == 'true':
        print('Failing the workflow')
        sys.exit(1)
