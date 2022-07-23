from modules.api import *
from asyncio import sleep

print("[INFO] Успешно загружен EY_status")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Инфо: ;info, помощь: ;help"))