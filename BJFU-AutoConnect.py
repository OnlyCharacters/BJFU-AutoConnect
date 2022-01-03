import requests
import base64
import socket

def cutString(str, s_start, s_end):
    pos_start = str.find(s_start)
    str_temp = str[pos_start + len(s_start):-1]
    pos_end = str_temp.find(s_end)
    return str_temp[:pos_end]

username = ''
password = ''
with open('xyw.txt','r') as f:
    lines=f.readlines()
    username = lines[0].rstrip()
    password = lines[1].rstrip()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('192.168.55.2', 8800))
if result == 0:
    # dor_wifi
    r = requests.get('http://202.204.122.1/index.jsp')
    wifi_url = r.url
    p1 = cutString(wifi_url, 'p1=', '&')
    p2 = cutString(wifi_url, 'p2=', '&')
    p3 = cutString(wifi_url, 'p3=', '&')
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

r = requests.get('http://10.1.1.10/')
text = r.text
ip = cutString(text, 'v46ip=\'', '\'')
pass_base = base64.b64encode(password.encode()).decode()
dataToGet = {
    'callback': 'dr1004',
    'login_method': 1,
    'user_account': username,
    'user_password': pass_base,
    'wlan_user_ip': ip,
    'wlan_user_ipv6': '',
    'wlan_user_mac': '000000000000',
    'wlan_ac_ip': '',
    'wlan_ac_name': '',
    'jsVersion': '4.1.3',
    'terminal_type': 1,
    'type': 1,
    'lang': 'en',
    'v': 1218,
    'lang': 'en',
}
r = requests.get('http://10.1.1.10:801/eportal/portal/custom/auth', params=dataToGet)
