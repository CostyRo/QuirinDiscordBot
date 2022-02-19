from os import getenv,listdir
from dotenv import load_dotenv
# import getenv to get the .env variables and listdir to browse the directory
# import load_dotenv from dotenv to load .env variables

from discord.ext import commands
from discord import Bot,Embed,Game,Status
# import bot, embed, game, status adn commands from pycord

load_dotenv()
# load .env variables

bot=Bot()
# create the bot

@bot.event
async def on_ready(): await bot.change_presence(status=Status.idle,activity=Game("To use FunFacts commands you need to have \"allow DMs from server members\" setting on!"))
# when bot is ready set the status of the bot

@bot.event
async def on_application_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown): await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR!**",description="**This command is currently on cooldown!**"))
    else: raise error
# if a command is spammed announce that or raise the given error

if __name__=="__main__":
	for filename in listdir("cogs"):
		if filename.endswith(".py"): bot.load_extension(f"cogs.{filename[:-3]}")
# if this file is executed loop the directory with cogs and load the cogs

bot.run(getenv("TOKEN"))
# run the bot with the token from .env