from modules.api import *

import asyncio

import discord
from config import config
from discord.ext import commands
from musicbot import linkutils, utils


class Music(commands.Cog):
    """ A collection of the commands related to music playback.

        Attributes:
            bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def _play_song(self, ctx, *, track: str):
        print(f"[DingoLingo] Использование команды: {prefix}play пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]

        if (await utils.is_connected(ctx) == None):
            if await audiocontroller.uconnect(ctx) == False:
                return

        if track.isspace() or not track:
            return

        if await utils.play_check(ctx) == False:
            return

        # reset timer
        audiocontroller.timer.cancel()
        audiocontroller.timer = utils.Timer(audiocontroller.timeout_handler)

        if audiocontroller.playlist.loop == True:
            await ctx.send("Повтор включён! Используйте {}loop чтобы выключить".format(config.BOT_PREFIX))
            return

        song = await audiocontroller.process_song(track)

        if song is None:
            await ctx.send(config.SONGINFO_ERROR)
            return

        if song.origin == linkutils.Origins.Default:

            if audiocontroller.current_song != None and len(audiocontroller.playlist.playque) == 0:
                await ctx.send(embed=song.info.format_output(config.SONGINFO_NOW_PLAYING))
            else:
                await ctx.send(embed=song.info.format_output(config.SONGINFO_QUEUE_ADDED))

        elif song.origin == linkutils.Origins.Playlist:
            await ctx.send(config.SONGINFO_PLAYLIST_QUEUED)

    @commands.command(name='loop')
    async def _loop(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}loop пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]

        if await utils.play_check(ctx) == False:
            return

        if len(audiocontroller.playlist.playque) < 1 and current_guild.voice_client.is_playing() == False:
            await ctx.send("В очереди нет треков!")
            return

        if audiocontroller.playlist.loop == False:
            audiocontroller.playlist.loop = True
            await ctx.send("Повтор включён :arrows_counterclockwise:")
        else:
            audiocontroller.playlist.loop = False
            await ctx.send("Повтор выключен :x:")

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}shuffle пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]

        if await utils.play_check(ctx) == False:
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        if current_guild.voice_client is None or not current_guild.voice_client.is_playing():
            await ctx.send("Очередь пуста :x:")
            return

        audiocontroller.playlist.shuffle()
        await ctx.send("Очередь перемешана :twisted_rightwards_arrows:")

        for song in list(audiocontroller.playlist.playque)[:config.MAX_SONG_PRELOAD]:
            asyncio.ensure_future(audiocontroller.preload(song))

    @commands.command(name='pause')
    async def _pause(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}pause пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        if current_guild.voice_client is None or not current_guild.voice_client.is_playing():
            return
        current_guild.voice_client.pause()
        await ctx.send("Воспроизведение приостановлено :pause_button:")

    @commands.command(name='queue')
    async def _queue(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}queue пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        if current_guild.voice_client is None or not current_guild.voice_client.is_playing():
            await ctx.send("Очередь пуста :x:")
            return

        playlist = utils.guild_to_audiocontroller[current_guild].playlist

        # Embeds are limited to 25 fields
        if config.MAX_SONG_PRELOAD > 25:
            config.MAX_SONG_PRELOAD = 25

        embed = discord.Embed(title=":scroll: Очередь [{}]".format(
            len(playlist.playque)), color=config.EMBED_COLOR, inline=False)

        for counter, song in enumerate(list(playlist.playque)[:config.MAX_SONG_PRELOAD], start=1):
            if song.info.title is None:
                embed.add_field(name="{}.".format(str(counter)), value="[{}]({})".format(
                    song.info.webpage_url, song.info.webpage_url), inline=False)
            else:
                embed.add_field(name="{}.".format(str(counter)), value="[{}]({})".format(
                    song.info.title, song.info.webpage_url), inline=False)

        await ctx.send(embed=embed)

    @commands.command(name='stop')
    async def _stop(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}stop пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        audiocontroller.playlist.loop = False
        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await ctx.send("Все треки остановлены :octagonal_sign:")

    @commands.command(name='move')
    async def _move(self, ctx, *args):
        print(f"[DingoLingo] Использование команды: {prefix}move пользователем", ctx.author.name, "с id:",ctx.author.id)
        if len(args) != 2:
            ctx.send("Неверное число аргументов")
            return

        try:
            oldindex, newindex = map(int, args)
        except ValueError:
            ctx.send("Неверный аргумент")
            return

        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        if current_guild.voice_client is None or (
                not current_guild.voice_client.is_paused() and not current_guild.voice_client.is_playing()):
            await ctx.send("Очередь пуста :x:")
            return
        try:
            audiocontroller.playlist.move(oldindex - 1, newindex - 1)
        except IndexError:
            await ctx.send("Неверная позиция")
            return
        await ctx.send("Перемещён")

    @commands.command(name='skip')
    async def _skip(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}skip пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        audiocontroller.playlist.loop = False

        audiocontroller.timer.cancel()
        audiocontroller.timer = utils.Timer(audiocontroller.timeout_handler)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        if current_guild.voice_client is None or (
                not current_guild.voice_client.is_paused() and not current_guild.voice_client.is_playing()):
            await ctx.send("Очередь пуста :x:")
            return
        current_guild.voice_client.stop()
        await ctx.send("Трек пропущен :fast_forward:")

    @commands.command(name='clear')
    async def _clear(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}clear пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        audiocontroller.clear_queue()
        current_guild.voice_client.stop()
        audiocontroller.playlist.loop = False
        await ctx.send("Очередь очищена :no_entry_sign:")

    @commands.command(name='prev')
    async def _prev(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}prev пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        audiocontroller.playlist.loop = False

        audiocontroller.timer.cancel()
        audiocontroller.timer = utils.Timer(audiocontroller.timeout_handler)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].prev_song()
        await ctx.send("Запущен прошлый трек :track_previous:")

    @commands.command(name='resume')
    async def _resume(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}resume пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        current_guild.voice_client.resume()
        await ctx.send("Воспроизведение возобновлено :arrow_forward:")

    @commands.command(name='songinfo')
    async def _songinfo(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}songinfo пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        song = utils.guild_to_audiocontroller[current_guild].current_song
        if song is None:
            return
        await ctx.send(embed=song.info.format_output(config.SONGINFO_SONGINFO))

    @commands.command(name='history')
    async def _history(self, ctx):
        print(f"[DingoLingo] Использование команды: {prefix}history пользователем", ctx.author.name, "с id:",ctx.author.id)
        current_guild = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await ctx.send(utils.guild_to_audiocontroller[current_guild].track_history())

    @commands.command(name='volume')
    async def _volume(self, ctx, *args):
        print(f"[DingoLingo] Использование команды: {prefix}volume пользователем", ctx.author.name, "с id:",ctx.author.id)
        if ctx.guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return

        if await utils.play_check(ctx) == False:
            return

        if len(args) == 0:
            await ctx.send("Текущая громкость: {}% :speaker:".format(utils.guild_to_audiocontroller[ctx.guild]._volume))
            return

        try:
            volume = args[0]
            volume = int(volume)
            if volume > 100 or volume < 0:
                raise Exception('')
            current_guild = utils.get_guild(self.bot, ctx.message)

            if utils.guild_to_audiocontroller[current_guild]._volume >= volume:
                await ctx.send('Громкость установлена на {}% :sound:'.format(str(volume)))
            else:
                await ctx.send('Громкость установлена на {}% :loud_sound:'.format(str(volume)))
            utils.guild_to_audiocontroller[current_guild].volume = volume
        except:
            await ctx.send("Ошибка: Громкость должна быть в диапазоне 1-100%")


def setup(bot):
    bot.add_cog(Music(bot))
