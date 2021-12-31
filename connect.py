import requests
import hashlib


def cutString(str, s_start, s_end):
    pos_start = str.find(s_start)
    str_temp = str[pos_start + len(s_start):-1]
    pos_end = str_temp.find(s_end)
    return str_temp[:pos_end]

def md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

r = requests.get('http://202.204.122.1/index.jsp')
cookie_r = r.cookies
token1 = '<input type="hidden" id="password8" name="password8" value=""/>'
token2 = '<input type="hidden" id="action" name="action" value="connect"/>'
token3 = 'name="ip" value="'
token4 = 'name="no" value="'
token5 = '"'
form_text = r.text
str1 = cutString(form_text, token1, token2)
ip = cutString(str1, token3, token5)
no = cutString(str1, token4, token5)
username = ''
password = ''
with open('xyw.txt','r') as f:
    lines=f.readlines()
    username = lines[0].rstrip()
    password = lines[1].rstrip()

password1 = md5(password)
password2 = md5(password1 + no)

dataToPost = {
    "username8" : username,
    "password8" : password2,
    "ip" : ip,
    "no" : no,
    "action" : "disconnect"
}

# varify
r = requests.post('http://202.204.122.1/checkLogin.jsp', data=dataToPost, cookies=cookie_r, allow_redirects=True)
# get userid
return_text = r.text
userid = cutString(return_text, 'userid=', '&')
# connect
dataToGet = {
    'userid': userid,
    'ip': ip,
    'type': "2"
}
r = requests.get('http://202.204.122.1/user/network/connect_action.jsp', cookies=cookie_r, params=dataToGet)
