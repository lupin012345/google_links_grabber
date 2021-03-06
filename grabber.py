#!/usr/bin/python3

import requests
from sys import argv

url = "http://searx.me"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
headers = {
    'User-Agent': user_agent
}
additional_params="categories=general"

def usage():
    print('usage : %s "query"' %argv[0])
    return 1

def get_links_from_text(text):
    links = []
    splits = text.replace("https://", "http://").split("http://")
    for split in splits:
        if not "google" in split:
            find = split.find('"')
            if split.find('<') < find:
                find = split.find('<')
            if len(split[:find]) > 0:
                links.append(split[:find])
    return links

def get_links(query, page):
    get_request = url+"/search?q=%s&oq=%s&pageno=%s&%s" %(query.replace(" ", "+"), query.replace(" ", "+"), page, additional_params)
    print("Query : [%s]" %get_request)
    r = requests.get(get_request, headers=headers)
    if (r.status_code == 200):
        return get_links_from_text(r.text)
    print(r.text)
    return []

def main():
    if len(argv) != 2:
        return usage()
    else:
        print(get_links(argv[1], 0))
    return 0

if __name__ == "__main__":
    main()
