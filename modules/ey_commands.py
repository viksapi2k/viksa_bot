from modules.api import *

module_loaded(f"Ey_CommandPack")

@bot.command(name="info", description="Основная информация (Время работы, разработчики, версия бота)")
async def info(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Eybie", description=f"Текущая версия: {eybie_ver}", colour=0xFFE933)
    embed.add_field(name="Время работы", value=f"{cursession}", inline=False)
    embed.add_field(name="Разработчик", value="Eyndjl#2356", inline=True)
    embed.add_field(name="Оф.сайт", value="https://eyndjl.github.io", inline=True)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    print(f"[INFO] Использование команды: /info пользователем", ctx.author.name, "с id:",ctx.author.id)

@bot.command(name="rules", description="Вывод правил сервера") #Оставлю так пока не найду алтернативное решение
@has_permissions(administrator=True)
async def rules(ctx):
    if os.path.exists('rules.txt'):
        with open("rules.txt", "r") as file:
            rules_txt = file.read()
    else:
        rules_txt = "Файл \"rules.txt\" отсутствует в корне Eybie :("
    embed = discord.Embed(title=' ', description=f'`{rules_txt}`', colour=0xFFE933)
    embed1 = discord.Embed(title=message_sent, description=" ", colour=0xFFE933)
    await ctx.send(embed=embed)
    await ctx.response.send_message(embed=embed1, ephemeral=True)
    print(f"[INFO] Использование команды: /rules пользователем", ctx.author.name, "с id:",ctx.author.id)

@rules.error
async def rules_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)

@bot.command(name="github", description="Вывод Github'a Eybie")
async def github(ctx):
    print(f"[DingoLingo] Использование команды: /github пользователем", ctx.author.name, "с id:",ctx.author.id)
    embed = discord.Embed(title='Github', description="Страница Eybie в Github: https://github.com/Eyndjl/eybie", colour=0xFFE933)
    await ctx.response.send_message(embed=embed)