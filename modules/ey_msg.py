from modules.eybie import *

logging.info("Загружен модуль EY_MSG")

@bot.command(name="say", description="Вывод сообщения от имени бота")
@has_permissions(administrator=True)
async def say(ctx, text):
    await ctx.send(text)
    embed = discord.Embed(title=message_sent, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Использование команды: /say пользователем {ctx.author.name} с id: {ctx.author.id} | Текст сообщения: \"{text}\"") 

@say.error
async def say_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)