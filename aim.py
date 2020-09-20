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
    cmd = ctx.message.content[9:]
    if cmd == "":
        embed = discord.Embed(title="Solindy Bot Help", description="솔린디 봇 도움말", color=0x00aaaa)
        embed.add_field(name="관리자 전용", value=" `!sb dm` `!sb clean` `!sb role`", inline=False)
        embed.add_field(name="기본",  value=" `!sb rn` \n ", inline=False)
        embed.add_field(name="명령어는 추후 추가될 수 있습니다", value="\n `!sb help <명령어>` 명령어를 통해 명령어의 상세정보를 확인할 수 있습니다", inline=False)
        await ctx.channel.send(embed=embed)
    elif cmd == "dm":
        embed = discord.Embed(title="명령어 - DM", description="<할 말> 에 쓰여있는 말로 전체 DM 공지를 보냅니다", color=0x00aaaa)
        embed.add_field(name="사용법", value="`!sb dm <할 말>`")
        await ctx.channel.send(embed=embed)
    elif cmd == "clean":
        embed = discord.Embed(title="명령어 - clean", description="<숫자> 에 쓰여있는 숫자만큼 밑에서부터 메시지를 삭제합니다", color=0x00aaaa)
        embed.add_field(name="사용법", value="`!sb clean <숫자>`")
        await ctx.channel.send(embed=embed)
    elif cmd == "role":
        embed = discord.Embed(title="명령어 - role", description="설정한 역할을 멘션한 유저에게 적용합니다", color=0x00aaaa)
        embed.add_field(name="사용법", value="`!sb role <역할 이름> <유저 멘션>`")
        await ctx.channel.send(embed=embed)
    elif cmd == "randomnumber":
        embed = discord.Embed(title="명령어 - RandomNumber", description="설정한 숫자의 범위 안에서 랜덤한 숫자를 하나 뽑습니다", color=0x00aaaa)
        embed.add_field(name="사용법", value="`!sb randomnumber/rn <숫자 1> <숫자 2>`")
        await ctx.channel.send(embed=embed)
    elif cmd == "rn":
        embed = discord.Embed(title="명령어 - RandomNumber", description="설정한 숫자의 범위 안에서 랜덤한 숫자를 하나 뽑습니다", color=0x00aaaa)
        embed.add_field(name="사용법", value="`!sb randomnumber/rn <숫자 1> <숫자 2>`")
        await ctx.channel.send(embed=embed)
    else:
        await ctx.channel.send("상세정보를 확인할 명령어를 입력해주세요")

@app.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("값을 입력해주세요")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("값이 다릅니다")
    else:
        embed = discord.Embed(title="오류가 발생했습니다", description=" ", color=0xFF0000)
        embed.add_field(name="상세", value=f"```{error}```")
        await ctx.send(embed=embed)
    


access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
