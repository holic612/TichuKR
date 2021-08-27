import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    game = discord.Game("테스트중")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("깔깔")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
