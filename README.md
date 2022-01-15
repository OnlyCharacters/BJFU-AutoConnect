# BJFU校园网自动连接

- 使用方法：

  - **Windows**
  
    1. 前往 [release](https://github.com/OnlyCharacters/BJFU-AutoConnect/releases) 页面下载 BJFU-AutoConnect.zip
  
    2. 下载完成后，解压
  
    3. 打开 xyw.txt，在第一行填上学号，第二行填上登录的密码，保存退出
  
    4. 双击 BJFU-AutoConnect.exe 运行即可
  
  - **Linux 或其他支持 Python 的操作系统**
  
    1. 安装 git, Python3
  
    2. 安装 Python3 的 requests 包
  
    3. ```bash
       git clone https://github.com/OnlyCharacters/BJFU-AutoConnect
       ```
  
    4. 打开 xyw.txt，在第一行填上学号，第二行填上登录的密码，保存退出
  
    5. python3 BJFU-AutoConnect.py 运行
  
  - 其他使用技巧
  
    1. 如果你需要联网的设备无法使用 Python，你可以在有 Python 环境的电脑上，装好 requests 包，然后下载源码
  
    2. 在源码中找到
  
       ```python
       'wlan_user_ip': ip,
       ```
  
    3. 将 ip 修改为你需要联网设备 ip 的字符串，如你的设备 ip 是 10.1.1.10，修改结果如下
  
       ```python
       'wlan_user_ip': '10.1.1.10',
       ```
  
    4. 运行源码
  

如果有报毒情况，把文件还原添加信任即可。

源代码是公开的，你也可以在 Windows 上自行安装 python3，并安装 requests 包，然后直接运行源代码。

