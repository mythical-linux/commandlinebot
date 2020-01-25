from discord import Message
from array import array
import discord
from discord import User
import subprocess
from discord.ext.commands import Bot
from discord.ext import commands
Client = discord.Client()
client = discord.Client()
import string
import os
import os.path
import re
import json

# # # Config part # # #

# find XDG config directory from environment variable. otherwise, return current user's home directory plus /.config
config_home_incomplete = os.environ.get('XDG_CONFIG_HOME', os.environ['HOME'] + '/.config')

# take the userconfigdir variable and attatch /programname/ to it to get the dir that programname should create
config_home_complete = config_home_incomplete + '/correctorbot/'

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
            print('Uh oh! CorrectorBOT could not start because you\'re missing a config file! Create ' + config_home_complete + 'config.json and fill it with this data:\n{\n   "token\
": "<bot account\'s token>"\n}')
                exit()

                # # # Config part # # #
                



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print(message.content)

# replace twitter links with nitter links
  twmatch = re.search('https://twitter.com/*', message.content)
  if twmatch:
    twmatchstring = twmatch.string
    twreplace = re.sub('https://twitter.com/', 'https://nitter.net/', twmatchstring)
    twmatch2 = re.findall('https://nitter.net/.*', twreplace, flags=0)
    if twmatch2:
      print(twmatch2)
      twmatchstring2 = ' '.join(twmatch2)
      print(twmatchstring2)
      await message.channel.send('**Heads up!**\n\nYou just posted a link to Twitter! This is extremely bad practice.\nBelow is a link to the same tweet on Nitter.net.\n<' + twmatchstring2 + '>\nDon\'t post Twitter links or Phate will write an essay.')


                                                
# replace youtube links with invidious links
  ytmatch = re.search('https://www.youtube.com/.*', message.content)
  if ytmatch:
    ytmatchstring = ytmatch.string
    ytreplace = re.sub('https://www.youtube.com/', 'https://invidio.us/', ytmatchstring)
    ytsearch2 = re.findall
    if ytsearch2:
      ytsearchstring = ytbsearch.string
      ytsub = re.sub('https://www.youtube.com/', 'https://invidio.us/', ytsearchstring)
      ytsearchreplace = re.findall('https://invidio.us/.*', ytsub, flags=0)
      if ytsearchreplace:
        print(ytsearchreplace)
        ytsearchreplacestring = ' '.join(ytsearchreplace)
        print(ytmatchstring2)
        await message.channel.send('**Heads up!**\n\nYou just posted a link to YouTube! This is extremely bad practice.\nBelow is a link to the same video on Invidio.us.\n<' + ytmatchstring2 + '>\nDon\'t post YouTube links or Phate will write an essay.')

  ytbmatch = re.search('https://www.youtube.com/.*', message.content)
  if ytbmatch:
    ytbsearchstring = ytbmatch.string
    ytbreplace2 = re.sub('https://youtu.be/', 'https://invidio.us/watch?v=', ytbsearchstring)
    if ytbreplace2:             
      ytbmatch2 = re.findall('https://invidio.us/.*', ytbreplace2, flags=0)
      if ytbmatch2:
        print(ytbmatch2)
        ytbmatchstring2 = ' '.join(ytbmatch2)
        print(ytbmatchstring2)
        await message.channel.send('**Heads up!**\n\nYou just posted a link to YouTube! This is extremely bad practice.\nBelow is a link to the same video o\nnInvidio.us.\n<' + ytbmatchstring2 + '>\nDon\'t post YouTube links or Phate will write an essay.')


  
# reddit UTM parameter stripping
  redditmatch = re.search('https://www.reddit.com/*', message.content)
  if redditmatch:
    redditmatchstring = redditmatch.string
    redditmatch2 = re.search('.utm.*', redditmatchstring)
    if redditmatch2:
      print(redditmatch2)
      redditutmstrip = re.sub('.utm.*', '', redditmatchstring)
      redditmatch3 = re.findall('https://www.reddit.com/.*', redditutmstrip, flags=0)
      print(redditmatch3)  
      redditmatchstring2 = ' '.join(redditmatch3)

      print('**Reddit link replaced\n' + redditutmstrip)
      await message.channel.send('**Heads up!**\n\nYou just posted a link that has UTM parameters.\nBelow is a safe version.\n<' + redditmatchstring2 + '>\nIf you keep posting links with UTM parameters Phate will write an essay.')
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
      
client.run(data["token"])
