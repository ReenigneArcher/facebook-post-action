# standard imports
import os
import sys

# lib imports
from dotenv import load_dotenv
import requests

load_dotenv()

# inputs
ACCESS_TOKEN = os.environ['INPUT_ACCESS_TOKEN']
MESSAGE = os.environ['INPUT_MESSAGE']
PAGE_ID = os.environ['INPUT_PAGE_ID']
URL = os.getenv('INPUT_URL', None)
FAIL_ON_ERROR = os.getenv('INPUT_FAIL_ON_ERROR', 'true')

# constants
FACEBOOK_API_END = f'https://graph.facebook.com/{PAGE_ID}/feed'


def main():
    facebook_api_data = {
        'message': MESSAGE,
        'access_token': ACCESS_TOKEN,
    }
    if URL:
        facebook_api_data['link'] = URL

    r = requests.post(url=FACEBOOK_API_END, json=facebook_api_data)

    result = r.json()

    if 'error' not in result:
        print('Post successful')
    else:
        print('Post error:')
        print(result)
        if FAIL_ON_ERROR.lower() == 'true':
            print('Failing the workflow')
            sys.exit(1)


if __name__ == '__main__':
    main()  # pragma: no cover
