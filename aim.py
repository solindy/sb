import asyncio
import discord
from discord.ext import commands
import random
from discord.utils import get
import os

app = commands.Bot(command_prefix='!sb ')

@app.event
async def on_ready():
    print("봇 온라인")
    game = discord.Game("Verious Games Server")
    await app.change_presence(status=discord.Status.online, activity=game)

app.remove_command("help")

@app.command(pass_context=True)
async def dm(ctx, text):
    if ctx.message.author.bot:
        return None
    if ctx.message.author.guild_permissions.manage_messages:
        for i in ctx.message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = ctx.message.content[7:]
                    embed = discord.Embed(colour=0x1DDB16, timestamp=ctx.message.created_at,
                                              title="Various Games Server 공지")
                    embed.add_field(name="-----------------------------------------", value=msg, inline=True)
                    embed.set_footer(text=f"https://discord.gg/3wX5cHh")
                    await i.send(embed=embed)
                except:
                    pass
    else:
        await ctx.message.channel.send("당신은 권한이 없기 때문에 이 명령어를 사용할 수 없습니다")

@app.command(pass_context=True)
async def clean(ctx, amount):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if str(amount) >= str(51):
                await ctx.send("50 이하의 수를 입력해 주세요.")
            else:
                await ctx.message.channel.purge(limit=int(amount) + 1)
                await ctx.send(f"**{amount}**개의 메시지를 지웠습니다.")
        except ValueError:
            await ctx.send("청소하실 메시지의 **수**를 입력해 주세요.")
    else:
        await ctx.send("당신은 권한이 없기 때문에 이 명령어를 사용할 수 없습니다")

@app.command(pass_context=True)
async def rn(ctx, num1, num2):
    try:
        picked = random.randint(int(num1), int(num2))
        await ctx.send(f'뽑힌 숫자는 **{str(picked)}** 입니다')
    except IndexError:
        await ctx.send("무슨 숫자를 뽑을지 알려주세요")
    except ValueError:
        await ctx.channel.send("정수를 입력해주세요")
    except ZeroDivisionError:
        await ctx.channel.send("0으로 나눌 수 없습니다")

@app.command(pass_context=True)
async def randomnumber(ctx, n1, n2):
    try:
        pickled = random.randint(int(n1), int(n2))
        await ctx.send(f'뽑힌 숫자는 **{str(pickled)}** 입니다')
    except IndexError:
        await ctx.send("무슨 숫자를 뽑을지 알려주세요")
    except ValueError:
        await ctx.channel.send("정수를 입력해주세요")
    except ZeroDivisionError:
        await ctx.channel.send("0으로 나눌 수 없습니다")

@app.command(name="role", pass_context=True)
async def _Puresoul(ctx, role, member : discord.Member=None):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            member = member or ctx.message.author
            await member.add_roles(get(ctx.guild.roles, name=role))
            await ctx.channel.send(str(member)+"에게 역할이 적용되었습니다.")
        except:
            await ctx.channel.send("뭘 잘못 쳤는진 모르겠지만 쨌든 제대로 입력좀")
    else:
        await ctx.channel.send("당신은 권한이 없기 때문에 이 명령어를 사용할 수 없습니다")

@app.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Solindy Bot Help", description="솔린디 봇 도움말", color=0x00aaaa)
    embed.add_field(name="1. `!sb dm <할 말>`", value=" - 전체 DM 공지를 보냅니다", inline=False)
    embed.add_field(name="2. `!sb clean <숫자>`", value=" - 정한 숫자만큼 밑에서부터 메세지를 삭제합니다", inline=False)
    embed.add_field(name="3. `!sb role <역할 이름> <유저 멘션>`", value=" - 멘션한 유저에게 해당 역할을 지급합니다", inline=False)
    embed.add_field(name="4. `!sb randomnumber/rn <숫자 1> <숫자 2>`", value=" - <숫자 1> 에서 설정한 숫자부터 설정한 <숫자 2> 에서 설정한 숫자까지 랜덤으로 하나의 숫자를 뽑습니다", inline=False)
    embed.add_field(name="5. `!sb help`", value=" - 현재 도움말 창을 출력합니다", inline=False)
    await ctx.channel.send(embed=embed)
    


access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
