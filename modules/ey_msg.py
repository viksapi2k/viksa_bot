from modules.api import *

print("[INFO] Успешно загружен EY_msg")

@bot.command()
@has_permissions(administrator=True)
async def say(ctx, *args):
    text = ''
    for item in args:
        text = text + item + ' '
    await ctx.send(text)
    await ctx.message.delete()
    print("[INFO] Использование команды: say пользователем", ctx.author.name, "с id:",ctx.author.id)