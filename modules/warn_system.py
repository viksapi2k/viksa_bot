from modules.api import *
import sqlite3

#Создание необходимых папок
if not os.path.isdir(f"database/servers"):
    os.mkdir(f'database')
    os.mkdir(f'database/servers')

module_loaded(f"Ey_WarnSystem")

#Система варнов на sqlite3.
@bot.command(name="warn", description="Выдать предупреждение пользователю")
@has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, reason: str):
    logging.info(f"Использование команды: /warn пользователем {ctx.author.name} с id: {ctx.author.id} | Причина: \"{reason}\"") 
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
    embed = discord.Embed(title=f'Пользователю {member.name} выдано предупреждение.', description=f'Причина: {reason}', colour=0xFFE933)
    await ctx.response.send_message(embed=embed)
    if warns >= 3:
        embed2 = discord.Embed(title="Пользователю был ограничен доступ к текстовому и голосовому чату на 7 дней за нарушения правил.", description='', colour=0xFFE933)
        await member.timeout_for(datetime.timedelta(minutes=10080)) #Таймаут на 7 дней, указал в минутах потому что я так хочу :/
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

@bot.command(name="warns", description="Отобразить список предупреждений пользователя")
@has_permissions(administrator=True)
async def warns(ctx, user:discord.User):
    logging.info(f"Использование команды: /warns пользователем {ctx.author.name} с id: {ctx.author.id}")
    serverid = ctx.guild.id
    sqlite_conn = sqlite3.connect(f'database/servers/{serverid}/users.db')
    cursor = sqlite_conn.cursor()
    userid = "id" + str(user.id)
    warns_reasons = cursor.execute(f"SELECT reason FROM {userid}").fetchall()
    warns = len(warns_reasons)
    reasons_clean = str(warns_reasons).replace("[(\'", '').replace("(\'", '').replace("\',)", '').replace(",", '\n') #Добавить проверку на количество варнов
    reasons_form = str(reasons_clean[:len(reasons_clean)-1])
    embed = discord.Embed(title=f'Предупреждения пользователя {user.name}', description='  ', colour=0xFFE933)
    embed.add_field(name=f"Количество предупреждений: {warns}, причины:", value=f"{reasons_form}", inline=False)
    await ctx.response.send_message(embed=embed, ephemeral=True)

@warns.error
async def warns_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)