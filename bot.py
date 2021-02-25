import discord, requests
import os, tempfile
import random
from img_editing import make_cite
from datetime import datetime, date, timedelta
from discord.ext import commands, tasks

prefixo = '.'
client = commands.Bot(command_prefix = prefixo)
async def naninha(ctx):
     await ctx.send('hora de dormir ai galera bora')
     

schedule = []
token = open('token.txt', 'r').read()



def job():
    print('oi galera')

#eventos
@client.event
async def on_ready():
    print('tudo certo.')
    a.start()

#@client.event
#async def on_message(message):
#    if "ão" in message.content:
#        await message.channel.send('Meu pau na sua mão')
#        return

@tasks.loop(seconds=5)
async def a():
    canal = client.get_channel(788194445748600873)
    temp = []
    while schedule:
        item = schedule.pop()
        hora = item[0]
        msg = item[1]
        if datetime.now() >= hora:
            hora += timedelta(days = 1)
            await canal.send(f'hora de dormir galerinha {msg}')
        temp.append([hora, msg])
    while temp:
        schedule.append(temp.pop())

#comandos
@client.command()
async def soninho(ctx, hora, *args):
    msg = (' '.join(args))
    fhora = datetime.combine(date.today(),datetime.strptime(hora, '%H:%M').time())
    schedule.append([fhora, msg])
    print(schedule)


@client.command()
async def teste(ctx):
    await ctx.send('eae mano tudo certo')

@client.command()
async def teste2(ctx):
    await ctx.send('cu de cachorro')

@client.command()
async def falae(ctx):
    await ctx.send('Pinguim')

@client.command()
async def carina(ctx):
    await ctx.send('Bolo de banana')

@client.command()
async def henrique(ctx):
    await ctx.send('o mais brabo')

@client.command()
async def kevin(ctx):
    await ctx.send('waifuzin da galera')

@client.command()
async def guido(ctx):
    await ctx.send('superfície não orientável <:gaara:811438983699628092>')

@client.command()
async def joao(ctx):
    await ctx.send('BHG <:like:803073240204705792>')

@client.command()
async def caio(ctx):
    await ctx.send('F1')

@client.command()
async def ão(ctx):
    await ctx.send('meu pau na sua mão')

@client.command()
async def al(ctx):
    await ctx.send('pega no meu pau')

@client.command()
async def eio(ctx):
    await ctx.send('seu cu parado meu pau sem freio')

@client.command()
async def alvaro(ctx):
    await ctx.send('rei do spoiler')

@client.command()
async def citeadd(ctx, *args):
    autor = ctx.message.mentions[0].id
    texto = ' '.join(args[1:])
    with open(f'cite/{autor}.txt', 'a') as f:
        f.write(texto + '\n')
    print(texto)

@client.command()
async def cite(ctx):
    autor_id = ctx.message.mentions[0].id
    autor_nick = ctx.message.mentions[0].nick
    autor_url = ctx.message.mentions[0].avatar_url
    text = str()
    try:
        with open(f'cite/{autor_id}.txt', 'r') as f:
            citations = f.readlines()
            rnumber = random.randint(0,len(citations) - 1)
            text = citations[rnumber][:-1]
    except Exception:
        await ctx.send(f"<@{autor_id}> não possue nenhuma citação.\nUse o comando {prefixo}citeadd para adiciona-las.")
        return 0
    #await ctx.send(f'\"{text}\"\n{autor_nick}')
    foto = requests.get(autor_url)
    tmpfile, path = tempfile.mkstemp(suffix = '.webp')
    try:
        with os.fdopen(tmpfile, 'wb') as f:
            f.write(foto.content)
        make_cite(path, f'\"{text}\"', autor_nick)
        await ctx.send(file=discord.File(path))
    finally:
        os.remove(path)

@client.command()
async def fotinho(ctx,*args):
    user = ctx.message.mentions[0]
    user_url = user.avatar_url
    await ctx.send(f'Baixando fotinha de {user} no link {user_url}.')
    foto = requests.get(user_url)
    tmpfile, path = tempfile.mkstemp(suffix = '.webp')
    try:
        with os.fdopen(tmpfile, 'wb') as f:
            f.write(foto.content)
        make_cite(path,path)
        await ctx.send(file=discord.File(path))
    finally:
        os.remove(path)

client.run(token)
