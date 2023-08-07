import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
# Load the .env file
load_dotenv()

# Access the variables
DISCORD_LUNCH_BOT = os.getenv('DISCORD_LUNCH_BOT')

intents = discord.Intents.default()
intents.webhooks = True
intents.messages = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command()
async def link(ctx):
    await ctx.send('please place your order through this link:\nhttp://aimanmx.pythonanywhere.com/')

bot.run(DISCORD_LUNCH_BOT)
