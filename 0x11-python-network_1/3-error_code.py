#!/usr/bin/python3
"""This python script sends a request to the url passed and display the body of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        code = e.code
        print("Error code: {:d}".format(code))
