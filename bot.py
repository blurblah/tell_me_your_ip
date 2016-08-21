
import config
import logging
import telepot
import time
import socket


class TelegramBotHandler:

    CMD_START = '/start'
    CMD_GET_IP = '/tell_me_your_ip'
    KEYBOARD = {'keyboard': [[CMD_START], [CMD_GET_IP]]}

    def __init__(self, config_file):
        cfg = config.TelegramConfig()
        try:
            cfg.load(config_file)
            token = cfg.token
            self.bot = telepot.Bot(token)
            logging.debug("Telegram bot token: %s", token)
        except Exception as e:
            logging.error(e)

    def start(self):
        if self.bot is not None:
            self.bot.message_loop(self.handle_message)
            logging.info("Telegram bot started.")
            while True:
                time.sleep(10)

    def handle_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        logging.debug(msg)
        logging.debug("content_type:%s chat_type:%s chat_id:%s" % (content_type, chat_type, chat_id));

        if content_type == 'text':
            reply_message = "Command : %s or %s" % (self.CMD_START, self.CMD_GET_IP)
            tokens = msg['text'].split(' ')
            command = tokens[0].lower()

            if command == self.CMD_GET_IP:
                ip = self.retrieve_ip()
                logging.info("IP:%s", ip)
                reply_message = "My IP is %s" % ip

            self.bot.sendMessage(chat_id, reply_message, reply_markup=self.KEYBOARD)

    def retrieve_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        return s.getsockname()[0]
