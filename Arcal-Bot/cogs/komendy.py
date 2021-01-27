import discord
from discord.ext import commands
import asyncio
import random
import string
import requests
import json

class YT(commands.Cog): 
	def __init__(self, bot):
        	self.bot = bot		
	
	@commands.command(name='everythingwillfreeze')
	async def everythingwillfreeze(self, ctx):
		'''- Everything Will Freeze by Undead Corporation'''
		await ctx.send('https://www.youtube.com/watch?v=lkicMsn-s_8')
	
	@commands.command(name='hestiastep')
	async def hestiastep(self, ctx):
		'''- Hestiastep by GlupiCycu'''
		await ctx.send('https://www.youtube.com/watch?v=nZsC5p9M3p8')
	
	@commands.command(name='wrongchannel')
	async def wrongchannel(self, ctx):
		'''- You Reposted in the Wrong Neighborhood'''
		await ctx.send('https://www.youtube.com/watch?v=4feUSTS21-8')
	
	@commands.command(name='rickroll')
	async def rickroll(self, ctx):
		'''- XcQ :)'''
		await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
	
	@commands.command(name='sandstorm')
	async def sandstorm(self, ctx):
		'''- DUDUDUDUDU DU DUDUDUDUDU'''
		await ctx.send('https://www.youtube.com/watch?v=y6120QOlsfU')
	
	@commands.command(name='celebration')
	async def celebration(self, ctx):
		'''- SEEEELEEBREJT GUD TAAJMS, COMON!'''
		await ctx.send('https://youtu.be/3GwjfUFyY6M?t=34')
	
	@commands.command(name='dlaczego')
	async def dlaczego(self, ctx):
		'''- KURRRRWA, Dlaczego?'''
		await ctx.send('https://youtu.be/fFl7hEVSE1Q')
		
	@commands.command(name='cyrkulacja')
	async def cyrkulacja(self, ctx):
		'''- Cyrkulacja Wszystkich!'''
		await ctx.send('https://youtu.be/RQmEERvqq70')
		
	@commands.command(name='run')
	async def run(self, ctx):
		'''- BJEGNIIJ!'''
		await ctx.send('https://youtu.be/mw2kKyJu9gY?t=131')
		
	@commands.command(name='gasgasgas')
	async def gasgasgas(self, ctx):
		'''- General Anakin Skywalker lol'''
		await ctx.send('https://youtu.be/atuFSv2bLa8?t=78')
		
	@commands.command(name='crabrave')
	async def crabrave(self, ctx):
		'''- clack clack clack clack clack'''
		await ctx.send('https://youtu.be/LDU_Txk06tM?t=75')
		
	@commands.command(name='dejavu')
	async def dejavu(self, ctx):
		'''- I've just been in this place before!'''
		await ctx.send('https://youtu.be/dv13gl0a-FA?t=1m4s')
		
	@commands.command(name='duel')
	async def duel(self, ctx):
		'''- kiedy sprawy zaszly za daleko...'''
		await ctx.send('https://www.youtube.com/watch?v=ZTg6hg1miFg')
		
	@commands.command(name='fbi')
	async def fbi(self, ctx):
		'''- *JEB JEB JEB* FBI, OPEN UP!'''
		await ctx.send('https://youtu.be/6fB8QiPTadY')	
		
	@commands.command(name='fuckthisshit')
	async def fuckthisshit(self, ctx):
		'''- ...I'm out'''
		await ctx.send('https://www.youtube.com/watch?v=5FjWe31S_0g')
		
	@commands.command(name='technounion')
	async def technounion(self, ctx):
		'''- TECHNO UNIOOOOOON!'''
		await ctx.send('TECHNOOO UNIOOOOOOOON!')
		await asyncio.sleep(1)
		await ctx.send('https://www.youtube.com/watch?v=PW4OIHDsWsM')
		
	@commands.command(name='dolary')
	async def dolary(self, ctx):
		'''- dolary Goncia'''
		await ctx.send('https://www.tenor.co/IULU.gif ')
		
