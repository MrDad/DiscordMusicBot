import discord
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient
import sys, traceback
import configloader as cfload
from logger import Logger as log

log.info('Reading config data...')
cfload.read('../config.ini')

#######################    Begin Loading Process   ################################
startup_extensions = cfload.configSectionMap('Startup')['startup_extensions'].split()
command_prefix = cfload.configSectionMap('Commands')['command_prefix']

bot = commands.Bot(command_prefix = commands.when_mentioned_or(command_prefix), description = cfload.configSectionMap('Startup')['description'])

#Load extensions
if __name__ == "__main__":
    log.info("\nLoading extensions...")
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            log.info(f"Extension \'{extension}\' loaded.")
        except Exception as e:
            log.critical(f'Failed to load {extension} extension.')
            log.critical(e)

@bot.event
async def on_ready():
    log.info("\nConnected to Discord as", bot.user.name, "- ID ", bot.user.id)
    log.info("U4Management loaded successfully.\n______________________________\n")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user and message.content.startswith(command_prefix):
        return
    # Magically checks for any of the greetings in message and waves
    if not set(message.content.upper().split(' ')).isdisjoint(("HELLO", "HI", "HEY", "GREETINGS", "SALUTATIONS", "YO")):
        await message.add_reaction("\U0001F44B") #waving hand

###################################################################################
bot.run(cfload.configSectionMap("Startup")["token"])
