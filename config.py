
import os
import configparser

class TelegramConfig:

    def load(self, configFile):
        if os.path.exists(configFile) == False:
            raise Exception("%s No such file or directory" % configFile)

        config = configparser.ConfigParser()
        config.read(configFile)
        self.token = config.get("Telegram", "bot_token")
        self.myChatId = config.get("Telegram", "my_chat_id")