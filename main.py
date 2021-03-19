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
clienttoken = "YOUR_TOKEN_HERE"
spam = "THE_MESSAGE_YOU_WANT_TO_SPAM"

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
    await message.channel.send("Spam code made by: Bana#3175")
    await message.channel.send("https://github.com/Bana-code/DiscordSpamBot")
    await message.channel.send("Successfully Started")
    while 3 > 2:
      await message.channel.send(spam)
      await message.channel.send(spam)
      await message.channel.send(spam)

client.run(clienttoken)
