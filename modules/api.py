import discord, random, datetime, time, os, gettext
from time import sleep as tsleep
from discord.ext import commands
from discord.ext.commands import has_permissions

from config_eybie import settings, version_info

eybie_ver = version_info['version']
eybie_codename = version_info['codename']
eybie_reldate = version_info['rel_date']
prefix = settings['prefix']
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = prefix, intents=intents)

global startTime
startTime = time.time()