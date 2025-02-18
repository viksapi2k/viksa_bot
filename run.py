from modules.viksa import *

from modules.vi_msg import *
from modules.vi_commands import *
from modules.warn_system import *

if settings['token'] == "TOKEN" or "":
    logging.error("Oops... You forgot to add a token for Viksa. You can get it here: https://discord.com/developers/applications, token fits into config_viksa.py")
else:
    logging.info("Token is valid. Trying to start...")
    bot.run(settings['token'])
    logging.info("Bot is running.")

if KeyboardInterrupt:
    logging.info("Turning off...")
