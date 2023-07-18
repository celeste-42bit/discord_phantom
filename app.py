import logger
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.reactions = True

follow = False   # Should the bot follow the chat? Overridden, if record is set to true
record = True  # Should the bot record the chat?

if record:
    follow = True
        
description = 'The Phantom by "The Phantasm Bot Projects"'                                  # The bots 'about me'
status = discord.Status.online                                                              # The bots status (The dot on the profile picture)
activity = discord.Activity(type=discord.ActivityType.watching, name="over the Phantasm")   # The bots activity (The text under its name)
        
client = commands.Bot(
    command_prefix='/',
    intents = intents,
    description = description,
    status=status,
    activity=activity,
    case_insensitive=True
    )

@client.event
async def on_ready():
    print(f'I logged in as {client.user} (ID: {client.user.id}). At your service, mistress!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    concat = f'At [{message.created_at}] [{message.author.name}] wrote: {message.content}'
    
    if follow:
        print(concat)
    if message.content.__contains__("/") or record:
        logger.log(concat);
    

with open('.token', 'r') as tkn:
    token = str(tkn.read())
client.run(token)