import discord
import os
import requests
import json
from jokeapi import Jokes  # Import the Jokes class

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n\n-" + json_data[0]['a']
    return (quote)


def setup():
    j = Jokes()
    joke = j.get_joke()
    setup = joke["setup"] +"\n \n" + joke["delivery"]
    return (setup)



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
    if msg.content.startswith("$dadjoke"):
        joke = setup()
        await msg.channel.send(joke)

client.run(os.getenv('TOKEN'))
