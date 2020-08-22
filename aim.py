import discord
import asyncio
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다.")
    game = discord.Game('L')
    await client.change_presence(status=discord.Status.online, activity=game)

#!dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('!sb dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[7:]
                    embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="Various Games Server 공지")
                    embed.add_field(name="-----------------------------------------", value=msg, inline=True)
                    embed.set_footer(text=f"https://discord.gg/3wX5cHh")
                    await i.send(embed=embed)
                except:
                    pass

    if message.content.startswith("토리 멍청이"):
        await message.channel.send("ㅇㅈ")
    if message.content.startswith("Tori is L"):
        await message.channel.send("LLLLLLLLL")
    if message.content.startswith("토리멍청이"):
        await message.channel.send("ㅇㅈ")
    if message.content.startswith("반짝반짝 희벼리"):
        await message.channel.send("멍청하게 비치네")
    if message.content.startswith("반짝반짝 희별이"):
        await message.channel.send("멍청하게 비치네")

    if message.content.startswith("!sb clean"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[10:]
                if str(amount) >= str(51):
                    await message.channel.send("50 이하의 수를 입력해 주세요.")
                else:
                    await message.channel.purge(limit=int(amount))
                    await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("당신은 권한이 없기 때문에 채팅청소 명령어를 사용하실 수 없습니다.")


    if message.content.startswith("!sb"):
        mg = message.content[4:]
        if str(mg) == str("help"):
            await message.channel.send("1. !sb dm <할 말> \n - 전체 DM 공지를 보냅니다\n2. !sb clean <숫자> \n - 정한 숫자만큼 밑에서부터 메세지를 삭제합니다.")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
