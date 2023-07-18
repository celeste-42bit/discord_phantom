import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.reactions = False
        
description = "The Phantom by 'The Phantasm Bot Projects'"
        
bot = commands.Bot(intents = intents, description = description, command_prefix='/', debug_guild=1090933390007615551)
        
with open('.token', 'r') as tkn:
    token = str(tkn.read())
bot.run(token)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.CustomActivity(name="Type /help"))
    print(f'I logged in as {bot.user} (ID: {bot.user.id})')