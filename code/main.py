# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Made by: Bana#3175, Bana-code on github

# imports don't touch
import discord
from discord.ext import commands
from time import sleep

# put your credentials here.
clienttoken = "BOT_TOKEN_HERE"
spam = "YOUR_MESSAGE_HERE"

# Bot prefix don't touch.
client = commands.Bot(command_prefix = "s.")

# If you don't know how this works, I suggest you to not touch it.
@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.do_not_disturb, activity=discord.Game('Created by: Bana#3175'))
  print("Bot Online")
      
@client.event
async def on_message(message):
    if message.content.lower() == "s.start":
      await message.channel.send("Spam bot code made by: Bana#3175")
      await message.channel.send("||https://github.com/Bana-code/DiscordSpamBot||")
      await message.channel.send("Do you want to start? Press y to continue (lowercase only)")

      def check(m):
        return m.content.lower() == 'y' and m.channel == message.channel

      msg = await client.wait_for('message', check=check)
      await message.channel.send("Starting")
      sleep(1)
      await message.channel.send("Started")
      for y in range(70):   
        await message.channel.send(spam.format(msg))
        sleep(0.8)

client.run(clienttoken, bot=True, reconnect=True)
