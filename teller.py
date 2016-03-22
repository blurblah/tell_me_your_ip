
import logging
import urllib.request
import time
import sys
import bot


def is_connected(url_string):
    connected = False
    try:
        urllib.request.urlopen(url_string, timeout=5)
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

    config_file = sys.argv[1]
    url = "https://telegram.me/tell_me_your_ip_bot"

    while not is_connected(url):
        logging.info("Not connected.")
        time.sleep(10)

    logging.info("Connected to url %s", url)

    telegram_bot = bot.TelegramBotHandler(config_file)
    telegram_bot.start()
