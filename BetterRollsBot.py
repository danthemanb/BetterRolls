import discord
import os
import errno
from discord.ext import commands
import BetterRollsClass


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
    dice = BetterRollsClass.BetterGRoll()
    rolls = dice.parse(argv)
    if(not rolls):
        await ctx.send("Invalid Format! Usage -- ")
        return None
    dice.rollDice(rolls)
    await ctx.send(f'You Rolled {dice.diceList} and have {dice.wiggle} wiggle dice!')

client.run(TOKEN)
