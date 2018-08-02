
import logging
import asyncio
import sys

from discord.ext import commands
import discord

import config
import utils


description = """
  Bot for managing channels in the Kepler Collective.
"""

logging.getLogger("discord.http").setLevel(logging.WARNING)
logging.getLogger("discord").setLevel(logging.DEBUG)

logger = logging.getLogger()

level = logging.DEBUG if config.debug else logging.INFO

f_handler = logging.FileHandler(filename="juewang.log", encoding="utf-8", mode="w")
cl_handler = logging.StreamHandler()

dt_fmt = "%Y-%m-%d %H:%M:%S"
out_fmt = "[{asctime}] [{levelname:<6}] {name}: {message}"
logger_fmt = logging.Formatter(out_fmt, dt_fmt, style="{")

cl_handler.setFormatter(logger_fmt)
f_handler.setFormatter(logger_fmt)

logger.addHandler(cl_handler)
logger.addHandler(f_handler)
logger.setLevel(level)

extension = (
  "cogs."
)


class Juewang(commands.Bot):
  def __init__(self, config, command_prefix=config.prefix_callable, 
      description=description):

    super().__init__(command_prefix, description)

    self.config = config
    self.logger = logging.getLogger()

    async def on_command_error(self, ctx, err):
      if isinstance(err, commands.NoPrivateMessage):
        await ctx.author.send("That command cannot be used in DMS.")

      elif isinstance(err, comamnds.DisabledCommand):
        await ctx.author.send("Sorry that command has been disabled.")
