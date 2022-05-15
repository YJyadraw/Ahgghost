import discord
from discord.ext import commands
import json
import random

with open("set.json",'r',encoding='utF8')as jFile:
    jdata=json.load(jFile)

bot=commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print(">>你的機器人已經上線了~<<")
    game = discord.Game('陳勳')
    await bot.change_presence(status=discord.Status.idle, activity=game)




@bot.event
async def on_message(msg):
    IDK=random.choice(jdata['IDK'])
    idiot=random.choice(jdata['idiot'])
    think=random.choice(jdata['think'])
    laugh=random.choice(jdata['laugh'])
    bad_luck=random.choice(jdata['bad_luck'])
    whether=random.choice(jdata['whether'])
    hi=random.choice(jdata['hi'])
    if msg.author == bot.user:
        return
    if '笑死' in msg.content:
       await msg.channel.send(F'{laugh}')
    if '覺得' in msg.content:
        await msg.channel.send(F'{think}')
    if '真不錯' in msg.content:
        await msg.channel.send(F'其實也還好。')
    if '不知道' in msg.content:
        await msg.channel.send(F'{IDK}')
    if '「大凶」' in msg.content:
        await msg.channel.send(F'{bad_luck}')
    if '「兇」' in msg.content:
        await msg.channel.send(F'{bad_luck}')
    if '「小兇」' in msg.content:
        await msg.channel.send(F'下次抽個大兇吧')
    if '廢物' in msg.content:
        await msg.channel.send(F'{idiot}')
    if '低能兒' in msg.content:
        await msg.channel.send(F'{idiot}')
    if msg.content.startswith('說'):
      tmp = msg.content.split(" ",2)
      if len(tmp) == 1:
        await msg.channel.send("連講話都說不清楚了要我跟你講?")
      else:
        await msg.channel.send(tmp[1])
    if '要不要' in msg.content:
        await msg.channel.send(F'{whether}')
    if '幹' in msg.content:
        await msg.channel.send(F'都給你幹就好啦')
    if '嗨' in msg.content:
        await msg.channel.send(F'{hi}')
    if '哈囉' in msg.content:
        await msg.channel.send(F'{hi}')
    if '你好' in msg.content:
        await msg.channel.send(F'{hi}')



@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}(ms)')


bot.run(jdata['TOKEN'])