#!/usr/bin/python3

import urllib3

web = urllib3.PoolManager()


def fetch_file(url):
    if url:
        url = "https://raw.githubusercontent.com/"+url
        filename = url.split("/")[-1]
        response = web.request('get', url)
        if response.status == 200:
            with open(filename, "wt") as outfile:
                text = response.data.decode()
                print(text)
                outfile.write(text)


fetch_file(
    "hugsy/stuff/master/pentestlib.py")
