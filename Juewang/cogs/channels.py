
from discord.ext import commands
import discord

import utils


class Moderation:
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="createChannel")
  @commands.has_permissions(manage_channels=True)
  @commands.bot_has_permissions()
  def create_text_channel(self, ctx, chan_name, *, role: discord.Role=None):
    """Creates a new text_channel

    Args:
      chan_name (str): Name of channel to be created
      role (str): lowest role that can read channel

    Returns:
      None
    """

    overwrites = {}
    if role:
      proletariat = utils.get_proletariat_role(ctx, role)

      overwrites = {
        _: discord.PermissionOverwrite(read_messages=False)
        for _ in proletariat
      }

    await ctx.guild.create_text_channel(name, overwrites=overwrites)


  @commands.command(name="createPool")
  @commands.has_permissions(manage_channels=True, manage_roles=True)
  @commands.bot_has_permissions(manage_channels=True, manage_roles=True)
  def create_pool_channel(ctx, chan_name, *, role=None):
    """Creates a new text_channel for pooling, default memebers can't read.
    Also generates a new role for pool channel notifs.

    Args:
      chan_name (str): Name of channel and role to be created.
      role (str): Name of role to be created.

    Returns:
      None
    """

    if role:
      ctx.guild.create_role(role, mentionable=True, reason="New Pool")

    overwrites = {
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    } 

    await ctx.guild.create_text_channel(chan_name, overwrites=overwrites)


def setup(bot):
  bot.add_cog(Moderation(bot))
