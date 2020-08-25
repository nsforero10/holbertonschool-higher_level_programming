#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/statu'''
import urllib.request as request
if __name__ == '__main__':
    with request.urlopen('http://intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
