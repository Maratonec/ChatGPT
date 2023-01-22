import discord
import data
from discord import option
from ai import requestAI
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
description = "ChatGPT is a Discord bot that uses OpenAI\'s GPT-3 API to generate responses to user prompts."
token = os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True



bot = discord.Bot(command_prefix='/', description=description, intents=intents)

#Help
@bot.slash_command(name="help")
async def help(ctx):
    embed = discord.Embed(title="ChatGPT", description="ChatGPT is a Discord bot that uses OpenAI\'s GPT-3 API to generate responses to user prompts.", color=0x00ff00)
    embed.add_field(name="/ai", value="Generate a response to your prompt.", inline=False)
    embed.add_field(name="/setkey", value="Set your API key.", inline=False)
    embed.add_field(name="/settoken", value="Set the maximum number of tokens that the AI will generate.", inline=False)
    embed.add_field(name="/help", value="Show this message.", inline=False)

    await ctx.send(embed=embed)


#Request response from AI
@bot.slash_command(name="ai")
@option(
    "prompt",
    str,
    description="Enter your prompt here"
)
async def ai(ctx, message : str):
    #If no API key is set
    if data.read_record(ctx.guild.id)[0][1] == "invalid":
        await ctx.respond("No API key has been set. Please use /setkey to set your API key.")
        return
    await ctx.response.defer()
    await ctx.followup.send(requestAI(message, data.read_record(ctx.guild.id)[0][1], data.read_record(ctx.guild.id)[0][2]))

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
        await ctx.respond("You do not have permission to use this command. Please contact an administrator.")
        return
    data.update_record(ctx.guild.id, key, data.read_record(ctx.guild.id)[0][2])
    await ctx.respond("API key has been set. ")
#Set token
@bot.slash_command(name="settoken")
@option(
    "token",
    str,
    description="Enter your token"
)
async def settoken(ctx, token : str):
    #Check if user is an admin
    if not ctx.author.guild_permissions.administrator:
        await ctx.respond("You do not have permission to use this command. Please contact an administrator. ")
        return
    #Check if token is a number
    if not token.isnumeric():
        await ctx.respond("Token must be a number. Please try again. Example: /settoken 500. This will set the token to 500.")
        return
    data.update_record(ctx.guild.id, data.read_record(ctx.guild.id)[0][1], token)
    await ctx.respond("Token has been set. Please note that the token is the maximum number of tokens that the AI will generate. If you set the token to 500, the AI will generate a maximum of 500 tokens. ")
    
#Create a record for the guild on bot join event
@bot.event
async def on_guild_join(guild):
    data.insert_record(guild.id, "invalid", 500)
    #write welcome message to chat
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Thanks for inviting me to your server! Please use /setkey to set your API key. Without an API key, the bot will not work. You can get an API key from https://beta.openai.com/account/api-keys. You can also use /settoken to set the token. The token is the maximum number of tokens that the AI will generate. If you set the token to 500, the AI will generate a maximum of 500 tokens.")
            break
    print("Record created for " + guild.name)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for guild in bot.guilds:
        if data.read_record(guild.id) == []:
            data.insert_record(guild.id, "invalid", 500)

#Error handler for ai command
@ai.error
async def ai_error(ctx, error):
    #Respond with error message specified in the error handler
    await ctx.send(error)



bot.run(token)