import discord
import os
import requests
import json
client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return(quote)

def get_joke():
    response = requests.get("https://dad-jokes.p.rapidapi.com/random/joke")
    json_data = json.loads(response.text)
    joke = json_data['body'][2] + "\n" + json_data['body'][3]

def update_inspiration(message):
    if "encouragements" in db.key():
        encouragements = db["encouragements"]
        encouragements.append(message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) >  index:
        del encouragements
        db["encouragements"] = encouragements
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format((client)))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith("$pickmeup"):
        quote = get_quote()
        await msg.channel.send(quote)

client.run(os.getenv('TOKEN'))
