from discord.ext import commands
from datetime import datetime
from discord import Embed


class CalendarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tyden(self, ctx):
        year, week, day_of_week = datetime.today().isocalendar()
        if week % 2 == 0:
            cal_type = "Sudý"
        else:
            cal_type = "Lichý"
        embed = Embed(title="Týden", color=0xE5DC37)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=str(ctx.author))
        embed.add_field(name="Kalendářní",
                        value="{} ({})".format(cal_type, week))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CalendarCog(bot))
