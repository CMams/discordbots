import discord
import asyncio
import random
import os
import requests
import app
import config

def run():
    """Run the bot"""
    client.run(config.DISCORD_TOKEN)

client = discord.Client()

print("Logging on...")
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('tet?') or message.content.startswith('Tet?'):
		tet = random.choice(['Tet or no balls', 'Tet or uninstall', 'Of course.', "Haha bitches, 3rd dande box this week. I'm sorry you were saying something?" , 'Idk ask Dadfrog', 'With that many stacks? What are you Ragdan?', 'Congrats on Duo'])
		await client.send_message(message.channel, tet)
	elif message.content.startswith('!isitgay') or message.content.startswith('isitgay?'):
		isitgay = random.choice(['Of Course.','Depends, is ranger a playable class?','ImGay', 'Not as gay as ranger mains','Cabbages are pretty gay','Idk, but Kama SoonTM','Only Rag would know','Gayer than aids', 'Nah, definitely not', 'Depends, is Smash in a frat?', 'Depends, is Dras gay?', 'Dadfrog decides', 'Ummm, what are we even talking about?'])
		await client.send_message(message.channel, isitgay)
	elif message.content.startswith('!drasjoke') or message.content.startswith('!DrasJoke'):
		DrasJoke = "Dras joke detected! Quick, here's a Chuck Norris joke instead: "
		joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
		DrasJoke += joke
		await client.send_message(message.channel, DrasJoke)
	elif message.content.startswith('!Zandi') or message.content.startswith('!zandi'):
		Zandi = "Commands:\n!DrasJoke \nTet? \nisitgay?"
		await client.send_message(message.channel, Zandi)
	##elif message.content.startswith('!yok') or message.content.startswith('!Yok'):
	##	years = 55 - #userinput
	##	yok = "I have shoes " + years +" older than you."
	##	await client.send_message(message.channel, yok)

client.run(config.DISCORD_TOKEN)



