
from discord.ext import commands
import discord


class Moderation:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.bot_has_permissions(kick_members=True)
  def kick(ctx, user: discord.User, *, reason="None provided"):
    """Kicks the user mentioned.
    
    Args:
      user (discord.User): user to be kicked.
      reason (str): Multi whitespace string which contains reason why the user was kicked.

    Returns:
      None
      
    """
    await ctx.guild.kick(user, reason)


  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(ban_members=True)
  def ban(ctx, user: discord.User, *, reason="None provided"):
    """Kicks the user mentioned.
    
    Args:
      user (discord.User): user to be kicked.
      reason (str): Multi whitespace string which contains reason why the user was kicked.

    Returns:
      None
      
    """
    await ctx.guild.ban(user, reason)


def setup(bot):
  bot.add_cog(Moderation(bot))
