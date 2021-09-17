import discord
from discord.ext import commands
import configloader as cfload
import praw, random
from logger import Logger as log
import qrcode
from io import BytesIO

cfload.read('..\\config.ini')
log.info(cfload.configSectionMap("Owner Credentials")['owner_id'], "is the owner. Only this user can use /shutdown.")

class Commands(commands.Cog):
    """Various commands"""
    prune_cutoff = 25

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! ({round(self.bot.latency, 2)} ms)')

    @commands.command()
    async def test(self, ctx, test_msg="test"):
        await ctx.send(test_msg)



def setup(bot):
    bot.add_cog(Commands(bot))
