import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command(name='bot')
async def help(ctx):
    await ctx.send('если вы напишите - ($hello) - с вами поздаровуется мой бот аналогично работает ($bye), если вы напишите ($flip_coin) бот подкинет монетку, ($smile) сгенерирует смайлик из 10 записаных в код, напишите ($pass) и бот сгенерирует 10 значный пароль, команда ($heh <число>) тогда бот напишет he столько раз сколько указали')



bot.run("")