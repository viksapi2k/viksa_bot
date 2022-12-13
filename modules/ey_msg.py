from modules.api import *

module_loaded(f"Ey_Messages")

@bot.command(name="say", description="Вывод сообщения от имени бота") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@has_permissions(administrator=True)
async def say(ctx, text):
    await ctx.send(text)
    embed = discord.Embed(title=message_sent, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    print("[INFO] Использование команды: /say пользователем", ctx.author.name, "с id:",ctx.author.id) 

@say.error
async def say_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)