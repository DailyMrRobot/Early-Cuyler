import os
import random
import discord
import requests
import json
import youtube_dl
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord import client

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)





load_dotenv()
TOKEN = os.getenv('OTA1MTExMjQ1MjYxMjU0NjU3.YYFUiQ.kiDuMBZLYeRlHOsT3m2csJS-rAM')

bot = commands.Bot(command_prefix='!')

@bot.command(name='Early')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "Wooh!",
        "I dont netflix and chill...I VHS & F**K",
        "Get off my ass demon love, douse the pain!",
        "Santa Claus is dead!",
        "See if that sum bitch'll fax now!",
        "We can take five if y'all need to get busy.",
        "Aw Granny, rape is illegal in these parts. Ask me how I know. Go on, ask me one time how I know... It's a long story, but a colorful one... how is it rape when they're dead? Talk about a victimless crime!",
        "Early Cuyler, babeh! WHOO!",
        "Play that note again, the low pitchy one, you know the one! There you go, thats the one, that is pissing me off!",
        "That's the closest damn thing to a birthday party you'll ever get!",
        "I care not to consort with the roboty race",
        "I'm the best there ever was!",
        "Alright, you corny sum'bitch, the revolution starts right now!",
        "Do not touch the trim!",
        "I am gonna jimmy-jack them speakers!",
        "I'm as firm as red clay and as constant as... drinkin'. I'm constantly drinkin'.",
        "If it walks like a duck, talks like a duck, den shoot that lying summa' bitchen goose and suppa' down!",
        "Whoo! I win! I WIN! Whoo! Heall yeah!! That was a thinkin' man's victory there!",
        "You know how much that coffin cost, woman? You goin' in the damn ground!",
        "Allow me to explain the contamination process. Pine cones go in here, party liquors comes out here and proceed to here. Fights begin, finger prints are took, days is lost, bail is made, court dates are ignored, cycle is repeated.",
        "Readin' don't never not done nothing for not nonebody. Never not no one, didn't about no reason not never. And by God they never not ain't gonna will!",
        "Why have the sequel when you can have the prequel? The prequel is unequel!",
        "She got the holler heart of a bitch.",
        "Go get you some, Reverend! She's in heat!",
        "But some other crazy sum'bitch is the one what bangulated and pregnified that white woman. Not I.",
        "She was enormous and Lord, did I loved her. For 32 frenetic seconds. Ugh, ugh, ugh, the lovin' was good!",
        "Russell, you need to respectify your Aunt Lil. She ain't some dumb, dirty-ass whore you can trash down like your mama.",
        "Nu-uh. Pick it up with ya buttcheeks!",
        "Oh, I see. Just stalkin' for now, huh? Now don't you be textin' threats, 'cause the police can trace that. If you you got something to say to her you best carve it into a dog's fur with a boxcutter.",
        "Come on nah, thunderbuns. Whoo! The dumplin' is mine!",
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
@bot.command(name='hat')
async def hat(ctx):
    hat_names = ['Booty Hunter',
    'Lifeguard On Booty',
    'Groom',
    'Free Hat Limit 1',
    'Nice Legs, What Time They Open?',
    'Tell Your Titties To Stop Staring At My Eyes!',    
    "I'm Did Asbestos I Can",
    "Too Funk To Druck",
    "I ♡ Cock Fighting",
    "Hold My Hat While I Have Sex With Your Wife",
    "Rock Out With Your Jock Out Daytona Beach 1986",
    "No Habla Jibber Jabber",
    "Breath If You're Horny",
    "Divorce Is Strong With This One",
     "The Big E",

    ]
    response = random.choice(hat_names)
    await ctx.send(response)

@bot.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Rumbling.wav')
        player = voice.play(source)
    else:
        await ctx.send("Boy, get your ass in a voice channel before I whup that ass!")

@bot.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I done did left that bitch you feel me?")
    else:
        await ctx.send("I aint in a voice channel if your dumbass aint in there boy.")       






    

bot.run('')
