
import logging
import urllib.request
import time
import telepot
import config
import sys
import socket

def isConnected(url):
    connected = False
    try:
        response = urllib.request.urlopen(url, timeout=5)
        connected = True
    except Exception as e:
        logging.error(e)

    return connected

def retrieveIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    return s.getsockname()[0]

def usage():
    print("Usage : python3 %s {config file}" % sys.argv[0])

if __name__ == "__main__":
    logging.basicConfig(#filename='teller.log',
                        format='[%(asctime)s] %(levelname)s  %(message)s',
                        level=logging.DEBUG)

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    url = "https://telegram.me/tell_me_your_ip_bot"

    while isConnected(url) == False:
        logging.info("Not connected.")
        time.sleep(10)

    logging.info("Connected to url %s", url)

    ip = retrieveIp()

    config = config.TelegramConfig()
    config.load(sys.argv[1])
    token = config.token
    chatId = config.myChatId

    logging.debug("Telegram bot token: %s", token)
    logging.debug("My chat id: %s", chatId)

    bot = telepot.Bot(token)
    bot.sendMessage(chatId, "My IP is %s" % ip)
    logging.info("Message is sent.")
