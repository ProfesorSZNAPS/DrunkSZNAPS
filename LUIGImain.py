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
async def say(ctx):
    with open('memesfromtesla\elektryki.jpg', 'rb') as f:
        picture = discord.File(f)
    with open('memesfromtesla\null.jpg', 'rb') as h:
        picture = discord.File(h)
    with open('memesfromtesla\ogien.jpg', 'rb') as g:
        picture = discord.File(g)
    with open('memesfromtesla\teslawogniu.jpg', 'rb') as k:
        picture = discord.File(k)
    o=random.randint(1,4)
    if o==1:
        picture = discord.File(f)
    elif o==2:
        picture = discord.File(h)
    elif o==3:
        picture = discord.File(g)
    elif o==4:
        picture = discord.File(k)
    await ctx.send(file=picture)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$pomoc'):
        y=random.randint(1,2)
        if y==1:
            y="Aby zacząć dbać o środowisko, warto skupić się na prostych, codziennych nawykach, które razem mogą przynieść dużą zmianę.\nKluczowe działania to:\nsegregacja śmieci, oszczędzanie energii i wody, ograniczenie zużycia plastiku,\npromowanie transportu publicznego lub roweru oraz wspieranie lokalnych inicjatyw ekologicznych.\nPomocna będzie tez ta aplikacja pobierz ja z tego linku\n------>https://play.google.com/store/apps/details/AfvalWijzer?id=nl.addcomm.afvalwijzer&hl=pl&pli=1"
        elif y==2:
            y="o\nd"
        
        await message.channel.send(y)



bot.run("TOKEN")
