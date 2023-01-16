import discord, random, datetime, time, os, art, logging, zipfile
from time import sleep
from discord.ext import commands
from asyncio import sleep as asleep
from discord.ext.commands import has_permissions
from config_eybie import settings, version_info, splashes

#Место для проверки скриптов, это номально если тут пусто :)

#Необходимые директории для нормальной работы
if not os.path.isdir(f"logs"):
    os.mkdir(f'logs')

#Архивирование логов предыдущей сессии (при наличии)
if os.path.isfile("logs/latest.log"):
    with zipfile.ZipFile(f'logs/{str(datetime.datetime.now())}.zip', 'w') as log_archive:
        log_archive.write('logs/latest.log')
    os.remove("logs/latest.log")

#Информация о текущей версии бота
eybie_codename = version_info['codename']
eybie_reldate = version_info['rel_date']
eybie_ver = version_info['version']
eybie_distro = version_info['distribution']
eybie_name = settings['bot_name']

#Необходимо для работоспособности основных функций
bot = discord.Bot()
startTime = time.time()

#Сокращения сообщений на все случаи жизни
error_text = "Возникла ошибка при выполнении данной команды :("
message_sent = "Сообщение отправлено ✅"

#Стандартные функции
logging.basicConfig(
    level=logging.INFO, #Уровень логирования
    format="(%(asctime)s) [%(levelname)s] %(message)s", #Формат логов
    handlers=[
        logging.FileHandler("logs/latest.log"), #Директория логов
        logging.StreamHandler()
    ]
)

#PROFSTATE = "PROFSTATE" #основа для будущего подобия профайлера (если не передумаю)

#ARGS = "ARGS" #основа для параметров запуска

#Обновление статуса
@bot.event
async def on_ready():
    logging.info("Установка имени...")
    await bot.user.edit(username=eybie_name) #Изменение имени согласно настройкам
    logging.info(f"Имя Eybie изменено на \"{eybie_name}\"")
    while True:
        random_splash = random.randint(0, len(splashes) - 1)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"v{eybie_ver} | {splashes[random_splash]}"))
        await asleep(7)

#Стандартные команды
@bot.command(name="devinf", description="Краткая информация для разработчиков")
@has_permissions(administrator=True)
async def devinf(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Eybie", description=f"Версия: {eybie_ver} \n Кодовое имя: {eybie_codename} \n Дистрибутив: {eybie_distro} \n Дата релиза: {eybie_reldate} \n Длительность текущей сессии: {cursession}", colour=0xFFE933)
    embed.add_field(name="Список сплешей", value=f"{splashes}", inline=True)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Использование команды: /devinf пользователем {ctx.author.name}, с id: {ctx.author.id}")

@devinf.error
async def devinf_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)

#Скрипты при запуске
art.tprint(f"|Eybie  v{eybie_ver}|") #Поставил два пробела из-за слишком малого расстояния между символами в art.tprint
print("========================================================================\n")
sleep(0.5)
if os.path.isfile("changelog.txt"):
    print(open("changelog.txt", "r", encoding='UTF-8').read() + "\n")
else:
    print("Отсутствует changelog.txt!\n")
sleep(2)
logging.info(f"Eybie v{eybie_ver} запущен!")
logging.info("Запуск модулей...")