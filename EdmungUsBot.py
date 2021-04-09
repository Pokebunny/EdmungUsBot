import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from english_words import english_words_set

load_dotenv()
TOKEN = os.getenv("EDMUNGBOT_TOKEN")

bot = commands.Bot(command_prefix='!')

a_set = []
b_set = []
c_set = []
d_set = []
e_set = []
f_set = []
g_set = []
h_set = []
i_set = []
j_set = []
k_set = []
l_set = []
m_set = []
n_set = []
o_set = []
p_set = []
q_set = []
r_set = []
s_set = []
t_set = []
u_set = []
v_set = []
w_set = []
x_set = []
y_set = []
z_set = []

for word in english_words_set:
    if word[0].lower() == "a":
        a_set.append(word)
    elif word[0].lower() == "b":
        b_set.append(word)
    elif word[0].lower() == "c":
        c_set.append(word)
    elif word[0].lower() == "d":
        d_set.append(word)
    elif word[0].lower() == "e":
        e_set.append(word)
    elif word[0].lower() == "f":
        f_set.append(word)
    elif word[0].lower() == "g":
        g_set.append(word)
    elif word[0].lower() == "h":
        h_set.append(word)
    elif word[0].lower() == "i":
        i_set.append(word)
    elif word[0].lower() == "j":
        j_set.append(word)
    elif word[0].lower() == "k":
        k_set.append(word)
    elif word[0].lower() == "l":
        l_set.append(word)
    elif word[0].lower() == "m":
        m_set.append(word)
    elif word[0].lower() == "n":
        n_set.append(word)
    elif word[0].lower() == "o":
        o_set.append(word)
    elif word[0].lower() == "p":
        p_set.append(word)
    elif word[0].lower() == "q":
        q_set.append(word)
    elif word[0].lower() == "r":
        r_set.append(word)
    elif word[0].lower() == "s":
        s_set.append(word)
    elif word[0].lower() == "t":
        t_set.append(word)
    elif word[0].lower() == "u":
        u_set.append(word)
    elif word[0].lower() == "v":
        v_set.append(word)
    elif word[0].lower() == "w":
        w_set.append(word)
    elif word[0].lower() == "x":
        x_set.append(word)
    elif word[0].lower() == "y":
        y_set.append(word)
    elif word[0].lower() == "z":
        z_set.append(word)

@bot.event
async def on_message(ctx):
    if ctx.author.name == bot.user:
        return

    if (len(ctx.content) == 6) and ctx.channel.name == "room-codes":
        print(len(ctx.content))
        response = ""
        for letter in ctx.content:
            if letter.lower() == "a":
                response += random.choice(a_set)
            elif letter.lower() == "b":
                response += random.choice(b_set)
            elif letter.lower() == "c":
                response += random.choice(c_set)
            elif letter.lower() == "d":
                response += random.choice(d_set)
            elif letter.lower() == "e":
                response += random.choice(e_set)
            elif letter.lower() == "f":
                response += random.choice(f_set)
            elif letter.lower() == "g":
                response += random.choice(g_set)
            elif letter.lower() == "h":
                response += random.choice(h_set)
            elif letter.lower() == "i":
                response += random.choice(i_set)
            elif letter.lower() == "j":
                response += random.choice(j_set)
            elif letter.lower() == "k":
                response += random.choice(k_set)
            elif letter.lower() == "l":
                response += random.choice(l_set)
            elif letter.lower() == "m":
                response += random.choice(m_set)
            elif letter.lower() == "n":
                response += random.choice(n_set)
            elif letter.lower() == "o":
                response += random.choice(o_set)
            elif letter.lower() == "p":
                response += random.choice(p_set)
            elif letter.lower() == "q":
                response += random.choice(q_set)
            elif letter.lower() == "r":
                response += random.choice(r_set)
            elif letter.lower() == "s":
                response += random.choice(s_set)
            elif letter.lower() == "t":
                response += random.choice(t_set)
            elif letter.lower() == "u":
                response += random.choice(u_set)
            elif letter.lower() == "v":
                response += random.choice(v_set)
            elif letter.lower() == "w":
                response += random.choice(w_set)
            elif letter.lower() == "x":
                response += random.choice(x_set)
            elif letter.lower() == "y":
                response += random.choice(y_set)
            elif letter.lower() == "z":
                response += random.choice(z_set)
            response += " "

        await ctx.channel.send(response)


bot.run(TOKEN)
