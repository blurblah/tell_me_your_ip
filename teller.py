
import logging
import urllib.request
import time
import telepot
import config
import sys
import netifaces

def isConnected(url):
    connected = False
    try:
        response = urllib.request.urlopen(url, timeout=1)
        connected = True
    except Exception as e:
        logging.error(e)

    return connected

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

    addresses = []
    for nif in netifaces.interfaces():
        addressInfo = "Interface:%s Address:%s" % (nif, netifaces.ifaddresses(nif))
        logging.info(addressInfo)
        addresses.append(addressInfo)

    config = config.TelegramConfig()
    config.load(sys.argv[1])
    token = config.token
    chatId = config.myChatId

    logging.debug("Telegram bot token: %s", token)
    logging.debug("My chat id: %s", chatId)

    bot = telepot.Bot(token)
    bot.sendMessage(chatId, addresses)
    logging.info("Message is sent.")