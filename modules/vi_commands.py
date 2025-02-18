from modules.viksa import *

logging.info("Загружен модуль EY_COMMANDS")

@bot.command(name="info", description="Основная информация (Время работы, разработчики, версия бота)")
async def info(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Viksa", description=f"Текущая версия: {viksa_ver}", colour=0xFFE933)
    embed.add_field(name="Прочее", value=f"Дистрибутив: {viksa_distro}, статус профайлера {PROFSTATE}")
    embed.add_field(name="Время работы", value=f"{cursession}", inline=False)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Использование команды: /info пользователем {ctx.author.name} с id: {ctx.author.id}")

@bot.command(name="github", description="Вывод Github'a Viksa")
async def github(ctx):
    logging.info(f"Использование команды: /github пользователем {ctx.author.name} с id: {ctx.author.id} | Спасибки <3")
    embed = discord.Embed(title='Github', description="Страница Viksa в Github: https://github.com/viksapi2k/viksa", colour=0xFFE933)
    await ctx.response.send_message(embed=embed)
