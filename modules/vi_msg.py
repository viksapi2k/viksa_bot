from modules.viksa import *

logging.info("Module loaded VI_MSG")

@bot.command(name="say", description="Send a message on behalf of the bot")
@has_permissions(administrator=True)
async def say(ctx, text):
    await ctx.send(text)
    embed = discord.Embed(title=message_sent, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Command usage: /say by {ctx.author.name} with id: {ctx.author.id} | Текст сообщения: \"{text}\"") 

@say.error
async def say_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
