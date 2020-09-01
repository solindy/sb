import discord
import asyncio
import datetime
import os

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is Ready.(24h online)")
    game = discord.Game('L')
    await client.change_presence(status=discord.Status.online, activity=game)


# !dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('!sb dm'):
        if message.author.guild_permissions.manage_messages:
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        msg = message.content[7:]
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at,
                                              title="Various Games Server 공지")
                        embed.add_field(name="-----------------------------------------", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/3wX5cHh")
                        await i.send(embed=embed)
                    except:
                        pass
        else:
            await message.channel.send("ERROR : You Do Not Have Permissions")

    if message.content.startswith("토리 멍청이"):
        await message.channel.send("ㅇㅈ")
    if message.content.startswith("Tori is L"):
        await message.channel.send("LLLLLLLLL")
    if message.content.startswith("tori is L"):
        await message.channel.send("LLLLLLLLL")
    if message.content.startswith("토리멍청이"):
        await message.channel.send("ㅇㅈ")
    if message.content.startswith("반짝반짝 희벼리"):
        await message.channel.send("멍청하게 비치네")
    if message.content.startswith("반짝반짝 희별이"):
        await message.channel.send("멍청하게 비치네")
    if message.content.startswith("마트롤시카"):
        await message.channel.send("마트롤시카?!")
    if message.content.startswith("솔린디가 누구임"):
        await message.channel.send("나임")
    if message.content.startswith("도토리묵"):
        await message.channel.send("도토리묵 맛있겠다")

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
            await message.channel.send("ERROR : You Do Not Have Permissions")
    
    if message.content.startswith("!sb vote"):
        if message.author.guild_permissions.manage_messages:
            ej = message.content[9:]
            emoji = await message.channel.send("투표해 주세요! " + "**" + ej + "**" + " (찬/반, 중복투표 금지)")
            await emoji.add_reaction("\U0001F44D")
            await emoji.add_reaction("\U0001F44E")
            return
        else:
            await message.channel.send("ERROR : You Do Not Have Permissions")

    if message.content.startswith("!sb"):
        mg = message.content[4:]
        if str(mg) == str("help"):
            embed = discord.Embed(title="Solindy Bot Help", description="솔린디 봇 도움말", color=0x00aaaa)
            embed.add_field(name="1. !sb dm <할 말>", value=" - 전체 DM 공지를 보냅니다", inline=False)
            embed.add_field(name="2. !sb clean <숫자>", value=" - 정한 숫자만큼 밑에서부터 메세지를 삭제합니다", inline=False)
            embed.add_field(name="3. !sb msg", value=" - 사용 가능한 메시지 채팅 반응을 모두 표시합니다", inline=False)
            embed.add_field(name="4. !sb vote <주제>", value=" - 주제에 대한 찬반 투표를 진행합니다", inline=False)
            await message.channel.send(embed=embed)
        if str(mg) == str("msg"):
            await message.channel.send("토리 멍청이 / Tori is L / 반짝반짝 희벼리 / 마트롤시카 / 솔린디가 누구임 / 도토리묵")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
