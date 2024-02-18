#
# This is the Laegna Math Spider meant to train an AI with Laegna Math Studies website.
#   It should be used by client and server.
#

import requests
import urllib.parse
import json

def json_to_pyobj(json_obj):
    return json.loads(json_obj)

class BaseLaegnaDownloader:
    def __init__(self, url):
        self.url = url
        self.type = None
        self.content = None

    # Inherited classes overload this to have proper child classes
    def newInstance(self, url):
        return BaseLaegnaDownloader(url)

    def travel(self, urlpart):
        parsed_url = urllib.parse.urlparse(self.url)
        path = parsed_url.path
        if not path.endswith('/'):
            path += '/'
        newurl = f"{parsed_url.scheme}://{parsed_url.netloc}{path}{urlpart}"
        return self.newInstance(newurl)

    def download(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.type = self._detect_type(response.headers['Content-Type'])
            self.content = response.text
        else:
            raise RuntimeError('Request failed with status code {}'.format(response.status_code))

    def _detect_type(self, content_type):
        if content_type == 'application/json':
            return 'Json'
        elif content_type in ['text/html', 'text/markdown']:
            return 'Html'
        else:
            return None

def add_piece_to_url(url, piece):
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path
    if not path.endswith('/'):
        path += '/'
    return f"{parsed_url.scheme}://{parsed_url.netloc}{path}{piece}"

url = "http://127.0.0.1:5000/test?a=7"
piece = "/additional"
new_url = add_piece_to_url(url, piece)
print(new_url)  # Outputs http://127.0.0.1:5000/test/additional?a=7
