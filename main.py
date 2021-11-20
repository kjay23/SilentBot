# SilentBot

## Replit Properties, uncomment the next line if you want to host your bot other than replit.
from webserver import keep_alive

## Discord.py stuffs, requirement things
import discord, asyncio, os, platform, sys
from discord.ext.commands import Bot
from discord.ext import commands

## Some random response support
import random

## Bot configuration, eh?
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

## AI witty bot response, get your own token here:
from prsaw import RandomStuff

## Discord Intents stuffs
"""	
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://discordpy.readthedocs.io/en/latest/intents.html
https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents


Default Intents:
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.emojis = True
intents.bans = True
intents.guild_typing = False
intents.typing = False
intents.dm_messages = False
intents.dm_reactions = False
intents.dm_typing = False
intents.guild_messages = True
intents.guild_reactions = True
intents.integrations = True
intents.invites = True
intents.voice_states = False
intents.webhooks = False

Privileged Intents (Needs to be enabled on dev page):
intents.presences = True
intents.members = True
"""

intents = discord.Intents.all()

## Hmmm prefixes, edit on config.py than here!
bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents)


## The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

    await bot.change_presence(status=discord.Status.idle)

## Setup the game status task of the bot
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Minecraft of course!"))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("with Cyanide."))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("Music feature will be re-writing it again."))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("with humans!"))
        await asyncio.sleep(3)

## Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")

## Cogs, some stuffs like commands
if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

## AI witty chatbot ahiii
api_key = config.AI_KEY
rs = RandomStuff(async_mode=True, api_key = api_key)

## The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
        if bot.user == message.author:
          return

    # Ignores if a command is being executed by a blacklisted user
    if message.author.id in config.BLACKLIST:
        return
    await bot.process_commands(message)

    r = await rs.get_ai_response(message.content)


