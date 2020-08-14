import discord
import random
client = discord.Client()
token = 'NzQzOTAxNzIyMjgzNDc0OTg0.Xzbadw.n19XkVb3laalnd4APz6vhR2WxEc'

@client.event
async def on_ready():
    print('정상접속 완료 무시!')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('무시!'))

@client.event
async def on_message(message):
    if message.content == '푸키킨': 
        a = ['무시!', 'https://www.youtube.com/channel/UCLUOFrZmspqwKrrP_dqtlPw', '푸키키키키키키키키키킨', '우잉?']
        await message.channel.send(random.choice(a))

@client.event
async def on_message(message):
    if message.content == '푸키킨 유튜브': 
        embed = discord.Embed(title = '푸키킨 유튜브', description = 'https://www.youtube.com/channel/UCLUOFrZmspqwKrrP_dqtlPw', color = discord.Color.blue())
        await message.channel.send(embed = embed)

@client.event
async def on_message(message):
    if message.content == '봇범위': 
        embed = discord.Embed(title = '봇 지원범위', description = '무시방에서만 지원합니다', color = discord.Color.blue())
        await message.channel.send(embed = embed)

@client.event
async def on_message(message):
    if message.content == '무시야!': 
        a = ['왜', 'ㅇㅇ', '무시!', '왜.불.러']
        await message.channel.send(random.choice(a))

client.event
async def on_message(message):
    if message.content == '무시!': 
        a = ['무시!', '너도 무시를 아는군!!', 'https://tenor.com/view/wink-dog-animal-pet-gif-4800447', '푸키킨!!!']
        await message.channel.send(random.choice(a))

@client.event
async def on_message(message):
    if message.content == '서버연결확인': 
        await message.channel.send('연결이 정상적으로 되었습니다')
    elif message.content == '관리자 명령어 지원 확인':
        await message.channel.send('미지원')
    elif message.content == '안녕':
        await message.channel.send('안녕하세요')
    if message.content == 'ㅂ2':
        await message.channel.send('안녕히가세요')

client.run(token)