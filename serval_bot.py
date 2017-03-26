import discord
import asyncio
import re
import random
import time
from twitch import TwitchClient
from discord.ext.commands import Bot

my_bot=discord.Client()
client=TwitchClient(client_id='TWITICH ID')

def twitchSearchByChannel(query):
	#Just !Stream
	if(query.lower()=="!stream"):
		query2="saltyflakes"

	#Otherwise remove it
	else:
		query1=query.split(" ")
		if (len(query1)!=2):
			return("Sugoi! Your search even confused Kaban-chan! Did you spell the channel name correctly?")
		query2=query1[1]

	channel=client.search.channels(query2,1,0)
	#print(channel[0])
	if channel[0].name.lower()!=query2.lower():
		return("There is no channel by that name, maybe Red Fox will know something about it!\nDid you spell the channel name correctly?")
	else:
		if (channel[0].game!=""):
			return("Sugoi! "+channel[0].display_name+"'s last game played was "+channel[0].game+"\nhttps://www.twitch.tv/"+channel[0].name)
		else:
			return("Ehhhh? "+channel[0].display_name+" hasn't played a game?")

def erabe(query):
	if (query=="!pick"):
		return ("Ehhhhh? You didn't give me anything to choose from!\nSeparate your options with spaces!")

	else:
		query1=query.split(" ")
		query1.remove("!pick")
		time.sleep(3)
		return ("I pick "+random.choice(query1)+"!")


#text handler because i want more than commands
@my_bot.event
@asyncio.coroutine 
def on_message(message):
	member=message.author.id

	if re.search('please don\'t eat me',message.content,re.IGNORECASE):
		return (yield from my_bot.send_message(message.channel,"I won't eat you!"))
	#hello
	elif message.content.startswith('!hello'):
		return (yield from my_bot.send_message(message.channel,"Hello! I'm Serval the Serval Cat!"))
	#japari
	elif message.content.startswith('!japari'):
		return (yield from my_bot.send_message(message.channel,"https://www.youtube.com/watch?v=xkMdLcB_vNU"))	
	#Help/Tasukete
	elif message.content.startswith('!help'):
		return (yield from my_bot.send_message(message.channel,"Wow Boss started talking!\n The following commands are currently in order:\n!pick\n!stream\n!japari\n!hello\n!help"))
	elif message.content.startswith('!stream'):
		return (yield from my_bot.send_message(message.channel,twitchSearchByChannel(message.content)))
	elif message.content.startswith('!pick'):
		return (yield from my_bot.send_message(message.channel,erabe(message.content)))




	#last resort
	elif message.content.startswith('!'):
		return(yield from my_bot.send_message(message.channel,"Sugoi! <@{0}> must be a friend who is good at asking dumb questions!\n\t".format(member)))

		



my_bot.run("BOT ID FROM DISCORD APPS")

