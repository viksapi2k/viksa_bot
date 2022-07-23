from modules.api import *

print("[INFO] Успешно загружен EY_commands")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Уупс...", description="Данная функция временно недоступна или вовсе не реализована :(", colour=0xFFE933)
        await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Eybie", description=f"Текущая версия: {eybie_ver}", colour=0xFFE933)
    embed.add_field(name="Время работы", value=f"{str(datetime.timedelta(seconds=int(round(time.time()-startTime))))}", inline=False)
    embed.add_field(name="Разработчик", value="Eyndjl#2356", inline=True)
    embed.add_field(name="Оф.сайт", value="Недоступен", inline=True)
    await ctx.send(embed=embed)
    print(f"[INFO] Использование команды: {prefix}info пользователем", ctx.author.name, "с id:",ctx.author.id)

@bot.command()
async def version_info(ctx):
    embed = discord.Embed(title="Информация о версии", description=f"Текущая версия: {eybie_ver}\nДата выпуска: {eybie_reldate}\nКодовое имя: {eybie_codename}", colour=0xFFE933)
    await ctx.send(embed=embed)
    print(f"[INFO] Использование команды: {prefix}version_info пользователем", ctx.author.name, "с id:",ctx.author.id)

@bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Помощь Eybie", description="", colour=0xFFE933)
    embed.add_field(name="Основные", value=";info - Основная информация(аптайм, разработчики и версия)\n;version_info - Подробности о версии;\n;support - Поддержать копеечкой", inline=False)
    embed.add_field(name="Администрирование", value=";warn - Добавить варн пользователю", inline=True)
    await ctx.send(embed=embed)
    print(f"[INFO] Использование команды: {prefix}help пользователем", ctx.author.name, "с id:",ctx.author.id)

@bot.command()
@has_permissions(administrator=True)
async def rules(ctx):
    if os.path.exists('rules.txt'):
        with open("rules.txt", "r") as file:
            rules_txt = file.read()
    else:
        rules_txt = "Файл rules.txt пуст :("
    embed = discord.Embed(title=' ', description=f'`{rules_txt}`', colour=0xFFE933)
    await ctx.send(embed=embed)
    await ctx.message.delete()
    print(f"[INFO] Использование команды: {prefix}rules пользователем", ctx.author.name, "с id:",ctx.author.id)

@bot.command()
async def github(ctx):
    print(f"[DingoLingo] Использование команды: {prefix}github пользователем", ctx.author.name, "с id:",ctx.author.id)
    embed = discord.Embed(title='Github', description="Страница Eybie в Github: https://github.com/Eyndjl/eybie", colour=0xFFE933)
    await ctx.send(embed=embed)