class Obrazkowe(commands.Cog): 
	def __init__(self, bot):
       		self.bot = bot
		
	@commands.command(name='pointing')
	async def pointing(self, ctx):
		'''- NO U!'''
		await ctx.send(file=discord.File('obrazki/pointing_spiderman.jpg'))
		
	@commands.command(name='ruchanie')
	async def ruchanie(self, ctx):
		'''- he he... segzig'''
		await ctx.send(file=discord.File('obrazki/ruchanie.jpg'))
	
	@commands.command(name='stonks')
	async def stonks(self, ctx):
		'''- Potato Stonks!'''
		await ctx.send(file=discord.File('obrazki/stonks.png'))
	
	@commands.command(name='meh')
	async def meh(self, ctx):
		'''- meh'''
		await ctx.send(file=discord.File('obrazki/meh.jpg'))
	
	@commands.command(name='facepalm')
	async def facepalm(self, ctx):
		'''- facepalm'''
		await ctx.send(file=discord.File('obrazki/facepalm.jpg'))

	@commands.command(name='fu')
	async def fu(self, ctx):
		'''- Fuck You'''
		await ctx.send(file=discord.File('obrazki/fuck you.png'))
		
	@commands.command(name='getout')
	async def getout(self, ctx):
		'''- Get Out! Tak mowi TouHou gurl'''
		await ctx.send(file=discord.File('obrazki/get out.png'))
	
	@commands.command(name='helping')
	async def helping(self, ctx):
		'''Shows this message'''
		await ctx.send(file=discord.File('obrazki/helping.jpg'))
	
	@commands.command(name='karny')
	async def karny(self, ctx):
		'''- Karny Kabat'''
		await ctx.send(file=discord.File('obrazki/karny.jpeg'))
	
	@commands.command(name='magic')
	async def magic(self, ctx):
		'''- Do you believe in magic?'''
		await ctx.send(file=discord.File('obrazki/magic.jpg'))
	
	@commands.command(name='nani')
	async def nani(self, ctx):
		'''- NANI THE FUCK?!'''
		await ctx.send(file=discord.File('obrazki/nani.jpg'))

	@commands.command(name='notworking')
	async def notworking(self, ctx):
		'''- That's not how it works you little shit'''
		await ctx.send(file=discord.File('obrazki/notwork.png'))

	@commands.command(name='obviously')
	async def obviously(self, ctx):
		'''- Duuuh'''
		await ctx.send(file=discord.File('obrazki/obviously.jpg'))
	
	@commands.command(name='ok')
	async def ok(self, ctx):
		'''- Ok by Saitama'''
		await ctx.send(file=discord.File('obrazki/ok.jpg'))
	
	@commands.command(name='XD')
	async def XD(self, ctx):
		'''- Jeblem'''
		await ctx.send(file=discord.File('obrazki/xd.jpg'))
	
	@commands.command(name='yamero')
	async def yamero(self, ctx):
		'''- Poniechaj swe niecne zamiary'''
		await ctx.send(file=discord.File('obrazki/yamero.jpg'))
	
	@commands.command(name='trick')
	async def trick(self, ctx):
		''' - I'll try spinning - that's a good trick!'''
		await ctx.send(file=discord.File('obrazki/switch1.png'))
		await asyncio.sleep(2)
		await ctx.send(file=discord.File('obrazki/switch2.png'))

	@commands.command(name='confused')
	async def confused(self, ctx):
		'''- Confused Olson Travolta'''
		await ctx.send(file=discord.File('obrazki/confused_olo.gif'))
	
	@commands.command(name='illegal')
	async def illegal(self, ctx):
		'''- wait, that's...'''
		await ctx.send(file=discord.File('obrazki/illegal.jpg'))
	
	@commands.command(name='niepierdol')
	async def niepierdol(self, ctx):
		'''- Niepierdol'''
		await ctx.send(file=discord.File('obrazki/niepierdol.png'))
		
	@commands.command(name='putin')
	async def putin(self, ctx):
		'''- Putout!'''
		await ctx.send(file=discord.File('obrazki/putin.png'))
		await asyncio.sleep(2)
		await ctx.send(file=discord.File('obrazki/putout.png'))
		
	@commands.command(name='x')
	async def x(self, ctx):
		'''- Doubt'''
		await ctx.send(file=discord.File('obrazki/x.png'))
		
	@commands.command(name='ź')
	async def ź(self, ctx):
		'''- Seubt'''
		await ctx.send(file=discord.File('obrazki/ź.png'))
		
	@commands.command(name='y')
	async def y(self, ctx):
		'''- Shame'''
		await ctx.send(file=discord.File('obrazki/y.jpg'))
		
	@commands.command(name='excuseme')
	async def excuseme(self, ctx):
		'''- Excuse me, WTF?'''
		await ctx.send(file=discord.File('obrazki/excuseme.png'))
		
	@commands.command(name='ruchacz')
	async def ruchacz(self, ctx):
		'''- Tancz Gwidon, tancz!'''
		await ctx.send(file=discord.File('obrazki/ruchacz.gif'))		

