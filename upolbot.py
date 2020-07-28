from discord.ext import commands
from discord.utils import get
from config import Config
from messages import Messages

bot = commands.Bot(command_prefix=Config.prefix)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the following guild:')
    for guild in bot.guilds:
        print(f"{guild.name} with members_count: {guild.member_count} and" +
              f" owner: {str(guild.owner)}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(Config.welcome_channel)
    role = get(member.guild.roles, name=Config.student_role)
    await channel.send(Messages.welcome_message.format(member.mention))
    await member.add_roles(role)


print('Loaded cogs: ', end='')
for cog in Config.cogs:
    bot.load_extension(f'cogs.{cog}')
    print(f'{cog} ', end='')
print('')

bot.run(Config.token)
