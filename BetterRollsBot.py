import discord
import os
import sys
import errno
from discord.ext import commands
from BetterRolls import GodlikeRoll

TOKEN = 'NTc1NTExODA4MTk1MDM1MTM2.XOHzmQ.4j0mPP3AYqpO1932s_dfo4R5NLk'

#client = discord.Client()
client = commands.Bot(command_prefix = ',')

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
    #await ctx.send(f'You Rolled {dice.diceList} and have {dice.wiggle} wiggle dice!')
    await ctx.send(out)

@client.command(aliases=['makemacro', 'MAKEMACRO', 'MakeMacro', 'mm', 'MM'])      #could make a command hidden, could give an alias
async def makeMacro(ctx, *argv):        #ctx stands for context and is sent in automatically
    usrhash = hash(ctx.message.author)
    status = create(usrhash, *argv)


@client.command(aliases=['exit'])      #could make a command hidden, could give an alias
async def quit(ctx):        #ctx stands for context and is sent in automatically
    await ctx.send("Goodbye")
    sys.exit(0)

'''
@client.command()      #could make a command hidden, could give an alias
async def help(ctx):        #ctx stands for context and is sent in automatically
    await ctx.send("Current Commands listing: ping, roll, exit")
'''
client.run(TOKEN)
