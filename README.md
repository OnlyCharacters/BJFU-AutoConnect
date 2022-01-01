# BJFU校园网自动连接
## 可以直接执行.py，前提是安装python3，并且安装了requests包
如果不愿意安装python3或者不想安装requests包，可以去[release](https://github.com/OnlyCharacters/BJFU-AutoConnect/releases)找打包好的可执行文件

## xyw.txt 里第一行填写学号，第二行填写校园网密码
connect.py 用于有线

connect_wifi.py 用于连接宿舍区域的bjfu-wifi

disconnect.py 用于断开连接

connect_wifi2.py 用于连接学研、食堂（登录界面长这个样的）区域的bjfu-wifi


话说为什么学校有两个WiFi认证？

学研、西配、食堂使用一套WiFi认证，宿舍使用另一套WiFi认证，为什么？

- 2021-12-31
  学校似乎准备了新的登陆界面，但目前此脚本依然可用

- 2022-01-01
  信息中心更新完之后，有线（connect.py）g了，connect_wifi.py和connect_wifi2.py暂时可用，disconnect.py也g了

  新的登录逻辑真复杂
