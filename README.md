Tell me your ip
===============
Booting 시점에 Device의 IP를 telegram으로 전송하는 기능을 수행하는 script
Prerequisite
------------
Python3

telepot (python module)

~~netifaces (python module)~~
Install
-------
Python3와 python3-pip가 설치된 상태에서 telepot를 설치한다.
#### OS X
```
sudo pip3 install telepot
sudo pip3 install telepot --upgrade
```
#### Raspbian
pip-3.2 설치된 상태
```
sudo pip-3.2 install telepot
sudo pip-3.2 install telepot --upgrade
```
Usage
-----
#### Telegram bot 등록
BotFather를 통해 신규 bot을 등록하고 token을 따로 기록한다.
#### Chat ID
등록한 bot을 이용해 본인의 chat_id를 구해서 기록해둔다
#### config-template.properties 수정
Property file의 bot_token, my_chat_id 항목에 기록해둔 token과 chat_id를 입력하고 저장한다.
#### Run
아래의 명령으로 실행
```
python3 teller.py {config_file}
```
#### Init script 등록
tell_me_your_ip.sh 를 적당히 수정해서 booting 시점에 동작하는 script로 등록한다.
Reference
---------
https://github.com/nickoala/telepot#installation

https://pypi.python.org/pypi/netifaces

https://core.telegram.org/bots
History
-------
#### 2016-03-18
Removed netifaces library
