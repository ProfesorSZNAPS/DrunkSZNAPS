import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowales sie jako {bot.user}')

@bot.command()
async def mem(ctx):
    with open('images\mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    with open('images\mem2.jpg', 'rb') as h:
        picture = discord.File(h)
    with open('images\mem3.jpg', 'rb') as g:
        picture = discord.File(g)
    o=random.randint(1,3)
    if o==1:
        picture = discord.File(f)
    elif o==2:
        picture = discord.File(h)
    elif o==3:
        picture = discord.File(g)
    await ctx.send(file=picture)

bot.run("TOKEN")
