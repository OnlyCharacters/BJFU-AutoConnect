import requests

def cutString(str, s_start, s_end):
    pos_start = str.find(s_start)
    str_temp = str[pos_start + len(s_start):-1]
    pos_end = str_temp.find(s_end)
    return str_temp[:pos_end]

r = requests.get('http://202.204.122.1/index.jsp')
wifi_url = r.url
p1 = cutString(wifi_url, 'p1=', '&')
p2 = cutString(wifi_url, 'p2=', '&')
p3 = cutString(wifi_url, 'p3=', '&')
username = ''
password = ''
with open('xyw.txt','r') as f:
    lines=f.readlines()
    username = lines[0].rstrip()
    password = lines[1]
dataToPost1 = {
    "p1": 3,
    "p2": p2,
    "p3": p3,
    "p4": "0",
    "p5": username,
    "p6": password,
    "p7": "0",
    "PtUser": username,
    "PtPwd": password,
    "PtButton": "logon",
}

r = requests.post('http://192.168.55.2:8800/ext_captive_portal.html', data=dataToPost1)
