from discord.ext import commands

from embed_templator import Embed

token = 'ODc4MzI5MjQ2MDg5NjEzNDEy.YR_l2g.h2Utz5JhsZNF9ITXM0FDj3ZsSow'
client = commands.Bot(command_prefix=',')

Embed.load(client, auto_author=True)


@client.command()
async def embed_example(ctx):
    await ctx.send(embed=Embed(ctx))


@client.command()
async def ping(ctx):
    await ctx.send(embed=Embed(ctx)(description='pong!'))

client.run(token)
