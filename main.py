import discord
from discord.ext import commands
#from discord import activity
#from dotenv import load_dotenv
import random
import os 
import json
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']


with open('setting.json',mode = 'r', encoding='utf8') as jfile: #read file setting.json
    jdata = json.load(jfile)
    jfile.close()

#load_dotenv() before using to store the password,but dont need it any more
#TOKEN = os.getenv('Discord_TOKEN')

bot = commands.Bot(command_prefix='$') #using '$' before commmand

@bot.event
async def on_ready():
    print(">> Bot is online. <<")
    print('Logged in as {}\n'.format(bot.user))
    game = discord.Game("努力學習py中")
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.command() #load the command
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command() #unload the command
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command() #reload the command
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')


@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = ['I\'m the human form of the 100.',
        'Cool. Cool cool cool.'
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


for filename in os.listdir('./cmds'): #read other py from cmds file
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}') # it will delete '.py' 


if __name__ == "__main__":
    keep_alive()
    bot.run(my_secret)