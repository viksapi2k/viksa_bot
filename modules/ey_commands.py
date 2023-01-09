from modules.api import *

logging.info("Загружен модуль EY_COMMANDS")

@bot.command(name="info", description="Основная информация (Время работы, разработчики, версия бота)")
async def info(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Eybie", description=f"Текущая версия: {eybie_ver}", colour=0xFFE933)
    embed.add_field(name="Время работы", value=f"{cursession}", inline=False)
    embed.add_field(name="Разработчик", value="Eyndjl#2356", inline=True)
    embed.add_field(name="Оф.сайт", value="https://eyndjl.github.io", inline=True)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Использование команды: /info пользователем {ctx.author.name} с id: {ctx.author.id}")

@bot.command(name="github", description="Вывод Github'a Eybie")
async def github(ctx):
    logging.info(f"Использование команды: /github пользователем {ctx.author.name} с id: {ctx.author.id} | Спасибки <3")
    embed = discord.Embed(title='Github', description="Страница Eybie в Github: https://github.com/Eyndjl/eybie", colour=0xFFE933)
    await ctx.response.send_message(embed=embed)