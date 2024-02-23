import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

dev_user_ids = [842201757948968991]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_command_error(ctx, error):
    error_channel_id = 1210495978722033664
    error_channel = bot.get_channel(error_channel_id)

    if error_channel:
        embed = discord.Embed(title="Error", description=f"An error occurred: {type(error).__name__} - {error}", color=discord.Color.red())
        await error_channel.send(embed=embed)
    else:
        print(f"An error occurred: {type(error).__name__} - {error}")

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

token = os.getenv("Token")
bot.run(token)


keep_alive()
