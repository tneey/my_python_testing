
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
import json
homeurl = ''
loginurl = ''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Referer': homeurl,
    "Upgrade-Insecure-Requests": "1"
}
payload = {
    'jobseeker_email':raw_input('input:'),
    'jobseeker_password':raw_input('input:')
}
session = requests.Session()
response = session.post(url=loginurl,headers=headers, data=payload)
response.headers['Referer'] = loginurl
print("Server status", response.status_code)
res = session.get(url=loginurl)
res.content.decode('utf8').encode('gb18030')
print res.content.decode('utf8').encode('gb18030')
