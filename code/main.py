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
from time import sleep

# put your credentials here.
clienttoken = "BOT_TOKEN_HERE"
spam = "YOUR_MESSAGE_HERE"

# Bot prefix don't touch.
client = commands.Bot(command_prefix = "s.")

# Code Don't Touch Ever and EVER.
@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.idle, activity=discord.Game('Created by: Bana#3175'))
  print("Bot Online")
      
@client.event
async def on_message(message):
    if message.content.startswith('s.start'):
      await message.channel.send("Spam bot code made by: Bana#3175")
      await message.channel.send("||https://github.com/Bana-code/DiscordSpamBot||")
      await message.channel.send("Do you want to start? y | n")

      def check(m):
        return m.content == 'y' and m.channel == message.channel

      msg = await client.wait_for('message', check=check)
      await message.channel.send("Starting")
      sleep(1)
      await message.channel.send("Started")
      for y in range(70):
        await message.channel.send(spam.format(msg))
        await message.channel.send(spam.format(msg))
        await message.channel.send(spam.format(msg))
        await message.channel.send(spam.format(msg))
        await message.channel.send(spam.format(msg))
        await message.channel.send(spam.format(msg))
        await message.channel.send(spam.format(msg))
client.run(clienttoken)
