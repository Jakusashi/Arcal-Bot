import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import asyncio
import random
import string
import requests
import json

class YT(commands.Cog): 
	def __init__(self, bot):
        	self.bot = bot		
		
	@cog_ext.cog_slash(name='everythingwillfreeze')
	async def everythingwillfreeze(self, ctx: SlashContext):
		'''- Everything Will Freeze by Undead Corporation'''
		await ctx.send('https://www.youtube.com/watch?v=lkicMsn-s_8')
	
	@cog_ext.cog_slash(name='hestiastep')
	async def hestiastep(self, ctx: SlashContext):
		'''- 'Hestiastep by GlupiCycu'''
		await ctx.send('https://www.youtube.com/watch?v=nZsC5p9M3p8')
	
	@cog_ext.cog_slash(name='wrongchannel')
	async def wrongchannel(self, ctx: SlashContext):
		'''- You Reposted in the Wrong Neighborhood'''
		await ctx.send('https://www.youtube.com/watch?v=4feUSTS21-8')
	
	@cog_ext.cog_slash(name='rickroll')
	async def rickroll(self, ctx: SlashContext):
		'''- XcQ :)'''
		await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
	
	@cog_ext.cog_slash(name='sandstorm')
	async def sandstorm(self, ctx: SlashContext):
		'''- DUDUDUDUDU DU DUDUDUDUDU'''
		await ctx.send('https://www.youtube.com/watch?v=y6120QOlsfU')
	
	@cog_ext.cog_slash(name='celebration')
	async def celebration(self, ctx: SlashContext):
		'''- SEEEELEEBREJT GUD TAAJMS, COMON!'''
		await ctx.send('https://youtu.be/3GwjfUFyY6M?t=34')
	
	@cog_ext.cog_slash(name='dlaczego')
	async def dlaczego(self, ctx: SlashContext):
		'''- KURRRRWA, Dlaczego?'''
		await ctx.send('https://youtu.be/fFl7hEVSE1Q')
		
	@cog_ext.cog_slash(name='cyrkulacja')
	async def cyrkulacja(self, ctx: SlashContext):
		'''- Cyrkulacja Wszystkich!'''
		await ctx.send('https://youtu.be/RQmEERvqq70')
		
	@cog_ext.cog_slash(name='run')
	async def run(self, ctx: SlashContext):
		'''- BJEGNIIJ!'''
		await ctx.send('https://youtu.be/mw2kKyJu9gY?t=131')
		
	@cog_ext.cog_slash(name='gasgasgas')
	async def gasgasgas(self, ctx: SlashContext):
		'''- General Anakin Skywalker lol'''
		await ctx.send('https://youtu.be/atuFSv2bLa8?t=78')
		
	@cog_ext.cog_slash(name='crabrave')
	async def crabrave(self, ctx: SlashContext):
		'''- clack clack clack clack clack'''
		await ctx.send('https://youtu.be/LDU_Txk06tM?t=75')
		
	@cog_ext.cog_slash(name='dejavu')
	async def dejavu(self, ctx: SlashContext):
		'''- I've just been in this place before!'''
		await ctx.send('https://youtu.be/dv13gl0a-FA?t=1m4s')
		
	@cog_ext.cog_slash(name='duel')
	async def duel(self, ctx: SlashContext):
		'''- kiedy sprawy zaszly za daleko...'''
		await ctx.send('https://www.youtube.com/watch?v=ZTg6hg1miFg')
		
	@cog_ext.cog_slash(name='fbi')
	async def fbi(self, ctx: SlashContext):
		'''- *JEB JEB JEB* FBI, OPEN UP!'''
		await ctx.send('https://youtu.be/6fB8QiPTadY')	
		
	@cog_ext.cog_slash(name='fuckthisshit')
	async def fuckthisshit(self, ctx: SlashContext):
		'''- ...I'm out'''
		await ctx.send('https://www.youtube.com/watch?v=5FjWe31S_0g')
		
	@cog_ext.cog_slash(name='technounion')
	async def technounion(self, ctx: SlashContext):
		'''- TECHNO UNIOOOOOON!'''
		await ctx.send('TECHNOOO UNIOOOOOOOON!')
		await asyncio.sleep(1)
		await ctx.send('https://www.youtube.com/watch?v=PW4OIHDsWsM')
		
	@cog_ext.cog_slash(name='dolary')
	async def dolary(self, ctx: SlashContext):
		'''- dolary Goncia'''
		await ctx.send('https://www.tenor.co/IULU.gif ')
		
