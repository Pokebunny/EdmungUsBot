import os
import random
import time
from typing import Sequence

import discord
from nltk.corpus import wordnet as wn
from discord.ext import commands
from dotenv import load_dotenv
import datetime

load_dotenv()
TOKEN = os.getenv("EDMUNGBOT_TOKEN")

default_multipoll_emojis = ["🍏", "🤨", "🥶", "🚫"]

bot = commands.Bot(command_prefix='!')

nouns = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [], "l": [],
         "m": [], "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [], "w": [], "x": [],
         "y": [], "z": []}
verbs = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [], "l": [],
         "m": [], "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [], "w": [], "x": [],
         "y": [], "z": []}
adjectives = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [],
              "l": [], "m": [], "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [],
              "w": [], "x": [], "y": [], "z": []}
adverbs = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [],
           "l": [], "m": [], "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [],
           "w": [], "x": [], "y": [], "z": []}

for synset in list(wn.all_synsets("n")):
    if synset.name()[0] != ".":
        word = synset.name().split(".")[0]
        if "_" not in word and word[0].isalpha():
            nouns[word[0]].append(word)

for synset in list(wn.all_synsets("v")):
    if synset.name()[0] != ".":
        word = synset.name().split(".")[0]
        if "_" not in word and word[0].isalpha():
            verbs[word[0]].append(word)

for synset in list(wn.all_synsets("a")):
    if synset.name()[0] != ".":
        word = synset.name().split(".")[0]
        if "_" not in word and word[0].isalpha():
            adjectives[word[0]].append(word)

for synset in list(wn.all_synsets("r")):
    if synset.name()[0] != ".":
        word = synset.name().split(".")[0]
        if "_" not in word and word[0].isalpha():
            adverbs[word[0]].append(word)


@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author.name == bot.user:
        return

    if (len(ctx.content) == 6) and (ctx.channel.name == "room-codes" or ctx.channel.name == "apollo-rythm-bots-etc") \
            and ctx.content.isalpha():
        await ctx.channel.send(create_acronym(ctx.content))

    if " EST" in ctx.content.upper():
        if time.localtime().tm_isdst:
            await ctx.channel.send("IT'S EDT YOU FUCKING MORON")

    if " CST" in ctx.content.upper():
        if time.localtime().tm_isdst:
            await ctx.channel.send("IT'S CDT YOU FUCKING MORON")

    if " MST" in ctx.content.upper():
        if time.localtime().tm_isdst:
            await ctx.channel.send("IT'S MDT YOU FUCKING MORON")

    if " PST" in ctx.content.upper():
        if time.localtime().tm_isdst:
            await ctx.channel.send("IT'S PDT YOU FUCKING MORON")

    # Needed to support other @bot.command methods
    await bot.process_commands(ctx)

def create_acronym(six_letter_string):
    response_words = []
    wordnum = 1
    # adj noun adv verb adj noun
    for letter in six_letter_string:
        if wordnum == 1 or wordnum == 5:
            response_words.append(random.choice(adjectives[letter.lower()]))
        elif wordnum == 2 or wordnum == 6:
            response_words.append(random.choice(nouns[letter.lower()]))
        elif wordnum == 3:
            response_words.append(random.choice(adverbs[letter.lower()]))
        elif wordnum == 4:
            verb = random.choice(verbs[letter.lower()])
            if verb.endswith(("o", "sh", "ch", "tch", "x", "z", "ss")):
                verb += "es"
            elif verb.endswith(("by", "cy", "dy", "fy", "gy", "hy", "jy", "ky", "ly", "my", "ny", "py", "qy",
                                "ry", "sy", "ty", "vy", "wy", "xy", "zy")):
                verb = verb[:-1]
                verb += "ies"
            else:
                verb += "s"
            response_words.append(verb)
        wordnum += 1

    response = " ".join(response_words)
    return response


@bot.command()
async def multipoll(context: commands.Context, *args: str):
    if ":" in args:
        separator = args.index(":")

        options = args[:separator]
        emojis = args[separator + 1:]

        await send_and_react(context, options, emojis)
    else:
        await send_and_react(context, args, default_multipoll_emojis)


@bot.command()
async def schedule_next_week(context: commands.Context):
    today = datetime.date.today()
    await schedule_for_seven_days(context, datetime.timedelta(days=-today.weekday(), weeks=1))


@bot.command()
async def schedule_next_seven_days(context: commands.Context):
    await schedule_for_seven_days(context, datetime.timedelta(days=1))


async def schedule_for_seven_days(context: commands.Context, start_offset: datetime.timedelta):
    today = datetime.date.today()
    week_dates = map(lambda offset: today + start_offset + datetime.timedelta(days=offset), range(0, 7))
    week_strings = list(map(lambda date: date.strftime("%A %m/%d"), week_dates))

    await send_and_react(context, week_strings, default_multipoll_emojis)


async def send_and_react(context: commands.Context, message_strings: Sequence[str], emojis: Sequence[str]):
    for message_string in message_strings:
        message = await context.channel.send(content=message_string)

        for emoji in emojis:
            await message.add_reaction(emoji)

bot.run(TOKEN)
