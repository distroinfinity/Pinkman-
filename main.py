import discord
import os
import requests
import json
import random

client = discord.Client()

def get_quote():
  response = requests.get("https://www.breakingbadapi.com/api/quote/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['quote']+'\n'+" -"+json_data[0]['author']+"\n"+ json_data[0]['series']
  return quote
"""
def get_char():
  response = requests.get("https://www.breakingbadapi.com/api/character/random")
  json_data = json.loads(response.text)
  #print(json_data)
  """
  json_data = 
  [{"char_id":57,"name":"Jack Welker","birthday":null,"occupation":["Criminal Gang Leader"],"img":"https://vignette.wikia.nocookie.net/breakingbad/images/c/ce/Jack5x13.png/revision/latest?cb=20130912225922","status":"Deceased","nickname":"Uncle Jack","appearance":[5],"portrayed":"Michael Bowen","category":"Breaking Bad","better_call_saul_appearance":null}]
  """
  name = str(json_data[0]['name'])
  birthday = ""
  birthday = json_data[0]['birthday']
  occupation = ""
  for k in json_data[0]['occupation']:
    occupation+=str(k)
  imgSource = str(json_data[0]['img'])
  nickname = str(json_data[0]['nickname'])
  char_info = imgSource+'\n'+name+'\n'+
  
  return()
"""
@client.event
async def on_ready():
  print('Bot is live as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  #print(msg)
  #print(msg[0:5])

  if msg.startswith('yo bitch'):
    await message.channel.send("Yo, yo, yo! 1-4-8-3 to the 3 to the 6 to the 9. representin' the ABQ. What up, Biatch? Leave it at the tone.")
  if msg =='yo quote':
    await message.channel.send(get_quote())
    """
  if msg =='yo character':
    await message.channel.send(get_char())
    """
client.run(os.getenv('TOKEN'))
