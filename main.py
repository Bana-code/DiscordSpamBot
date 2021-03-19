# created by Bana#3175, Bana-code
#
# WARNING:
#
# After you call s.start he will spam forever
# Bot sends 3 messages, inorder to prevent the bot from crashing but it's good tho ;)
#
# HOW TO STOP?
# Inorder to stop the bot, stop the code from running

# imports don't touch
import discord
from discord.ext import commands

# put your credentials here.
clienttoken = "UID/63ioe#IVUnfvti.6EyAb77NAOPAy9Noi"
spam = "GET SPAMMED LOL"

# Bot prefix don't touch.
client = commands.Bot(command_prefix = "s.")

# Code Don't Touch Ever and EVER.
@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.idle, activity=discord.Game('Created by: Bana#3175'))
  print("Bot Online")

@client.event
async def on_message(message):
  if message.content == "s.start":
    while 3 > 2:
      await message.channel.send(spam)
      await message.channel.send(spam)
      await message.channel.send(spam)

client.run(clienttoken)