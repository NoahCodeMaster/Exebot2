import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

dev_user_ids = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    error_channel_id = 1210495978722033664
    error_channel = bot.get_channel(error_channel_id)

    if error_channel:
        await error_channel.send(f"An error occurred: {type(error).__name__} - {error}")
    else:
        print(f"An error occurred: {type(error).__name__} - {error}")


for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

token = os.getenv("Token")
bot.run(token)
