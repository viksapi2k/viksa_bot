import discord, random, datetime, time, os, gettext, art
from time import sleep
from discord.ext import commands
from discord.ext.commands import has_permissions
from asyncio import sleep as asleep
from config_eybie import settings, version_info, splashes

#Информация о текущей версии бота
eybie_codename = version_info['codename']
eybie_reldate = version_info['rel_date']
eybie_ver = version_info['version']

art.tprint(f"|Eybie  v{eybie_ver}|") #Поставил два пробела из-за слишком малого расстояния между символами в art.tprint
print("============================================================\n")
sleep(3)
print("[INFO] Запуск модулей...")

#Необходимо для работоспособности основных функций
bot = discord.Bot()
startTime = time.time()

#Сокращения сообщений на все случаи жизни
error_text = "Возникла ошибка при выполнении данной команды :("
message_sent = "Сообщение отправлено ✅"

#Стандартные функции
def module_loaded(module_name):
    return print(f"[INFO] Загружен {module_name}")

@bot.event
async def on_ready():
    while True: #Может быть не самый лучший способ обновления статуса, но сойдёт
        random_splash = random.randint(0, len(splashes) - 1)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"v{eybie_ver} | {splashes[random_splash]}"))
        await asleep(7)

@bot.command(name="devinf", description="Краткая информация для разработчиков")
@has_permissions(administrator=True)
async def devinf(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Eybie", description=f"Версия: {eybie_ver} \n Кодовое имя: {eybie_codename} \n Дата релиза: {eybie_reldate} \n Длительность текущей сессии: {cursession}", colour=0xFFE933)
    embed.add_field(name="Список сплешей", value=f"{splashes}", inline=True)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    print(f"[INFO] Использование команды: /devinf пользователем", ctx.author.name, "с id:",ctx.author.id)

@devinf.error
async def devinf_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)