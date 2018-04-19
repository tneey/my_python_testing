
import requests
import re
cs_url = 'https://www.github.com/login'
cs_user = ''
cs_apsw = ''
my_headers = {
'User-Agent' : 'Mozilla/5 (Macintosh;Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML,like Gecko)Chrome/48.0.2564.116 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding' : 'gzip',
'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
s = requests.session()
r = s.get(cs_url,headers=my_headers)
print r

		

		