import discord
from discord.ext import commands
from ai import requestAI
description = 'A bot that does stuff.'
token = 'MTA1MTYwNTg4OTcyNDk3MzE0Nw.GW3TIP.4qhCn-YbTm4NALurtyqwKVe6VTkbGrxKRY5qfs'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
@bot.command()
async def ai(ctx, message : str):
    await ctx.send(requestAI(message))
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
bot.run(token)