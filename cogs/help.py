from discord.ext import commands
from messages import Messages


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(Messages.help)


def setup(bot):
    bot.add_cog(HelpCog(bot))
