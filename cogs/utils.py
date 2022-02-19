from discord.ext import commands
from discord import Embed,Member,Option,slash_command
# import embed, member, option and commands/slash commands from pycord

# create the class for utils commands
class Utils(commands.Cog):

	"""Utils cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(description="Get the avatar!")
	async def avatar(self,ctx,
	user:Option(Member,"Enter a user!",required=False,default=None)):

		"""Slash command to get the avatar of a user"""

		await ctx.respond((user or ctx.author).avatar.url)
		# respond with the avatar of the user

	@slash_command()
	async def info(self,ctx,
	number:Option(int,"Number of the info",choices=[0,1,2,3,4,5,6])):

		"""Slash command to display bot's info!"""

		if number==0: await ctx.respond(embed=Embed(color=0x00ff40,description="**Version: 0.2.0\nProgramming language: python\nAPI: pycord(discord.py fork)**"))
		elif number==1: await ctx.respond(embed=Embed(color=0x00ff40,description="**The avatar of the bot was made by Criss#4858 and Omul Invizibil#2727.**"))
		elif number==2: await ctx.respond(embed=Embed(color=0x00ff40,description=f"**Quirin, come from Quirinus, the roman god of springs.**"))
		elif number==3: await ctx.respond(embed=Embed(color=0x00ff40,description="**\"Defences Against the Dark Arts\" say something for you?**"))
		elif number==4: await ctx.respond(embed=Embed(color=0x00ff40,description="**My favorite fun fact is fun fact#46.**"))
		elif number==5: await ctx.respond(embed=Embed(color=0x00ff40,description="**Don't play roulettecolor!\nIs a scam.**"))
		else: await ctx.respond(embed=Embed(color=0x00ff40,description="**Info from number 1 to 5 was secret before.\nWere the 5 easter eggs of the bot and now there are public.**"))
		# respond with the info dependeing on the info number

	@slash_command(description="See the latency!")
	async def ping(self,ctx):

		"""Slash command to see the ping of the bot"""

		await ctx.respond(embed=Embed(color=0x00ff40,description=f"**Ping is {int(self.bot.latency*1000)}ms!**"))
		# respond with the ping

def setup(bot): bot.add_cog(Utils(bot))
# setup this cog