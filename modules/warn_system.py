from modules.api import *
import sqlite3

print("[INFO] Успешно загружен warn_system")

#Система варнов на sqlite3. Да, у меня нет личной жизни.
@bot.command()
@has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, reason: str):
    serverid = ctx.message.guild.id
    print(f"[DingoLingo] Использование команды: {prefix}warn пользователем", ctx.author.name, "с id:",ctx.author.id)
    if not os.path.isdir(f"database/servers/{serverid}"):
        os.mkdir(f'database/servers/{serverid}')
    sqlite_conn = sqlite3.connect(f'database/servers/{serverid}/warnings.db')
    cursor = sqlite_conn.cursor()
    userid = "id" + str(member.id)
    now = datetime.datetime.now()
    reason_full = "[" + str(now.day) + "-"+ str(now.month)+ "-" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "] " + reason
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {userid}(reason TEXT);")
    cursor.execute(f"INSERT INTO {userid} (reason) VALUES('{reason_full}');")
    sqlite_conn.commit()
    warns = len(cursor.execute(f"SELECT * FROM {userid}").fetchall())
    if warns >= 3:
        embed = discord.Embed(title=f'Пользователю {member.name} добавлено предупреждение.', description=f'Причина варна: {reason}', colour=0xFFE933)
        embed2 = discord.Embed(title="Пользователю был ограничен доступ к текстовому и голосовому чату на 7 дней за нарушения правил.", description='', colour=0xFFE933)
        await ctx.send(embed=embed)
        await member.timeout_for(datetime.timedelta(minutes=10080))
        await ctx.send(embed=embed2)
        cursor.execute(f"DROP TABLE {userid}")
        sqlite_conn.commit()
        await ctx.respond(f"Member timed out for 15 minutes.")
    else:
        embed = discord.Embed(title=f'Пользователю {member.name} добавлено предупреждение.', description=f'Причина варна: {reason}', colour=0xFFE933) 
        await ctx.send(embed=embed)
    sqlite_conn.close()

@bot.command()
@has_permissions(administrator=True)
async def warns(ctx, user:discord.User):
    serverid = ctx.message.guild.id
    sqlite_conn = sqlite3.connect(f'database/servers/{serverid}/warnings.db')
    cursor = sqlite_conn.cursor()
    userid = "id" + str(user.id)
    warns = len(cursor.execute(f"SELECT * FROM {userid}").fetchall())
    warns_reasons = cursor.execute(f"SELECT * FROM {userid}").fetchall()
    rml = str(warns_reasons).replace("[(\'", '').replace("(\'", '').replace("\',)", '').replace(",", '\n')
    reasons_form = str(rml[:len(rml)-1])
    embed = discord.Embed(title=f'Варны пользователя {user.name}', description='  ', colour=0xFFE933)
    embed.add_field(name=f"Количество варнов: {warns}, причины варнов:", value=f"{reasons_form}", inline=False)
    await ctx.send(embed=embed)
    print(f"[DingoLingo] Использование команды: {prefix}warns пользователем", ctx.author.name, "с id:",ctx.author.id)