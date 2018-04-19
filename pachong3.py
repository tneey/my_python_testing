
import requests
kb_url = ''
login_data = {
    'jobseeker_email':'',
    'jobseeker_password':''
}
loginreqsession = requests.session()
logincontent = loginreqsession.post(kb_url,data = login_data).content.decode('utf-8')
print logincontent
#print loginreqsession
lucky_url = ''
print(loginreqsession.get(lucky_url).content.decode('utf-8'))

		
