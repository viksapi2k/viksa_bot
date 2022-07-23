from modules.api import *

import discord, time
from config import config
from discord.ext import commands
from discord.ext.commands import has_permissions
from musicbot import utils
from musicbot.audiocontroller import AudioController
from musicbot.utils import guild_to_audiocontroller, guild_to_settings


class General(commands.Cog):
    """ A collection of the commands for moving the bot around in you server.

            Attributes:
                bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot

    # logic is split to uconnect() for wide usage

    @commands.command(name='connect')
    async def _connect(self, ctx):  # dest_channel_name: str
        print(f"[DingoLingo] Использование команды: {prefix}connect пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        await audiocontroller.uconnect(ctx)

    @commands.command(name='disconnect')
    async def _disconnect(self, ctx, guild=False):
        print(f"[DingoLingo] Использование команды: {prefix}disconnect пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        await audiocontroller.udisconnect()

    @commands.command(name='reset')
    async def _reset(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}reset пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} Подключён к {}".format(":white_check_mark:", ctx.author.voice.channel.name))

    @commands.command(name='changechannel')
    async def _change_channel(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}changechannel пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        vchannel = await utils.is_connected(ctx)
        if vchannel == ctx.author.voice.channel:
            await ctx.send("{} Уже подключён к {}".format(":white_check_mark:", vchannel.name))
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} Сменён на {}".format(":white_check_mark:", ctx.author.voice.channel.name))

    @commands.command(name='ping')
    async def _ping(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}ping пользователем", ctx.author.name, "с id:",ctx.author.id)
        await ctx.send("Понг!")

    #Сделал в виде @bot.event во избежание конфликтов с командой ;help в modules.ey_commands
    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        if message.content == f"{prefix}help":
            embed = discord.Embed(title="Помощь DingoLingo", description="", colour=0xFFE933)
            embed.add_field(name="Основные", value=f"{prefix}play - Воспроизвести трек.\n{prefix}connect - {config.HELP_CONNECT_SHORT}\n{prefix}disconnect - {config.HELP_DISCONNECT_SHORT}\n{prefix}history - {config.HELP_HISTORY_LONG}\n{prefix}pause - {config.HELP_PAUSE_SHORT}\n{prefix}volume - {config.HELP_VOL_SHORT}\n{prefix}prev - {config.HELP_PREV_SHORT}\n{prefix}resume - {config.HELP_RESUME_SHORT}\n{prefix}skip - {config.HELP_SKIP_SHORT}\n{prefix}songinfo - {config.HELP_SONGINFO_SHORT}\n{prefix}stop - {config.HELP_STOP_SHORT}\n{prefix}ping - {config.HELP_PING_SHORT}\n{prefix}clear - {config.HELP_CLEAR_SHORT}\n{prefix}loop - {config.HELP_LOOP_SHORT}\n{prefix}queue - {config.HELP_QUEUE_SHORT}\n{prefix}shuffle - {config.HELP_SHUFFLE_SHORT}", inline=False)
            await message.channel.send(embed=embed)
            print(f"[DingoLingo] Перехват команды {prefix}help")

    @commands.command(name='setting')
    @has_permissions(administrator=True)
    async def _settings(self, ctx, *args):
        print(f"[DingoLingo] Использование команды: {prefix}setting пользователем", ctx.author.name, "с id:",ctx.author.id)

        sett = guild_to_settings[ctx.guild]

        if len(args) == 0:
            await ctx.send(embed=await sett.format())
            return

        args_list = list(args)
        args_list.remove(args[0])

        response = await sett.write(args[0], " ".join(args_list), ctx)

        if response is None:
            await ctx.send("`Ошибка: настройка не найдена`")
        elif response is True:
            await ctx.send("Настройки обновлены!")

    #@commands.command(name='addbot')
    #async def _addbot(self, ctx):
    #    embed = discord.Embed(title="Добавить бота на свой сервер", description=config.ADD_MESSAGE +
    #                          "(https://discordapp.com/oauth2/authorize?client_id={}&scope=bot>)".format(self.bot.user.id))
    #
    #    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))
