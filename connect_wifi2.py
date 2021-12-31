import requests

def cutString(str, s_start, s_end):
    pos_start = str.find(s_start)
    str_temp = str[pos_start + len(s_start):-1]
    pos_end = str_temp.find(s_end)
    return str_temp[:pos_end]

r = requests.get('http://202.204.122.249:8080/index.html')
cookie_r = r.cookies
token1 = '<input type="text" class="am-form-field" name="ip" id="ip" value="'
form_text = r.text
ip = cutString(form_text, token1, '"')
username = ''
password = ''
with open('xyw.txt','r') as f:
    lines=f.readlines()
    username = lines[0].rstrip()
    password = lines[1].rstrip()
dataToPost1 = {
    "username": username,
    "password": password,
    "ip": ip,
    "nasip": "",
    "action": "连接网络",
}

r = requests.post('http://202.204.122.249:8080/Login', cookies=cookie_r, data=dataToPost1)
