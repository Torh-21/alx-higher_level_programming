#!/usr/bin/python3
"""This python script takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    values = {'email': mail}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
