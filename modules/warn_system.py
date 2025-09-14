from modules.viksa import *
import sqlite3

logging.info("Module loaded WARN_SYSTEM")

#Settings
WARNSCOUNT = 3 #Max warns. >3 = timeout
BLOCKDURATION = 10080 #Timeout duration

#Default folders
if not os.path.isdir(f"database/servers"):
    logging.info("There is no \"database/servers\". Creating...")
    os.mkdir(f'database')
    os.mkdir(f'database/servers')

#Warn system. Based on sqlite3.
@bot.command(name="warn", description="Warn user")
@has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, reason: str):
    logging.info(f"Command usage: /warn by {ctx.author.name} with id: {ctx.author.id} | Reason: \"{reason}\"") 
    serverid = ctx.guild.id
    if not os.path.isdir(f"database/servers/{serverid}"):
        os.mkdir(f'database/servers/{serverid}')
    sqlite_conn = sqlite3.connect(f'database/servers/{serverid}/users.db')
    cursor = sqlite_conn.cursor()
    userid = "id" + str(member.id)
    now = datetime.datetime.now()
    reason_full = "[" + str(now.day) + "-"+ str(now.month)+ "-" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "] " + reason #Приписка даты варна к причине
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {userid}(reason TEXT);")
    cursor.execute(f"INSERT INTO {userid} (reason) VALUES('{reason_full}');")
    sqlite_conn.commit()
    warns = len(cursor.execute(f"SELECT * FROM {userid}").fetchall())
    embed = discord.Embed(title=f'User {member.name} was warned.', description=f'Reason: {reason}', colour=0xFFE933)
    await ctx.response.send_message(embed=embed)
    if warns >= WARNSCOUNT:
        logging.info(f"User {member.name} was temporary blocked (warns >= {WARNSCOUNT})")
        embed2 = discord.Embed(title="The user's access to text and voice chat was restricted for 7 days for violating the rules.", description='', colour=0xFFE933)
        await member.timeout_for(datetime.timedelta(minutes=BLOCKDURATION))
        await ctx.send(embed=embed2)
        cursor.execute(f"DELETE FROM {userid}")
        sqlite_conn.commit()
    else:
        pass
    sqlite_conn.close()

@warn.error
async def warn_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)

@bot.command(name="warns", description="Show user's warn list")
@has_permissions(administrator=True)
async def warns(ctx, user:discord.User):
    logging.info(f"Command usage: /warns by {ctx.author.name} with id: {ctx.author.id}")
    serverid = ctx.guild.id
    sqlite_conn = sqlite3.connect(f'database/servers/{serverid}/users.db')
    cursor = sqlite_conn.cursor()
    userid = "id" + str(user.id)
    warns_reasons = cursor.execute(f"SELECT reason FROM {userid}").fetchall()
    warns = len(warns_reasons)
    reasons_clean = str(warns_reasons).replace("[(\'", '').replace("(\'", '').replace("\',)", '').replace(",", '\n')
    reasons_form = str(reasons_clean[:len(reasons_clean)-1])
    embed = discord.Embed(title=f'Warnings of {user.name}', description='  ', colour=0xFFE933)
    embed.add_field(name=f"Warnings count: {warns}, reasons:", value=f"{reasons_form}", inline=False)
    await ctx.response.send_message(embed=embed, ephemeral=True)

@warns.error
async def warns_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
