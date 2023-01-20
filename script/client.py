import discord
import data
from discord import option
from ai import requestAI
description = 'A bot that does stuff.'
token = 'MTA1MTYwNTg4OTcyNDk3MzE0Nw.GW3TIP.4qhCn-YbTm4NALurtyqwKVe6VTkbGrxKRY5qfs'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Bot(command_prefix='/', description=description, intents=intents)

#Request response from AI
@bot.slash_command(name="ai")
@option(
    "prompt",
    str,
    description="Enter your prompt here"
)
async def ai(ctx, message : str):
    await ctx.respond(requestAI(message, data.read_record(ctx.guild.id)[0][1], data.read_record(ctx.guild.id)[0][2]))

#Set API key
@bot.slash_command(name="setkey")
@option(
    "key",
    str,
    description="Enter your API key"
)
async def setkey(ctx, key : str):
    #Check if user is an admin
    if not ctx.author.guild_permissions.administrator:
        await ctx.respond("You do not have permission to use this command.")
        return
    data.update_record(ctx.guild.id, key, data.read_record(ctx.guild.id)[0][2])
    await ctx.respond("API key has been set.")
#Set token
@bot.slash_command(name="settoken")
@option(
    "token",
    str,
    description="Enter your token"
)
async def settoken(ctx, token : str):
    #rCheck if user is an admin
    if not ctx.author.guild_permissions.administrator:
        await ctx.respond("You do not have permission to use this command.")
        return
    #Check if token is a number
    if not token.isnumeric():
        await ctx.respond("Token must be a number.")
        return
    data.update_record(ctx.guild.id, data.read_record(ctx.guild.id)[0][1], token)
    await ctx.respond("Token has been set.")
#Create a record for the guild on bot join event
@bot.event
async def on_guild_join(guild):
    data.insert_record(guild.id, "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", 500)
    print("Record created for " + guild.name)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(token)