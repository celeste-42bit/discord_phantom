import discord
from discord.ext import commands

# This class is supposed to connect and lauch the bot and to provide data such as users currently online,
# name of the server, name of channels, etc. for the rest of the program

class Phantom():
    def __init__(self):
        intents = discord.Intents.default()
        intents.typing = True
        intents.presences = False
        intents.message_content = True
        intents.reactions = True
        
        description = '''This is the production version of "The Phantom"'''
        
        bot = commands.Bot(intents = intents, description = description, command_prefix='@The Phantom')
        
        with open('.token', 'r') as tkn:
            token = str(tkn.read())
        bot.run(token)
        
        @bot.event
        async def on_ready():
            print(f'I logged in as {bot.user} (ID: {bot.user.id})')
  
if __name__ == '__main__':  # This prevents direct uncontrolled launch of this class
    Phantom().__init__()  # init is unnecessary here, since this is the constructor, which will be called anyways...
else:
    print('Don`t awaken the phantom!')