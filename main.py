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

def get_char():
  response = requests.get("https://www.breakingbadapi.com/api/character/random")
  json_data = json.loads(response.text)

  """
  #print(json_data)
  json_data = 
  [{"char_id":57,"name":"Jack Welker","birthday":null,"occupation":["Criminal Gang Leader"],"img":"https://vignette.wikia.nocookie.net/breakingbad/images/c/ce/Jack5x13.png/revision/latest?cb=20130912225922","status":"Deceased","nickname":"Uncle Jack","appearance":[5],"portrayed":"Michael Bowen","category":"Breaking Bad","better_call_saul_appearance":null}]
  """

  embed = discord.Embed(
    title = json_data[0]['name'],
    color = discord.Colour.blue()
  )

  embed.set_image(url=json_data[0]['img'])
  if(json_data[0]['nickname']!=None):
    embed.add_field(name='Nickname',value=json_data[0]['nickname'],inline=False)
  
  if(json_data[0]['birthday']!=None):
    embed.add_field(name='Birthday',value=json_data[0]['birthday'],inline=False)
  
  if(json_data[0]['occupation'][0]!=None):
    embed.add_field(name='Occupation',value=json_data[0]['occupation'][0],inline=False)
  
  if(json_data[0]['status']!=None):
    embed.add_field(name='Status',value=json_data[0]['status'],inline=False)
  
  return(embed)


@client.event
async def on_ready():
  print('Pinkman! is live as {0.user}'.format(client))

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
  
  if msg =='yo character':
    await message.channel.send(embed=get_char())
  
client.run(os.getenv('TOKEN'))
