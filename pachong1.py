#coding=utf-8

import urllib2
import urllib
import cookielib
import requests
url = 'http://www.ecrecruit.com/en/jobseeker/user_login.php?Action=Login'
user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5; windows NT)'
referer = 'http://www.ecrecruit.com/'
postdata = {'jobseeker_email':'',
            'jobseeker_password':''
            }
data = urllib.urlencode(postdata)
headers = {'User-Agent':user_agent,'Referer':referer}
req = urllib2.Request(url,data,headers)
req.add_header('User-Agent',user_agent)
req.add_header('Referer',referer)
req.add_data(data)
response = urllib2.urlopen(req)
html = response.read()
print html.decode('utf8').encode('gb18030')
cookie = cookielib.CookieJar()
opener = urllib2.bulid_opener(urlib2.HTTPCookieProcessor(cookie))



		