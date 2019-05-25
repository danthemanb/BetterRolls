import discord
import os
import sys
import errno
from discord.ext import commands
from BetterRolls import GodlikeRoll
from BetterRolls import Macros

TOKEN = 'NTc1NTExODA4MTk1MDM1MTM2.XOHzmQ.4j0mPP3AYqpO1932s_dfo4R5NLk'

#client = discord.Client()
client = commands.Bot(command_prefix = ',')

#client._skip_check = lambda a,b:False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()      #could make a command hidden, could give an alias
async def ping(ctx):        #ctx stands for context and is sent in automatically
    await ctx.send(f'pong: {round(client.latency*1000)}ms')

@client.command(aliases=['r', 'R', 'Roll', 'ROLL'])
async def roll(ctx, *argv):
    dice = GodlikeRoll.BetterGRoll()
    rolls = dice.parse(argv)
    if(not rolls):
        await ctx.send("Invalid Format! Usage -- r[oll] dice [dice...]\nDice can be formatted as normal(d), hard(h), or wiggle(w) in the format of {Quantity}d{Size}\nFor Normal and Wiggle dice, Size must equal 10 or be left empty.")
        return None
    out = dice.Calc(rolls)
    await ctx.send(out)


@client.command(aliases=['exit'])      #could make a command hidden, could give an alias
async def quit(ctx):        #ctx stands for context and is sent in automatically
    await ctx.send("Goodbye")
    sys.exit(0)

@client.command()      #could make a command hidden, could give an alias
async def test(ctx):        #ctx stands for context and is sent in automatically
    #ctx.invoke(roll)
    await ctx.send(",ping")

@client.command(aliases=['makemacro', 'MAKEMACRO', 'MakeMacro', 'mm', 'MM'])      #could make a command hidden, could give an alias
async def makeMacro(ctx, *argv):        #ctx stands for context and is sent in automatically
    usrhash = str(hash(ctx.message.author))
    if ( len(argv) < 2):
        await ctx.send("Invalid Format! Usage -- ,MakeMacro MacroName Command")
        return
    status = Macros.create(usrhash, argv)
    if status:
        await ctx.send("Invalid Format! Usage -- ,MakeMacro MacroName Command")

@client.command(aliases=['deletemacro', 'DELETEMACRO', 'DeleteMacro', 'dm', 'DM'])      #could make a command hidden, could give an alias
async def deleteMacro(ctx, cmdName):        #ctx stands for context and is sent in automatically
    usrhash = str(hash(ctx.message.author))
    status = Macros.delete(usrhash, cmdName)
    if status:
        await ctx.send("Invalid Format! Usage -- ,DeleteMacro MacroName")

@client.command(aliases=['Macro', 'MACRO', 'm', 'M'])      #could make a command hidden, could give an alias
async def macro(ctx, cmdName):        #ctx stands for context and is sent in automatically
    usrhash = str(hash(ctx.message.author))
    cmd = Macros.get(usrhash, cmdName)
    if cmd:
        #await ctx.send(cmd)
        #async def roll(ctx, *argv):
        dice = GodlikeRoll.BetterGRoll()
        rolls = dice.parse(cmd)
        if(not rolls):
            await ctx.send("Invalid Format! Usage -- r[oll] dice [dice...]\nDice can be formatted as normal(d), hard(h), or wiggle(w) in the format of {Quantity}d{Size}\nFor Normal and Wiggle dice, Size must equal 10 or be left empty.")
            return None
        out = dice.Calc(rolls)
        await ctx.send(out)
    else:
        await ctx.send("Invalid Macro")

client.run(TOKEN)
