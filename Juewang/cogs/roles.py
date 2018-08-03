
from discord.ext import commands


def not_proletariat():
  def predicate(ctx):
      return ctx.author.top_role > ctx.guild.default_role
  return commands.check(predicate)


class Roles:
  def __init__(self, bot):
    self.bot = bot


  @commands.command(name="giveme")
  @not_proletariat()
  @commands.bot_has_permissions(manage_roles=True)
  def give_role(ctx, *, role: discord.Role):
    """Gives specified role to user as long as they do not have the
    default guild role or the requested role isn't better than their current one.
    """
    if ctx.author.top_role < role:
      ctx.author.send(f"{ctx.author}, your role isn't high enough.")
      return

    ctx.author.add_roles(role, reason=f"{ctx.author} asked for it via give me")


  @commands.command(name="giveme")
  @not_proletariat()
  @commands.bot_has_permissions(manage_roles=True)
  def remove_role(ctx, *, role: discord.Role):
    """Removes the specified role from the user.
    """
    if role in ctx.author.roles:
      ctx.author.remove_role(role, reason=f"{ctx.author} asked for removal of role")


def setup(bot):
  bot.add_cog(Moderation(bot))
