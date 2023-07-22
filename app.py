import discord, logger, random
from discord.ext import commands


intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.reactions = True

follow = True   # Should the bot follow the chat? Overridden, if record is set to true
record = False  # Should the bot record the chat?

if record:
    follow = True
        
description = 'The Phantom by "The Phantasm Bot Projects"'                                  # The bots description (This appears in the default help page)
status = discord.Status.online                                                              # The bots status (The dot on the profile picture)
activity = discord.Activity(type=discord.ActivityType.watching, name="over the Phantasm")   # The bots activity (The text under its name)
shard_id = 0                                                                                # Shard ID
shard_count = 2                                                                             # Total number of shards
        
client = commands.Bot(
    command_prefix='/',
    intents = intents,
    description = description,
    help_command=commands.DefaultHelpCommand(),
    status=status,
    activity=activity,
    case_insensitive=True,
    shard_id = shard_id,
    shard_count = shard_count
    )

@client.event
async def on_ready():
    print(f'I logged in as {client.user} (ID: {client.user.id}). At your service, mistress!')

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

    await ctx.send(str(concat))

def roll_the_dice():
    roll = random.randint(1, 10)  # roll a d10
    match roll:  # match to all possible dice states
        case 1:
            return 0  # total failure
        case 10:
            return 3  # critical success
        case x if x > 5:
            return 2  # success
        case x if x < 5:
            return 1  # failure

@client.command(name='hi', brief='Check whether the bot is available', help='Usage: /hi')
async def hi(ctx):
    await ctx.send(f'Heyo, {ctx.author.name}!')

with open('.token', 'r') as tkn:
    token = str(tkn.read())
client.run(token)