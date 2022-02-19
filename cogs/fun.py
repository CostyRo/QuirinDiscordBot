from random import choice,randrange
# import the necessary functions from the random module

from discord.ext import commands
from discord import Embed,Option,slash_command
# import embed, option and commands/slash commands from pycord

# create the class for fun commands
class Fun(commands.Cog):

	"""Fun cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(name="8ball",description="Ask me a question!")
	async def ask_a_question(self,ctx,
	question:Option(str,"Write your question here!")):

		"""Slash command for receving a random answear to a question"""

		responses=["Yes.","Sure.","Absolutely.","Si amigo.","YES YES YES!",
		"No.","Absolutely not.","No way.","No chance.","Nope.",
		"I don't know.","Maybe.","I can't tell you.","Sorry, i am bussy right now.","Leave me alone."]
		# create the list with possible answers

		await ctx.respond(embed=Embed(color=0x73e4e6,title="**8ball**",description=f"**Question: {question}\nAnswear: {choice(responses)}**"))
		# respond with a random answear

	@slash_command(description="Check how boomer you are!")
	async def boomer(self,ctx,
	user:Option(str,"Enter a user!",required=False,default=None)):

		"""Slash command to check how boomer you are"""

		await ctx.respond(embed=Embed(color=0x73e4e6,title="**Boomer**",description=f"**{user or ctx.author.mention} is {randrange(0,101)}% boomer.**"))
		# respond with a random percent

	@slash_command(description="Flip a coin!")
	async def coinflip(self,ctx):

		"""Slash command for fliping a coin"""

		# respond if the coin fell on side
		if randrange(0,6000)==0: await ctx.respond(embed=Embed(color=0xffdf00,title="**Coinflip!**",description="**WOW! Side!\nYou are so lucky today!**"))
		else:
			if randrange(0,2)==0: await ctx.respond(embed=Embed(color=0xdaa520,title="**Coinflip!**",description="**Heads**"))
			else: await ctx.respond(embed=Embed(color=0xdaa520,title="**Coinflip!**",description="**Tails**"))
			# respond with the part where the coin fell

	@slash_command(description="Say hello to somebody!")
	async def hello(self,ctx,
	user:Option(str,"Enter a user!",required=False,default=None)):

		"""Slash command to wave somebody"""

		await ctx.respond(embed=Embed(color=0x73e4e6,description=f"**Hello {user or ctx.author.mention}!**"))
		# wave the user or yourself if the name isn't given

	@slash_command(description="Find the impostor!")
	async def impostor(self,ctx,
	user:Option(str,"Enter a user",required=False,default=None)):

		"""Slash command to find the impostor"""

		await ctx.respond(embed=Embed(color=0xff0000,description=f"**{user or ctx.author.mention} is kinda sus!**"))
		# respond with the impostor(the user or you)

	@slash_command(description="Check how noob you are!")
	async def noob(self,ctx,
	user:Option(str,"Enter a user!",required=False,default=None)):

		"""Slash command to check how noob you are"""

		await ctx.respond(embed=Embed(color=0x73e4e6,title="**Noob**",description=f"**{user or ctx.author.mention} is {randrange(0,101)}% noob.**"))
		# respond with a random percent

def setup(bot): bot.add_cog(Fun(bot))
# setup this cog