#coding=utf-8
'''
import urllib2
import urllib
import cookielib
import requests
url = 'http://www.ecrecruit.com/en/jobseeker/user_login.php?Action=Login'
user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5; windows NT)'
referer = 'http://www.ecrecruit.com/'
postdata = {'jobseeker_email':'hui@hui.com',
            'jobseeker_password':'123123'
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
'''

'''
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
import json
homeurl = 'http://www.ecrecruit.com/'
loginurl = 'http://www.ecrecruit.com/en/jobseeker/user_login.php?Action=Login'

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
'''

'''
import urllib2  
import urllib  
import cookielib  
import requests

def renrenBrower(url,user,password):     
 login_page = "http://www.ecrecruit.com/en/jobseeker/user_login.php?Action=Login"  
 try:  
  cj = cookielib.CookieJar()   
  opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
  opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]  
  data = urllib.urlencode({"jobseeker_email":user,"jobseeker_password":password})  
  opener.open(login_page,data)  
  op=opener.open(url)  
  data= op.read()  
  return data  
 except Exception,e:  
  print str(e)  
print renrenBrower("http://www.ecrecruit.com/en/jobseeker/user_login.php?Action=Login","hui@hui.com","123123") 
'''

'''
import requests
kb_url = 'http://www.ecrecruit.com/en/jobseeker/user_login.php?Action=LoginPost'
login_data = {
    'jobseeker_email':'hui@hui.com',
    'jobseeker_password':'123123'
}
loginreqsession = requests.session()
logincontent = loginreqsession.post(kb_url,data = login_data).content.decode('utf-8')
print logincontent
#print loginreqsession
lucky_url = 'http://www.ecrecruit.com/en/jobseeker/user_message.php?Action=message'
print(loginreqsession.get(lucky_url).content.decode('utf-8'))
'''

'''
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
'''


'''
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0] 
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = 0
        return ret
		
k = KMP()
s = 'aababcabcdabcdeabcdef'
n = 'abcdeab'
next = k.partial(n)
status = k.search(s,n)
print next
print status
'''
'''###############################################'''

'''
void getNext(char a[], int n, int next[]){
	int i, j;
	i = 0;
	next[0] = -1;#首元跳转值为-1
	j = -1;
	#递推得到next表中剩余值
	while(i < n){
		if(j == -1 || a[i] == a[j]){
			++i;
			++j;
			next[i] = j;
		}
		else{
			j = next[j];
		}
	}
}
'''
'''
def p(str):
	s = str
	length = len(str)
	k = -1 
	j = 0
	next = [0]*length
	next[0] = -1
	while j <length -1:
		if s[j] == s[k] or k == -1:
			if s[j=j+1] == s[k=k+1]:
				next[j] = next[k]
			else:
				next[j] = k
		else:
			k = next[k]
	return next
ss = 'abcdeab'
print p(ss)
'''

'''
import os
class UNDERFLOW(Exception):pass # 下溢
class OVERFLOW(Exception):pass # 上溢
class Stack(object):
    def __init__(self, size):
        self.top = -1 #指向最新插入的元素
        self.S = [0 for _ in range(0,size)]
        self.size = size
    #测试一个栈是否为空
    STACK_EMPTY = lambda self: self.top == -1
    #测试一个栈是否已满
    STACK_FULL = lambda self: self.top == self.size-1
    #插入元素到栈顶
    def PUSH(self,x):
        if self.STACK_FULL():
 
               raise OVERFLOW("stack is full")
        self.top += 1
        self.S[self.top] = x
    #将栈顶元素返回并删除
    def POP(self):
        if self.STACK_EMPTY():
            raise UNDERFLOW("stack is empty")
        x = self.S[self.top]
        self.top -= 1
        return x
		
class s(object):
	def __init__(self,size):
		self.top = -1;
		self.show = [0 for _ in range(0,size)]
		self.size = size
	def push(self,item):
		self.top += 1
		self.show[self.top] = item
	def delete(self):
		self.show[self.top] = 0
		self.top -= 1
		
class queue(object):
	def __init__(self,size):
		self.last = -1
		self.size = size
		self.head = 0
		self.show = [0 for _ in range(0,size)]
	def add(self,item):
		self.last += 1
		self.show[self.last] = item
	def delete(self):
		self.show[self.last] = 0
		self.head += 1

class requeue(object):
	def __init__(self,size):
		self.last = 0
		self.size = size
		self.head = 0
		self.show = [0 for _ in range(0,size)]
	def add(self,item):
		if (self.last + 1) % self.size == self.head :
			return 'full'
		else:
			self.last = (self.last + 1) % self.size
			self.show[self.last] = item
			return self.show
	def delete(self):
		if self.last == self.head:
			return 'empty'
		else:
			self.show[self.head] = 0
			self.head = (self.head + 1) % self.size
			return self.show
'''


