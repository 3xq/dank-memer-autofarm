import discord, requests, time, asyncio, os
from discord.ext import commands, tasks

os.system('cls')

Bot = commands.Bot(command_prefix = '.', self_bot = True)
Channel = 900020551668600935

@tasks.loop(minutes = 1)
async def Hunt():
	Channel_Object = Bot.get_channel(Channel)

	await Channel_Object.send('pls hunt')

	while True:
		Message_Object = await Channel_Object.history(limit = 1).flatten()
		Message_Object = Message_Object[0]

		if Message_Object.author.id == 270904126974590976:
			break
		else:
			continue

	Message_Object = await Channel_Object.history(limit = 1).flatten()
	Message_Object = Message_Object[0]

	try:
		Brought_Back = Message_Object.content.split('brought back ')[1].split(' <')[0].lower()

		if 'nothing' not in Brought_Back.lower():
			print(f'Hunted and brought back: {Brought_Back}')
	except:
		eval('0+0')

@tasks.loop(minutes = 1)
async def Fish():
	Channel_Object = Bot.get_channel(Channel)

	await Channel_Object.send('pls fish')

	while True:
		Message_Object = await Channel_Object.history(limit = 1).flatten()
		Message_Object = Message_Object[0]

		if Message_Object.author.id == 270904126974590976:
			break
		else:
			continue

	Message_Object = await Channel_Object.history(limit = 1).flatten()
	Message_Object = Message_Object[0]

	try:
		Brought_Back = Message_Object.content.split('brought back ')[1].split(' <')[0].lower()

		if 'nothing' not in Brought_Back.lower():
			print(f'Fished and brought back: {Brought_Back}')
	except:
		eval('0+0')

@tasks.loop(minutes = 1)
async def Beg():
	Channel_Object = Bot.get_channel(Channel)

	await Channel_Object.send('pls beg')

	while True:
		Message_Object = await Channel_Object.history(limit = 1).flatten()
		Message_Object = Message_Object[0]

		if Message_Object.author.id == 270904126974590976:
			break
		else:
			continue

	Message_Object = await Channel_Object.history(limit = 1).flatten()
	Message_Object = Message_Object[0]

	try:
		Got = Message_Object.content.split('**⏣ ')[1].split('**')[0]

		print(f'Begged and got {Got}')
	except:
		eval('0+0')

@tasks.loop(minutes = 1)
async def Deposit():
	Channel_Object = Bot.get_channel(Channel)

	await Channel_Object.send('pls dep all')

@Bot.command()
async def start(ctx):
	await ctx.message.delete()

	while True:
		await ctx.send('pls inv')

		Channel_Object = Bot.get_channel(Channel)

		while True:
			Message_Object = await Channel_Object.history(limit = 1).flatten()
			Message_Object = Message_Object[0]

			if Message_Object.author.id == 270904126974590976:
				break
			else:
				continue

		Message_Object = await Channel_Object.history(limit = 1).flatten()
		Message_Object = Message_Object[0]

		Split = Message_Object.embeds[0].to_dict()['description'].split('\n')
		Items = []

		for Line in Split:
			if Line[:1] == '*' and 'Collectable' not in Line:
				Item = Line.split('`')[1]
				Items.append(Item)

				if Item not in ['fishingpole', 'huntingrifle', 'laptop']:
					await ctx.send(f'pls sell {Item}')
					time.sleep(3)

		if Items == ['fishingpole', 'huntingrifle', 'laptop']:
			break
		else:
			continue

	Hunt.start()
	Fish.start()
	Beg.start()
	Deposit.start()

@Bot.command()
async def debug(ctx):
	Channel_Object = Bot.get_channel(Channel)

	Message_Object = await Channel_Object.history(limit = 2).flatten()
	Message_Object = Message_Object[1]

	print(Message_Object.embeds[0].to_dict())

@Bot.event
async def on_message(message):
	if message.author.id == 270904126974590976 and message.channel.id == 900020551668600935 and 'fireball' in str(message.content).lower():
		Channel_Object = Bot.get_channel(Channel)

		Message_Object = await Channel_Object.send('pls with 30000')
		Message_Object = await Channel_Object.send('pls buy lifesaver')


@Bot.event
async def on_ready():
	Channel_Object = Bot.get_channel(Channel)
	await Channel_Object.send('pls bal')

	while True:
		Message_Object = await Channel_Object.history(limit = 1).flatten()
		Message_Object = Message_Object[0]

		if Message_Object.author.id == 270904126974590976:
			break
		else:
			continue

	Message_Object = await Channel_Object.history(limit = 1).flatten()
	Message_Object = Message_Object[0]

	print(Message_Object.embeds[0].to_dict()['description'].replace('**', '').replace('⏣', '').replace('`', '').replace('  ', ' ')+'\n')

Bot.run('TOKEN', bot = False, reconnect = True)