## And the war begins...
# sIlEnt HEY - camelcase words will not respond
    if message.content.startswith('hey silent'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('Hey Silent'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('hey Silent'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('HEY SILENT'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

# Paul something HEY
    if message.content.startswith('hey paul'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('Hey Paul'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('hey Paul'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('HEY PAUL'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

# without hey -silent
    if message.content.startswith('silent'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('Silent'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('SILENT'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

# paul without hey
    if message.content.startswith('paul'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('Paul'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('PAUL'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

# PPPPOOOOOOLLLL HAHAHAHAHAHAA
    if message.content.startswith('hey pool'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('Hey Pool'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('hey Pool'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('HEY POOL'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

# PPPPOOOOOOLLLL without hey HAHAHAHAHAHAA
    if message.content.startswith('pool'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('Pool'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('POOL'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

# compatibility stuffs    
    if message.content.startswith('@Silent Bot'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)

    if message.content.startswith('@Paul'):
        response = merge_dicts(r)
        await message.reply(response['message'])
        await bot.process.commands(message)


#working area

# Dieeee
    if 'die' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

    if 'dead' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

    if 'died' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

    if 'kms' in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/780620475742158889/873401628429021205/828657219091431434.gif")

    if 'pool' in message.content.lower():
      await message.channel.send('Can you not?')

    if 'Pool' in message.content.lower():
      await message.channel.send('I acknowledge you that there is no need to bully my name. Thanks!')

## friendship status

    aa = [
  "I don't know.",
  "I am your friend, just a good friend my man.",
  "I am your mom. Problems?",
  "I am living on the internet and what if I'm a human?",
  "You are my dog.\nWoof woof! :service_dog:",
  "A Minecraft player, anything else?",
  "As a bot, It's really dumb to ask something like that. <:disgust:862897347540811776>",
  "Rage quitter, why not?",
  "The owner of new unclaimed nuclear plant.",
  "Not in a good mood right now. Try ask me again.",
  "Try to ask <@440892659264126997> if she's good or being witty.",
  "Ask your parents.\n<:cheeze:862892425877913600>",
  "The one who stole your heart. <:kekwyou:862893918584176640>",
  "I am your husband. <:KEKW:867620478633377802>",
  "I am <@!420554438206554113>'s adopted rat. Sorry for ping, Dad.",
  "https://tenor.com/view/vegeta-dragonballsuper-dragonball-meme-language-of-gods-gif-14707991",
  "You are my inspiration.",
  "Bruh"
       ]

    if message.content.startswith('<@!870263071002738718>'):
      if message.content.endswith('ho are you?'):
        aa = random.choice(aa)
        await message.channel.send(aa)

    if message.content.startswith('<@!870263071002738718>'):
      if message.content.endswith('ho are you'):
        aa = random.choice(aa)
        await message.channel.send(aa)

    if message.content.startswith('<@!870263071002738718>'):
      if message.content.endswith('ho r u?'):
        aa = random.choice(aa)
        await message.channel.send(aa)

    if message.content.startswith('<@!870263071002738718>'):
      if message.content.endswith('ho r u'):
        aa = random.choice(aa)
        await message.channel.send(aa)


    if message.content.startswith('<@!870263071002738718>'):
      if "hat is" in message.content.lower():
        await message.channel.send("I don't know.")



## you there

    ab = [
      "I'm here, behind you pleb.",
      "In the bathroom, please wait.",
      "Maybe?",
      "I guess you saw me earlier, right?"
      "I don't think so.",
      "I'm about to die."
      ]

    if message.content.startswith('<@!870263071002738718>'):
      if "you there" in message.content.lower():
        ab = random.choice(ab)
        await message.channel.send(ab)

## doing some things

    ac = [
      "Doing my homework, how about you?",
      "Playing Minecraft. Talk to you later.",
      "Spying your messages.",
      "Calm for a sex.\nI mean, sec. Just a typo silly. <:pepedumb:862899244885082153>",
      "Online class. **AAAAAAAAAAAAAAAAAAAAA** <:brainfuck:862901059789258822>",
      "Uh nothing. I guess?",
      "Crunching noobs. Anything else?",
      "Bored. I don't know what to do."
      ]

    if message.content.startswith('<@!870263071002738718>'):
      if "u doin" in message.content.lower():
        ac = random.choice(ac)
        await message.channel.send(ac)

## beg lmao
    ad = [
      "RIP, I won't.",
      "Aww what a beggar man.",
      "Son of beggar L",
      "Hats off.",
      "What if I don't?",
      "L nah.",
      "Go ask your mom than me."
      ]

    if message.content.startswith('<@!870263071002738718>'):
      if "gimme" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "give me" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "can I" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "can i" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)

    if "ill you" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)
        
    if "ill u" in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)
        
    if "may " in message.content.lower():
        ad = random.choice(ad)
        await message.channel.send(ad)
        
## nou

    ae = [
      "No, you.",
      "Nou.",
      "UNO!",
      "<:nou:871682805686468669>",
      "https://tenor.com/view/confused-what-nigga-please-really-loop-gif-4966361"

      ]

    if message.content.startswith('<@!870263071002738718>'):
      if "nou" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)

    if "no, you" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)
        
    if "no, you" in message.content.lower():
        ae = random.choice(ae)    
        await message.channel.send(ae)
        
    if "no u" in message.content.lower():
        ae = random.choice(ae)
        await message.channel.send(ae)

    if message.content.endswith("umb"):
      ae = random.choice(ae)
      await message.channel.send(ae)  

    if "stupid" in message.content.lower():
      ae = random.choice(ae)
      await message.channel.send(ae)

    if "fuck" in message.content.lower():
      ae = random.choice(ae)
      await message.channel.send(ae)

## answer meeeee

    af = [
        "What if I don't?",
        "What is it?",
        "Shut down please.\n I mean up.",
        "What do you mean?",
        "Maybe I'm out of words to say. Try again and I'll mark your words."
      ]

    if message.content.startswith('<@!870263071002738718>'):
      if "swer me" in message.content.lower():
        af = random.choice(af)
        await message.channel.send(af)

## why not
    ag = [
        "Why not?",
        "Because yes.",
        "Because no.",
        "¯\_(ツ)_/¯"
      ]

    if message.content.startswith('<@!870263071002738718>'):
       if message.content.endswith('why'):
        ag = random.choice(ag)
        await message.channel.send(ag)

    if message.content.endswith('why?'):
        ag = random.choice(ag)
        await message.channel.send(ag)
        
## play something

    ah = [
        "Minecraft?",
        "Can't play right now."
      ]

    if message.content.startswith('<@!870263071002738718>'):
        if "lets play" in message.content.lower():
          ah = random.choice(ah)
          await message.channel.send(ah)

        if "let's play" in message.content.lower():
          ah = random.choice(ah)
          await message.channel.send(ah)


## nothing ig
    ai = [
        "Okay.",
        "Impossible. Just tell me what is it.",
        "Why it would be nothing?",
        "*Lies*"
     ]

    if message.content.startswith('<@!870263071002738718>'):
      if "nothing" in message.content.lower():
        ai = random.choice(ai)
        await message.channel.send(ai)
        
## yes no maybe
    aj = [
        "Alright.",
        "Mhmm?",
        "So what is it?"
      ]

    if message.content.startswith('<@!870263071002738718>'):
      if message.content.endswith("no"):
        aj = random.choice(aj)
        await message.channel.send(aj)

    if "nope" in message.content.lower():
      aj = random.choice(aj)
      await message.channel.send(aj)

    if "maybe" in message.content.lower():
      aj = random.choice(aj)
      await message.channel.send(aj)

    if "date me " in message.content.lower():
      aj = random.choice(aj)
      await message.channel.send(aj)


# Poll command fix
    if message.content.startswith("s!poll"):
      await message.delete()

    if message.content.startswith("!poll"):
      await message.delete()


def merge_dicts(l):
  if len(l) == 1:
    return l[0]
  return {**l[0], **merge_dicts(l[1:])}



@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")

# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="Error!",
            description="This command is on a %.2fs cool down" % error.retry_after,
            color=config.error
        )
        await context.send(embed=embed)
    raise error
   

## Uncomment down below if you are using replit
keep_alive()

# Run the bot with the token
bot.run(config.TOKEN)


## That's it? KEKW
