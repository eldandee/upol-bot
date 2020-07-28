from discord.ext import commands
from config import Config
import requests
from discord import Embed


class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pocasi'])
    async def weather(self, ctx, *args):
        city = Config.default_city if len(
            args) == 0 else " ".join(map(str, args))

        url = Config.openweather_api_url.format(city, Config.weather_token)
        res = requests.get(url).json()

        if str(res["cod"]) == "200":
            description = "Aktuální počasí v městě " + \
                res["name"] + ", " + res["sys"]["country"]
            embed = Embed(title="Počasí", description=description)
            image = "http://openweathermap.org/img/w/" + \
                res["weather"][0]["icon"] + ".png"
            embed.set_thumbnail(url=image)
            weather = res["weather"][0]["main"] + \
                " (" + res["weather"][0]["description"] + ") "
            temp = str(res["main"]["temp"]) + "°C"
            feels_temp = str(res["main"]["feels_like"]) + "°C"
            humidity = str(res["main"]["humidity"]) + "%"
            wind = str(res["wind"]["speed"]) + "m/s"
            clouds = str(res["clouds"]["all"]) + "%"
            visibility = str(res["visibility"] / 1000) + \
                " km" if "visibility" in res else "bez dat"
            embed.add_field(name="Počasí", value=weather, inline=False)
            embed.add_field(name="Teplota", value=temp, inline=True)
            embed.add_field(name="Pocitová teplota",
                            value=feels_temp, inline=True)
            embed.add_field(name="Vlhkost", value=humidity, inline=True)
            embed.add_field(name="Vítr", value=wind, inline=True)
            embed.add_field(name="Oblačnost", value=clouds, inline=True)
            embed.add_field(name="Viditelnost", value=visibility, inline=True)
            await ctx.send(embed=embed)
        elif str(res["cod"]) == "404":
            await ctx.send("Město nebylo nenalezeno.")
        elif str(res["cod"]) == "401":
            await ctx.send(
                'Nelze se připojit k API openweather. Kontaktuj tu pepegu.')
        else:
            await ctx.send("Něco se pokazilo (" + res["message"] + ")")


def setup(bot):
    bot.add_cog(WeatherCog(bot))
