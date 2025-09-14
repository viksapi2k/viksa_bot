from modules.viksa import *

logging.info("Module loaded VI_COMMANDS")

@bot.command(name="info", description="Main information (Uptme, developers, bot version)")
async def info(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Viksa", description=f"Current version: {viksa_ver}", colour=0xFFE933)
    embed.add_field(name="Other", value=f"Distribution: {viksa_distro}")
    embed.add_field(name="Uptime", value=f"{cursession}", inline=False)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Command usage: /info by {ctx.author.name} with id: {ctx.author.id}")

@bot.command(name="github", description="Viksa's Github")
async def github(ctx):
    logging.info(f"Command usage: /github by {ctx.author.name} with id: {ctx.author.id} | tysm")
    embed = discord.Embed(title='Github', description="Viksa's Github-page: https://github.com/viksapi2k/viksa", colour=0xFFE933)
    await ctx.response.send_message(embed=embed)

@bot.command(name="rules", description="Send server rules")
@has_permissions(administrator=True)
async def rules(ctx):
    if os.path.exists('rules.txt'):
        with open("rules.txt", "r") as file:
            rules_txt = file.read()
    else:
        rules_txt = "There is no \"rules.txt\" in Viksa's root"
    embed = discord.Embed(title=' ', description=f'`{rules_txt}`', colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Command usage: /rules by {ctx.author.name} with id: {ctx.author.id}")

@rules.error
async def rules_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)