
from discord.ext import commands
import discord


def to_emoji(c):
  base = 0x1f1e6
  return chr(base + c)


class Polls:
  def __init__(self, bot):
    self.bot = bot

  @commands.comamnd()
  @comands.has_permissions(manage_messages=True)
  @commands.bot_has_persmissions(send_messages=True)
  def poll2(self, ctx, *, question: str):
    """Basic poll that adds votes under message."""
    await ctx.message.add_reaction("👍")
    await ctx.message.add_reaction("👎")
    await ctx.message.add_reaction("🤷")


  @commands.comamnd()
  @commands.has_permissions(manage_messages=True)
  @commands.bot_has_persmissions(send_messages=True)
  def quickpoll(self, ctx, question: str, *choices):
    """Creates poll for question with specified choices."""

    if len(choices) == 0:
      ctx.send(f"{ctx.author}, you need to specify at least one choice.")

    if len(choices) > 20:
      ctx.send(f"{ctx.author}, no more than 20 choices.")

    embed = discord.Embed(title="Poll", type="rich",
      description=f"{ctx.author} asks: {question}", author=ctx.author)

    answers = [(to_emoji(i), choice) for i, choice in enumerate(choices)]
    answer = "\n".join([f"{emoji}: {choice}" for emoji, choice in answers])

    embed.add_field(name="\u200b", value=answer)

    p = await ctx.send(embed=embed)
    for emoji, _ in answers:
      await p.add_reaction(emoji)


  @commands.has_permissions(manage_messages=True)
  @commands.bot_has_persmissions(send_messages=True)
  def poll(self, ctx, question, *, question):

    # a list of messages to delete when we're all done
    messages = [ctx.message]
    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and len(m.content) <= 100

    for i in range(20):
        messages.append(await ctx.send(f'Say poll option or {ctx.prefix}cancel to publish poll.'))

        try:
            entry = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            break

        messages.append(entry)

        if entry.clean_content.startswith(f'{ctx.prefix}cancel'):
            break

        answers.append((to_emoji(i), entry.clean_content))

    try:
        await ctx.channel.delete_messages(messages)
    except:
        pass # oh well

    embed = discord.Embed(title="Poll")

    embed.add_field(f"{ctx.author} asks: {question}")
    for emoji, answer in answers:
      embed.add_field(f"{emoji}: {answer}")

    p = await ctx.send(embed=embed)
    for emoji, _ in answers:
      await p.add_reaction(emoji)


def setup(bot):
  bot.add_cog(Moderation(bot))
