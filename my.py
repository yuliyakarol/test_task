#!/usr/bin/python
#
# Begin by importing modules

import sys
import getpass
import json
import requests
import logging

BASE_URL = "http://confluence....com/rest/api/content"
PAGEID = pageid
PAYLOAD = {'some': 'data'}

def main():
# create logger
    logging.basicConfig(filename='page_update.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logging.info('Started')
# ask username and password
    username = raw_input('login: ')
    passwd = getpass.getpass()
#build url
    url = "{base}/{pageid}".format(
        base = BASE_URL, pageid = str(PAGEID))

    logging.info('Updating page PAGEID')
#Now, let's try to put a webpage.  
    r = requests.put(
        url,
        data = json.dumps(PAYLOAD),
        auth = (username, passwd),
        headers = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json'
            }
    )
	print(response.json())
    logging.info('Finished')
    r.raise_for_status()


if __name__ == "__main__" : main()
