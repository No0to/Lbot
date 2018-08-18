import random
import requests
from colorama import *
from datetime import timedelta
from discord.ext.commands import Bot
from discord import Game
import discord
from discord import *

init(convert=True)

print(Fore.GREEN + 'botbot v1.0')
print(Style.RESET_ALL + '__________')

filename = "token.txt"

with open(filename) as f:
    content = f.readlines()

for line in content:

    TOKEN = line

BOT_PREFIX = ("$$")

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball', description="Answers a yes or no question.", breif="Answers from a $10 ball", pass_context=True)
async def eight_ball(context):
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

    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    print("$$8ball")

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number + " squared is " + str(squared_value)))
    print("$$square")

@client.command()
async def cube(number):
    cubed_value = int(number) * int(number)
    await client.say(str(number + " cubed is " + str(cubed_value)))
    print("$$cube")

@client.command()
async def deadass():
    await client.say("https://imgur.com/a/I0Ktdkc")
    print("$$deadass")

@client.command()
async def bitcoin():
    discord_webhook_url = 'https://discordapp.com/api/webhooks/<webhookid>/<tokenid>'
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate']
    await client.say("The bitcoin price is $" + price_in_usd)
    print("$$bitcoin")


@client.command()
async def double(number):
    doubled = int(number) * 2
    await client.say(str(number + " doubled is " + str(doubled)))
    print("$$double")

@client.command()
async def triple(number):
    tripled = int(number) * 3
    await client.say(str(number + " tripled is " + str(tripled)))
    print("$$triple")

@client.command()
async def echo(*, words):
    await client.say(words)
    print("$$echo")

@client.command(pass_context=True)
async def getgay(ctx):
    test = ctx.message.author.mention
    testt = discord.Member
    await client.say( str(test) + " Has just came out as gay!")
    await client.change_nickname(ctx.message.author, ctx.message.author.display_name + '‍🌈')
    print("$$getgay")

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")
    print("$$ping")

@client.command(pass_context=True)
async def about(ctx):
    await client.say("ABOUT```\nMade by thog#6636\n```")
    print("$$about")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='$$help'))
    print("Logged in as " + client.user.name)


client.run(TOKEN)
