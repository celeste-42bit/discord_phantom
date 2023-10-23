import discord, logger, random
from discord.ext import commands


intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.reactions = True

follow = True   # Should the bot follow the chat? Overridden, if 'record' is set to true
record = False  # Should the bot record the chat? (Please comply with national data protection laws!)

if record:
    follow = True

'''These are the most commonly changed settings/presets
    
'''
description = 'The Phantom by "The Phantasm Bot Projects"'                                  # The bots description (This appears in the default help page)
status = discord.Status.online                                                              # The bots status (The dot on the profile picture)
activity = discord.Activity(type=discord.ActivityType.watching, name="over the Phantasm")   # The bots activity (The text under its name)
shard_id = 0                                                                                # Shard ID
shard_count = 1                                                                             # Total number of shards

'''Definition of the "client" object - this definition contains almost all settings

'''
client = commands.Bot(
    command_prefix='/',
    intents = intents,
    description = description,
    help_command=commands.DefaultHelpCommand(),  # TODO: Find out how to auto-display DefaultHelp...
    status=status,
    activity=activity,
    case_insensitive=True,
    shard_id = shard_id,
    shard_count = shard_count
    )

@client.event
async def on_ready():
    print(f'I logged in as {client.user} (ID: {client.user.id}). At your service, mistress!')
    # log this event w/ time


'''on_message function - This function is commented out, since it is blocking command execution. Refer to GitHub issue #1 https://github.com/celeste-42bit/discord_phantom/issues/1 
@client.event()
async def on_message(message):
    if message.author == client.user:
        return
    
    concat = f'At [{message.created_at}] [{message.author.name}] wrote: {message.content}'  # This is a concat 🐈
    
    if follow:
        print(concat)
    if message.content.__contains__("/") or record:
        logger.log(concat);
'''

@client.command(name='roll', brief='Roll the dice!', help='Usage: /roll <dice ammount> <hunger>')
async def roll(ctx, num_dice, hunger):
    # TODO: make sure this is set up in the server...
    # TODO: is there a list-way of doing this shit lmao?!?!?!?!?!
    tf = discord.utils.get(ctx.guild.emojis, name='total_failure')
    f = discord.utils.get(ctx.guild.emojis, name='failure')
    s = discord.utils.get(ctx.guild.emojis, name='success')
    cs = discord.utils.get(ctx.guild.emojis, name='critical_success')
    htf = discord.utils.get(ctx.guild.emojis, name='hunger_total_failure')
    hf = discord.utils.get(ctx.guild.emojis, name='hunger_failure')
    hs = discord.utils.get(ctx.guild.emojis, name='hunger_success')
    hcs = discord.utils.get(ctx.guild.emojis, name='hunger_critical_success')
    dice = []
    concat = []
    for i in range(int(num_dice)):
        dice.append(roll_the_dice())
    for i in range(int(num_dice)):
        match dice[i]:
            case 0:
                concat.append(tf)
            case 1:
                concat.append(f)
            case 2:
                concat.append(s)
            case 3: concat.append(cs)

# TODO: To display hunger, get hunger value && sign last list objects as negative.
# Then check for the negative values to display hunger dice

    await ctx.send(str(concat))  # this sends the list into tha chat

# TODO: Implement dice-display algo (replace every list object with the acc. dice-emoji concatted into a chat message)

def roll_the_dice():  # main dice algo
    roll = random.randint(1, 10)  # roll a d10
    match roll:  # match to all possible dice states
        case 1:
            return 0  # total failure (1/10)
        case 10:
            return 3  # critical success (1/10)
        case x if x > 5:
            return 2  # success (4/10)
        case x if x < 5:
            return 1  # failure (4/10)

def roll_the_dice_cursed():  # cursed dice algo (haxx)...
    roll = random.randint(0, 3)  # roll 1 of 5 ints, give crit and total failure 1/5 chance
    match roll:
        case 0:
            return 0  # tf (1/4)
        case 3:
            return 3  # cs (1/4)
        case 2:
            return 2  # s (1/4)
        case 1:
            return 1  # f (1/4)

@client.command(name='hi', brief='Check whether the bot is available', help='Usage: /hi')
async def hi(ctx):
    await ctx.send(f'Heyo, {ctx.author.name}!')

with open('.token', 'r') as tkn:
    token = str(tkn.read())
client.run(token)