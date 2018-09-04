import random
import requests
from colorama import *
from datetime import timedelta
from discord.ext.commands import Bot
from discord.utils import get
import discord
from discord import *

init(convert=True)

print(Fore.GREEN + 'davenPort v1.0')
print(Style.RESET_ALL + '__________')

filename = "token.txt"

with open(filename) as f:
    content = f.readlines()

for line in content:

    TOKEN = line

BOT_PREFIX = ("$$")

client = Bot(command_prefix=BOT_PREFIX)

client.remove_command('help')

@client.command()
async def help(ctx):
    embed=discord.Embed()
    embed.set_thumbnail(url="https://i.imgur.com/piq0KOO.png")
    embed.add_field(name="$$help", value="The command you're using currently.", inline=False)
    embed.add_field(name="$$info", value="Info about the bot", inline=True)
    embed.add_field(name="$$8ball", value="Answers questions using an 8ball", inline=False)
    embed.add_field(name="$$oot", value="oot", inline=False)
    embed.add_field(name="$$joy", value="Spams :joy: 5 times", inline=False)
    embed.add_field(name="$$double", value="Doubles a number", inline=True)
    embed.add_field(name="$$triple", value="Triples a number", inline=False)
    embed.add_field(name="$$square", value="Squares a number", inline=True)
    embed.add_field(name="$$cube", value="Cubes a number", inline=False)
    embed.add_field(name="$$bitcoin", value="Shows the current price of bitcoin", inline=True)
    embed.add_field(name="$$echo", value="Repeats whatever you say after the $$echo", inline=False)
    embed.add_field(name="$$ping", value="Just sees how quick it is at the moment", inline=True)
    embed.add_field(name="$$getgay", value="You'll see", inline=False)
    embed.set_footer(text="Note: $$getgay doesn't work with the owner of the guild. $$whydoesntitwork for more info.")
    await ctx.send(embed=embed)
    print("$$help")

@client.command()
async def info(ctx):
    embed=discord.Embed(title="davenPort Info", color=0xaaf9ff)
    embed.set_thumbnail(url="https://i.imgur.com/piq0KOO.png")
    embed.add_field(name="Made By Thou", value="thog #6636, @Th0u__", inline=True)
    embed.add_field(name="Invite", value="[Invite me to your guild!](https://discordapp.com/oauth2/authorize?&client_id=449815952293625857&scope=bot&permissions=8)", inline=True)
    embed.add_field(name="guild Count", value=len(client.guilds), inline=True)
    await ctx.send(embed=embed)
    print("$$info")

@client.command(name='8ball')
async def eightball(ctx):
    possible_responses = [

    "It is certain",
    "Is it decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "You can count on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Absolutely",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "Chances aren't good",
    "Possibly.",
    "I suppose it's decided.",
    "For sure.",
    "Yeah, definitely.",
    "Lol I guess.",
    "You can count on it..",
    "My spidey senses are telling me yes. (Mr Stark I don't fe-)",
    "Eh maybe.",
    "Microsoft says Outlook is good.",
    "yes",
    "Signs point to Yesville. Oh, it's a warzone.",
    "Signs point to Nopeville. Hell to the no.",
    "Signs poi... Oh. ***Oh no.***",
    "As if.",
    "Absolutely.",
    "What type of question is that? How- Nvm just try again later",
    "Come again?",
    "I know this one. Buuut I guess I'll just be an ass and not tell you now.",
    "Wait what?",
    "OK HOLD ON WHAT",
    "Don't even try.",
    "**No.**",
    "Never.",
    "Google says Outlook is a big NOPE.",
    "Jesus Christ dude, that's never going to happen and you know it.",
    "Your chances are as good as trying to convince me to do ten pushups. DON'T. YOU. DARE.",
    "You're- you're kidding. Of course not.",
    "God forbid.",
    "Hell no.",
    "Why?",
    "Heh, heh. ***funny jok-***",
    "Nahh",
    "...Don't *ever* ask this question anymore",
    "Hey, VSauce Michael here. It could, but maybe it won't.",
    "Hey, VSauce Michael here. When is, when you aren't?"
    
    ]
    await ctx.send( ctx.message.author.mention + " " + random.choice(possible_responses))
    print("$$8ball")
    
@client.command()
async def oot(ctx):
    possible_responses = [

    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "y",
    "z"

    ]
    await ctx.send(random.choice(possible_responses) + "oot")
    print("$$oot")
    
@client.command()
async def joy(ctx):
    await ctx.send(":joy:")
    await ctx.send(":joy:")
    await ctx.send(":joy:")
    await ctx.send(":joy:")
    await ctx.send(":joy:")
    print("$$joy")
    
@client.command()
async def double(ctx, number):
    doubled = int(number) * 2
    await ctx.send(str(number + " doubled is " + str(doubled)))
    print("$$double")
    
@client.command()
async def triple(ctx, number):
    tripled = int(number) * 3
    await ctx.send(str(number + " tripled is " + str(tripled)))
    print("$$triple")
    
@client.command()
async def square(ctx, number):
    squared_value = int(number) * int(number)
    await ctx.send(str(number + " squared is " + str(squared_value)))
    print("$$square")
    
@client.command()
async def cube(ctx, number):
    cubed_value = int(number) * int(number)
    await ctx.send(str(number + " cubed is " + str(cubed_value)))
    print("$$cube")
    
@client.command()
async def bitcoin(ctx):
    discord_webhook_url = 'https://discordapp.com/api/webhooks/<webhookid>/<tokenid>'
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate']
    await ctx.send("The bitcoin price is $" + price_in_usd)
    print("$$bitcoin")
    
@client.command()
async def echo(ctx, *, words):
    await ctx.send(words)
    print("$$echo")
    
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")
    print("$$ping")
    
@client.command()
async def getgay(ctx): #ctx.message.author
    test = ctx.message.author.mention
    testt = discord.Member
    await ctx.send(str(test) + " Has just came out as gay!")
    await ctx.author.edit(nick=f'{ctx.author.display_name} 🌈')
    print("$$getgay")

@client.command()
async def deadass(ctx):
    file = discord.File("god.png", filename="god.png")
    await ctx.send(file=file)

@client.command()
async def whydoesntitwork(ctx):
    await ctx.send("The reason why $$getgay doesn't work with the guild owner is because of the Discord API's (really) dumb idea of hierarchy.")
    print("$$whydoesntitwork")

@client.command()
async def about(ctx):
    await ctx.send("ABOUT```\nMade by thog#6636\n```")
    print("$$about")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name='$$help'))
    print("Logged in as " + client.user.name)


client.run(TOKEN)
