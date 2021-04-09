import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from english_words import english_words_set

load_dotenv()
TOKEN = os.getenv("EDMUNGBOT_TOKEN")

bot = commands.Bot(command_prefix='!')

alphabetized_words = dict()

for word in english_words_set:
    first_letter = word[0].lower()
    if not first_letter in alphabetized_words:
        alphabetized_words[first_letter] = []
    alphabetized_words[first_letter].append(word)

@bot.event
async def on_message(ctx):
    if ctx.author.name == bot.user:
        return

    if (len(ctx.content) == 6) and ctx.channel.name == "room-codes":
        print(len(ctx.content))

        response_words = []
        for letter in ctx.content:
            response_words.append(random.choice(alphabetized_words[letter.lower()]))
        response = " ".join(response_words)

        await ctx.channel.send(response)


bot.run(TOKEN)
