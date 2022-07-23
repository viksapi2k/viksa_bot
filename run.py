from modules.ey_msg import *
from modules.ey_commands import *
from modules.warn_system import *
#from modules.ey_status import * #Конфликтует с modules.dingolingo. Если modules.dingolingo отключён, включаем modules.ey_status

from modules.dingolingo import *

bot.run(settings['token'])
if KeyboardInterrupt:
    print("\n[INFO] Выключение бота...")