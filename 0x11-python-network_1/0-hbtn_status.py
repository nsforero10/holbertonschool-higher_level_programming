#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
if __name___ == '__main__':
    import urllib.request as request
    with request.urlopen('http://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
