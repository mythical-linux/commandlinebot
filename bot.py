from discord import Message
from array import array
import discord
from discord import User
import subprocess
from discord.ext.commands import Bot
from discord.ext import commands
Client = discord.Client()
client = discord.Client()
bot = commands.Bot(command_prefix='$')
import os
import os.path
import re
import json

# # # Config part # # #

# find XDG config directory from environment variable. otherwise, return current user's home directory plus /.config
config_home_incomplete = os.environ.get('XDG_CONFIG_HOME', os.environ['HOME'] + '/.config')

# take the userconfigdir variable and attatch /programname/ to it to get the dir that programname should create
config_home_complete = config_home_incomplete + '/commandlinebot/'

# make program's config directory. if it already exists, don't panic. or exception.
try:
    os.mkdir(config_home_complete)
except FileExistsError:
    print('Config folder already exists at ' + config_home_complete + '.')
else:
    print('Config folder created at ' + config_home_complete + '.')

pathcheck = os.path.exists(config_home_complete + 'config.json')
if pathcheck:
    with open(config_home_complete + 'config.json') as json_data_file:
         data = json.load(json_data_file)
else:
    print('Uh oh! Command Line could not start because you\'re missing a config file! Create ' + config_home_complete + 'config.json and fill it with this data:\n{\n   "token": "<bot account\'s token>"\n}')
    exit()
    
# # # Config part # # #


@bot.command()
async def sh(ctx, *args):
  list(args)
  separator = ' '
  output = separator.join(args)
  print(output)
  clineargssplit = output.split()
  print(clineargssplit)
  result = subprocess.run(clineargssplit, stdout=subprocess.PIPE).stdout.decode('utf-8')
  print(ctx.author.id)
  if ctx.author.id == "208129127494975488":
    await print('is it a problem with ctx.send or a problem with my function')
    ctx.send("ok gentoo user")
    return
  await ctx.send('```\n' + result + '\n```')

@bot.command()
async def fortune(ctx, *args):
  fortune = subprocess.run(['fortune', 'mythical_linux', 'off/mythical_linux'], stdout=subprocess.PIPE).stdout.decode('utf-8')
  await ctx.send("```\n" + fortune + "\n```")
  
@bot.command()
async def fortune_license(ctx, *args):
          await ctx.send(fortunelicense)

fortunelicense = ('MIT License\n\nCopyright (c) 2020 ncdulo\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\n use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.')
  
@bot.command()
async def py(ctx, *args):
    print(args)
    pyseperator = ' '
    pyseperated = pyseperator.join(args)
    print(pyseperated)
    result = eval(pyseperated) 
    await ctx.send('```py\n' + result + '\n```')
  
      
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
      
bot.run(data["token"])
