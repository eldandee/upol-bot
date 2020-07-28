from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)


def setup(bot):
    bot.add_cog(AdminCog(bot))
