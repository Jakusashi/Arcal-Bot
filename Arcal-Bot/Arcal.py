from discord.ext import commands
from discord_slash import SlashCommand
import discord
import asyncio
import random
import string
import requests
import json
import coreapi

from datetime import datetime
from pytz import timezone

desc = '''Arcal Bot now in Python'''
xd = True
ef = True

bot = discord.Client()
bot = commands.Bot(command_prefix='~')
extensions = ['cogs.komendy']
slash = SlashCommand(bot, override_type=True)


if __name__ == '__main__':
	for extension in extensions:
		try:
			bot.load_extension(extension)
			print('Wygranko, Cog zauadowany!')
		except Exception as error:
			print('{} nie moszna zauadowac. [{}]'.format(extension, error))
@bot.event
async def on_ready():
	#activity = discord.Game(name="use / for commands list")
	#await bot.change_presence(status=discord.Status.online, activity=activity)
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

#@bot.event
#async def on_member_join(member):
	#with open('users.json', 'r') as f:
		#users = json.load(f)

	#await update_data(users, member)

	#with open('users.json', 'w') as f:
		#json.dump(users, f)

@bot.event
async def on_message(message):
	#with open('users.json', 'r') as f:
		#users = json.load(f)
	#y = 0
	#await update_data(users, message.author)
	#await on_reaction_add(reaction, message.author)
	#await add_rep(users, message.author, y)

	#with open('users.json', 'w') as f:
		#json.dump(users, f)

	msg = message.content.lower()
	ms = message.content
	mc = message.channel
	spanish_check = random.randint(0,10000)
	kon = random.randint(0,500)
	zmiana_czasu = random.randint(0,50)

	global xd
	global ef
	global wiadomosci_Ja
	if 'gwidon' in msg and ':gwidon' not in msg:
		gwi = 'obrazki/Guidox.png'
		nr = random.randint(0,37)
		gwi2 = gwi.replace("x", str(nr))
		await mc.send(file=discord.File(""+gwi2+""))

	if spanish_check == 5:
		await mc.send(file=discord.File('obrazki/inkwizycja.jpg'))
	if kon == 10:
		 await mc.send('Jak tam {0.author.mention}? Koń zwalony?'.format(message))
	if 'penis' in msg and ':penis:' not in msg:
		await mc.send(file=discord.File('obrazki/beniz.jpg'))
		
	if ':penis:' in msg:
		await mc.send('https://www.youtube.com/watch?v=jXglHzoG_Zs')
		
	if ('F' == ms or 'f' == ms) and ef:
		ef = False
		await mc.send('F')
	else:
		ef = True
	if 'arcal test' in msg:
		await mc.send('co test? jaki test?')
	if 'dzięki arcal' in msg:
		await mc.send('Polecam się')
	if '@everyone' in msg:
		await mc.send('https://youtu.be/EXnbMp1yr1k?t=113') or await mc.send('https://www.youtube.com/watch?v=74BzSTQCl_c')
	if 'oh shit' in msg or 'ah shit' in msg:
		await mc.send('here we go again')
	if 'ah gówno' in msg:
		await mc.send('tutaj my idziemy znowu')
	if 'zsrr' in msg or 'związek radziecki' in msg or 'ussr' in msg or 'związku radzieckiego' in msg:
		await mc.send('https://www.youtube.com/watch?v=U06jlgpMtQs')
	if 'wziąść' in msg:
		await mc.send('Wziąć, KURWA')
	if 'arcal play despacito' in msg:
		await mc.send('https://youtu.be/kJQP7kiw5Fk?t=28')
	if 'creeper' in msg:
		await asyncio.sleep(2)
		await mc.send('AW MAAAAN...')
	if 'hello there' in msg or 'hello-there' in msg:
		await mc.send('https://tenor.com/view/grevious-general-kenobi-star-wars-gif-11406339')
	if ('Xd' == ms or ' Xd' in ms or ' Xd ' in ms) and xd:
		xd = False
		await mc.send('```Serio, mało rzeczy mnie triggeruje tak jak to chore „Xd”. Kombinacji x i d można używać na wiele wspaniałych sposobów. Coś cię śmieszy? Stawiasz „xD”. Coś się bardzo śmieszy? Śmiało: „XD”! Coś doprowadza Cię do płaczu ze śmiechu? „XDDD” i załatwione. Uśmiechniesz się pod nosem? „xd”. Po kłopocie. A co ma do tego ten bękart klawiaturowej ewolucji, potwór i zakała ludzkiej estetyki - „Xd”? Co to w ogóle ma wyrażać? Martwego człowieka z wywalonym jęzorem? Powiem Ci, co to znaczy. To znaczy, że masz w telefonie włączone zaczynanie zdań dużą literą, ale szkoda Ci klikać capsa na jedno „d” później. Korona z głowy spadnie? Nie sondze. „Xd” to symptom tego, że masz mnie, jako rozmówcę, gdzieś, bo Ci się nawet kliknąć nie chce, żeby mi wysłać poprawny emotikon. Szanujesz mnie? Używaj „xd”, „xD”, „XD”, do wyboru. Nie szanujesz mnie? Okaż to. Wystarczy, że wstawisz to zjebane „Xd” w choć jednej wiadomości. Nie pozdrawiam.```')
	else:
		xd = True
	if 'september' in msg:
		await mc.send('https://youtu.be/Gs069dndIYk?t=20')
		
	if 'dobrze?' in msg:
		await mc.send('```Moim zdaniem to nie ma tak, że dobrze albo że nie dobrze. Gdybym miał powiedzieć, co cenię w życiu najbardziej, powiedziałbym, że ludzi. Ekhm… Ludzi, którzy podali mi pomocną dłoń, kiedy sobie nie radziłem, kiedy byłem sam. I co ciekawe, to właśnie przypadkowe spotkania wpływają na nasze życie. Chodzi o to, że kiedy wyznaje się pewne wartości, nawet pozornie uniwersalne, bywa, że nie znajduje się zrozumienia, które by tak rzec, które pomaga się nam rozwijać. Ja miałem szczęście, by tak rzec, ponieważ je znalazłem. I dziękuję życiu. Dziękuję mu, życie to śpiew, życie to taniec, życie to miłość. Wielu ludzi pyta mnie o to samo, ale jak ty to robisz?, skąd czerpiesz tę radość? A ja odpowiadam, że to proste, to umiłowanie życia, to właśnie ono sprawia, że dzisiaj na przykład buduję maszyny, a jutro… kto wie, dlaczego by nie, oddam się pracy społecznej i będę ot, choćby sadzić… znaczy… marchew.```')

	if 'december' in msg:
		await mc.send('https://youtu.be/CjCWhwdnCd0?t=19')

	if 'incest' in msg or 'sweet home alabama' in msg or 'kazirodztwo' in msg or 'kazirodztwa' in msg:
		await mc.send('https://youtu.be/ye5BuYf8q4o')

	if 'GAS GAS GAS' in ms or 'GASGASGAS' in ms:
		await mc.send('https://youtu.be/atuFSv2bLa8?t=78')

	if ms.startswith('cześ'):
        	await mc.send('Cześ {0.author.mention}'.format(message))
		
	if ms.startswith('Arcal znasz'):
        	await mc.send('Nie')

	if ms.startswith('Arcal wiesz'):
        	await mc.send('Nie')
	
	if ms.startswith('Arcal zrób'):
        	await mc.send('Sam se zrób')
	
	if ('kupię' in msg or 'zamówię' in msg or 'kupić' in msg or 'zamówić' in msg) and (message.author.id == xxx or message.author.id == xxx):
		await mc.send('Tylko nie bierz DPD, GLSa lub kuriera InPostu. Głupie kurwie nigdy nie dzwonią')
		
	if ('nie zesraj się' in msg) and message.author.id != xxx:
		await mc.send('{0.author.mention}, -10pkt reputacji za nieuzasadnione użycie NZS i wprowadzanie złej atmosfery na serwerze'.format(message))
		
	if ('nie zesraj się' in msg) and message.author.id == xxx:
		await mc.send('{0.author.mention}, +1pkt do reputacji za prawożądność i pilnowanie porządku na serwerze!'.format(message))
	
		
	#============Wyświetla czas UTC+2, kod może się przydać do czegoś w przyszłości============
	#if zmiana_czasu == 40:
	#	fmt = "%H:%M"
	#	now_utc = datetime.now(timezone('Egypt'))
	#	print(now_utc)
	#	await mc.send('No synek, gdyby nie ta zmiana czasu, to by była już ' + now_utc.strftime(fmt))

	await bot.process_commands(message)

bot.run("xxx", bot=True, reconnect=True)

#async def update_data(users, user):
	#if not user.id in users:
		#users[user.id] = {}
		#users[user.id]['reputacja'] = 0

#async def on_reaction_add(reaction, user):
	#if reaction.emoji == 'thumbsup':
		#y = 1
	#elif reaction.emoji == 'thumbsdown':
		#y = (-1)
	#else:
		#y = 0

#async def add_rep(users, user, y):
	#users[user.id]['reputacja'] += y

	#if y > 0:
		#await bot.send_message(channel, '{} zyskałeś punkt reputacji'.format(user.mention))
	#elif y < 0:
		#await bot.send_message(channel, '{} utraciłeś punkt reputacji'.format(user.mention)) 
