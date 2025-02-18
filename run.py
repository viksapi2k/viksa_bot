from modules.viksa import *

from modules.vi_msg import *
from modules.vi_commands import *
from modules.warn_system import *

if settings['token'] == "TOKEN" or "":
    logging.error("Ууупс... вы забыли добавить токен для Eybie. Получить токен можно тут: https://discord.com/developers/applications, токен вписывается в config_eybie.py")
else:
    logging.info("Токен подходит, попытка запуска...")
    bot.run(settings['token'])
    logging.info("Попытка успешна. Приятного использования Eybie!")

if KeyboardInterrupt:
    logging.info("Выключение...")