class Obrazkowe(commands.Cog): 
	def __init__(self, bot):
       		self.bot = bot
		
	@cog_ext.cog_slash(name='pointing')
	async def pointing(self, ctx: SlashContext):
		'''- NO U!'''
		await ctx.send(file=discord.File('obrazki/pointing_spiderman.jpg'))
		
	@cog_ext.cog_slash(name='ruchanie')
	async def ruchanie(self, ctx: SlashContext):
		'''- he he... segzig'''
		await ctx.send(file=discord.File('obrazki/ruchanie.jpg'))
	
	@cog_ext.cog_slash(name='stonks')
	async def stonks(self, ctx: SlashContext):
		'''- Potato Stonks!'''
		await ctx.send(file=discord.File('obrazki/stonks.png'))
	
	@cog_ext.cog_slash(name='meh')
	async def meh(self, ctx: SlashContext):
		'''- meh'''
		await ctx.send(file=discord.File('obrazki/meh.jpg'))
	
	@cog_ext.cog_slash(name='facepalm')
	async def facepalm(self, ctx: SlashContext):
		'''- facepalm'''
		await ctx.send(file=discord.File('obrazki/facepalm.jpg'))

	@cog_ext.cog_slash(name='fu')
	async def fu(self, ctx: SlashContext):
		'''- Fuck You'''
		await ctx.send(file=discord.File('obrazki/fuck you.png'))
		
	@cog_ext.cog_slash(name='getout')
	async def getout(self, ctx: SlashContext):
		'''- Get Out! Tak mowi TouHou gurl'''
		await ctx.send(file=discord.File('obrazki/get out.png'))
	
	@cog_ext.cog_slash(name='helping')
	async def helping(self, ctx: SlashContext):
		'''Shows this message'''
		await ctx.send(file=discord.File('obrazki/helping.jpg'))
	
	@cog_ext.cog_slash(name='karny')
	async def karny(self, ctx: SlashContext):
		'''- Karny Kabat'''
		await ctx.send(file=discord.File('obrazki/karny.jpeg'))
	
	@cog_ext.cog_slash(name='magic')
	async def magic(self, ctx: SlashContext):
		'''- Do you believe in magic?'''
		await ctx.send(file=discord.File('obrazki/magic.jpg'))
	
	@cog_ext.cog_slash(name='nani')
	async def nani(self, ctx: SlashContext):
		'''- NANI THE FUCK?!'''
		await ctx.send(file=discord.File('obrazki/nani.jpg'))

	@cog_ext.cog_slash(name='notworking')
	async def notworking(self, ctx: SlashContext):
		'''- That's not how it works you little shit'''
		await ctx.send(file=discord.File('obrazki/notwork.png'))

	@cog_ext.cog_slash(name='obviously')
	async def obviously(self, ctx: SlashContext):
		'''- Duuuh'''
		await ctx.send(file=discord.File('obrazki/obviously.jpg'))
	
	@cog_ext.cog_slash(name='ok')
	async def ok(self, ctx: SlashContext):
		'''- Ok by Saitama'''
		await ctx.send(file=discord.File('obrazki/ok.jpg'))
	
	@cog_ext.cog_slash(name='XD')
	async def XD(self, ctx: SlashContext):
		'''- Jeblem'''
		await ctx.send(file=discord.File('obrazki/xd.jpg'))
	
	@cog_ext.cog_slash(name='yamero')
	async def yamero(self, ctx: SlashContext):
		'''- Poniechaj swe niecne zamiary'''
		await ctx.send(file=discord.File('obrazki/yamero.jpg'))
	
	@cog_ext.cog_slash(name='trick')
	async def trick(self, ctx: SlashContext):
		''' - I'll try spinning - that's a good trick!'''
		await ctx.send(file=discord.File('obrazki/switch1.png'))
		await asyncio.sleep(2)
		await ctx.send(file=discord.File('obrazki/switch2.png'))

	@cog_ext.cog_slash(name='confused')
	async def confused(self, ctx: SlashContext):
		'''- Confused Olson Travolta'''
		await ctx.send(file=discord.File('obrazki/confused_olo.gif'))
	
	@cog_ext.cog_slash(name='illegal')
	async def illegal(self, ctx: SlashContext):
		'''- wait, that's...'''
		await ctx.send(file=discord.File('obrazki/illegal.jpg'))
	
	@cog_ext.cog_slash(name='niepierdol')
	async def niepierdol(self, ctx: SlashContext):
		'''- Niepierdol'''
		await ctx.send(file=discord.File('obrazki/niepierdol.png'))
		
	@cog_ext.cog_slash(name='putin')
	async def putin(self, ctx: SlashContext):
		'''- Putout!'''
		await ctx.send(file=discord.File('obrazki/putin.png'))
		await asyncio.sleep(2)
		await ctx.send(file=discord.File('obrazki/putout.png'))
		
	@cog_ext.cog_slash(name='x')
	async def x(self, ctx: SlashContext):
		'''- Doubt'''
		await ctx.send(file=discord.File('obrazki/x.png'))
		
	@cog_ext.cog_slash(name='ź')
	async def ź(self, ctx: SlashContext):
		'''- Seubt'''
		await ctx.send(file=discord.File('obrazki/ź.png'))
		
	@cog_ext.cog_slash(name='y')
	async def y(self, ctx: SlashContext):
		'''- Shame'''
		await ctx.send(file=discord.File('obrazki/y.jpg'))
		
	@cog_ext.cog_slash(name='excuseme')
	async def excuseme(self, ctx: SlashContext):
		'''- Excuse me, WTF?'''
		await ctx.send(file=discord.File('obrazki/excuseme.png'))
		
	@cog_ext.cog_slash(name='ruchacz')
	async def ruchacz(self, ctx: SlashContext):
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
		headers = {'Client-ID': 'wvn2wjz8507v3ajv24ewu9090ic669', 'Authorization': 'Bearer bpvzygwivjh4vl0pq0h7hdjdexzyku'}

		parameters = 'search "'+tytul+'"; fields name,genres,platforms,cover,release_dates.human;'
		response = requests.post("https://api.igdb.com/v4/games", data=parameters, headers=headers)
		data = response.json()	
		await ctx.send('***' + data[0]['name'] + '*** \n Data Premiery: ' + data[0]['release_dates'][0]['human'])
		genresy=str(data[0]['genres'])[1:-1]
		platformy=str(data[0]['platforms'])[1:-1]
		okladka=str(data[0]['cover'])

		parameters2 = "fields name; where id = ("+genresy+");"
		response2 = requests.post("https://api.igdb.com/v4/genres", data=parameters2, headers=headers)
		data = response2.json()
		items = []
		for item in data:
			items.append(item['name'])
		await ctx.send(' Gatunek: *' + str(items)[1:-1] + '*')

		parameters3 = "fields abbreviation; where id = ("+platformy+");"
		response3 = requests.post("https://api.igdb.com/v4/platforms", data=parameters3, headers=headers)
		data = response3.json()
		items2 = []
		for item in data:
			items2.append(item['abbreviation'])
		await ctx.send(' Platformy: *' + str(items2)[1:-1] + '*')


		parameters4 = "fields image_id; where id = ("+okladka+");"
		response4 = requests.post("https://api.igdb.com/v4/covers", data=parameters4, headers=headers)
		data = response4.json()
		await ctx.send("https://images.igdb.com/igdb/image/upload/t_cover_big/" + data[0]['image_id'] + ".jpg")
		
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