class Funkcje(commands.Cog): 
	def __init__(self, bot):
        	self.bot = bot
		
	@commands.command(name='randomlinkyt')
	async def randomlinkyt(self, ctx):
		'''- Generuje Randomowy YT-link'''
		def generator(dlugoscstringow=11, literkiicyferki = string.ascii_letters + string.digits):		
			return ''.join(random.choice(literkiicyferki) for _ in range(dlugoscstringow))

		link = 'https://youtu.be/x'
		znak = generator()
		await ctx.send(link.replace("x", str(znak)))
		
	@commands.command(name='gra_info')	
	async def gra_info(self, ctx, tytul):
		'''- Pamietaj, podaj tytul gry'''
		headers = {'user-key': 'token'}

		parameters = 'search "'+tytul+'"; fields name,genres,platforms,cover,release_dates.human;'
		response = requests.post("https://api-v3.igdb.com/games", data=parameters, headers=headers)
		data = response.json()	
		await ctx.send('***' + data[0]['name'] + '*** \n Data Premiery: ' + data[0]['release_dates'][0]['human'])
		genresy=str(data[0]['genres'])[1:-1]
		platformy=str(data[0]['platforms'])[1:-1]
		okladka=str(data[0]['cover'])

		parameters2 = "fields name; where id = ("+genresy+");"
		response2 = requests.post("https://api-v3.igdb.com/genres", data=parameters2, headers=headers)
		data = response2.json()
		items = []
		for item in data:
			items.append(item['name'])
		await ctx.send(' Gatunek: *' + str(items)[1:-1] + '*')

		parameters3 = "fields abbreviation; where id = ("+platformy+");"
		response3 = requests.post("https://api-v3.igdb.com/platforms", data=parameters3, headers=headers)
		data = response3.json()
		items2 = []
		for item in data:
			items2.append(item['abbreviation'])
		await ctx.send(' Platformy: *' + str(items2)[1:-1] + '*')


		parameters4 = "fields image_id; where id = ("+okladka+");"
		response4 = requests.post("https://api-v3.igdb.com/covers", data=parameters4, headers=headers)
		data = response4.json()
		await ctx.send("https://images.igdb.com/igdb/image/upload/t_cover_big/" + data[0]['image_id'] + ".jpg")

		print(response.text)
		print(response2.text)
		print(response3.text)
		print(response4.text)
		
	@commands.command(name='swgoh')	
	async def swgoh(self, ctx, nazwa):
		'''- po komendzie wprowadz nazwe postaci'''
		headers = {'user-key': '839c05bd44e47d354fbec5ecb19640bc'}
		
		response = requests.get("http://swgoh.gg/api/characters", headers=headers)
		data = response.json()
		x = 0;
		y = 0;
		while y < 1:
			if nazwa.lower() in data[x]['name'].lower():
				link = data[x]['url']
				await ctx.send(link)
				y = 1
			else:
				x += 1 
			
def setup(bot):
	bot.add_cog(YT(bot))
	bot.add_cog(Obrazkowe(bot))
	bot.add_cog(Funkcje(bot))
