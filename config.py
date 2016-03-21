
import os
import configparser


class TelegramConfig:

    token = ''
    myChatId = ''

    def load(self, config_file):
        if not os.path.exists(config_file):
            raise Exception("%s No such file or directory" % config_file)

        config = configparser.ConfigParser()
        config.read(config_file)
        self.token = config.get("Telegram", "bot_token")
        self.myChatId = config.get("Telegram", "my_chat_id")