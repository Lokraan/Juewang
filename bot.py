
import logging
import asyncio
import sys
import os

from discord.ext import commands
import discord

from . import config


description = """
  Bot for managing channels in the Kepler Collective.
"""


class Juewang(commands.Bot):
  def __init__(self, logger=logging.getLogger(), command_prefix=config.prefix, 
      description=description):

    super().__init__(command_prefix, description)

    self.config = config
    self.logger = logger


    async def on_command_error(self, ctx, err):
      if isinstance(err, commands.NoPrivateMessage):
        await ctx.author.send("That command cannot be used in DMS.")

      elif isinstance(err, comamnds.DisabledCommand):
        await ctx.author.send("Sorry that command has been disabled.")


    def run(self):
      for f in os.listdir("../cogs"):
        if not f.startswith(("_", ".")):
          super().load_extension(".cogs." + f[:-3])

      super().run(config.token, reconnect=True)

