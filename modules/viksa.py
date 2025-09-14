import discord, random, datetime, time, os, art, logging, zipfile
from time import sleep
from discord.ext import commands
from asyncio import sleep as asleep
from discord.ext.commands import has_permissions
from config_viksa import settings, version_info, splashes

#Logs dir
if not os.path.isdir(f"logs"):
    os.mkdir(f'logs')

#Archive logs (if they exist)
if os.path.isfile("logs/latest.log"):
    with zipfile.ZipFile(f'logs/{str(datetime.datetime.now())}.zip', 'w') as log_archive:
        log_archive.write('logs/latest.log')
    os.remove("logs/latest.log")

#Bot version info
viksa_codename = version_info['codename']
viksa_reldate = version_info['rel_date']
viksa_ver = version_info['version']
viksa_distro = version_info['distribution']
viksa_name = settings['bot_name']
viksa_avatar = open(settings['avatar_path'], 'rb').read()

#For main funcs
bot = discord.Bot()
startTime = time.time()

error_text = "Oops... something wrong :("
message_sent = "Message sent ✅"

#Default funcs
logging.basicConfig(
    level=logging.INFO, #Уровень логирования
    format="(%(asctime)s) [%(levelname)s] %(message)s", #Формат логов
    handlers=[
        logging.FileHandler("logs/latest.log"), #Директория логов
        logging.StreamHandler()
    ]
)

#Launching startup scripts
@bot.event
async def on_ready():
    logging.info("Changing name...")
    await bot.user.edit(username=viksa_name) #Изменение имени согласно настройкам
    logging.info(f"Name changed to \"{viksa_name}\"")
    logging.info("Changing avatar...")
    await bot.user.edit(avatar=viksa_avatar)
    logging.info(f"Avatar changed to \"{settings['avatar_path']}\"")
    while True:
        random_splash = random.randint(0, len(splashes) - 1)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"v{viksa_ver} | {splashes[random_splash]}"))
        await asleep(7)

#Стандартные команды
@bot.command(name="devinf", description="Information for developers")
@has_permissions(administrator=True)
async def devinf(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Viksa", description=f"Version: {viksa_ver} \n Codename: {viksa_codename} \n Distribution: {viksa_distro} \n Release Date: {viksa_reldate} \n Uptime: {cursession}", colour=0xFFE933)
    embed.add_field(name="Splashes list:", value=f"{splashes}", inline=True)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Command usage: /devinf by{ctx.author.name}, with id: {ctx.author.id}")

@devinf.error
async def devinf_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)

art.tprint(f"|Viksa  v{viksa_ver}|")
print("========================================================================\n")
sleep(0.5)
if os.path.isfile("changelog.txt"):
    print(open("changelog.txt", "r", encoding='UTF-8').read() + "\n")
else:
    print("There is no changelog.txt!\n")
sleep(2)
logging.info(f"Viksa v{viksa_ver} starting!")
logging.info("Loading modules...")
