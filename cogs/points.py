from discord.ext import commands
from discord import Embed,Member,Option,slash_command
# import embed, member, option and commands/slash commands from pycord

from func import have_account,random_fact,update_points,user_points
# import necessary functions from my function module

# create the class for points commands
class Points(commands.Cog):

	"""Points cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(description="Check someone's balance!")
	async def balance(self,ctx,
	user:Option(Member,"Enter a user!",required=False,default=None)):

		"""Slash command for checking a user's balance"""

		# check if the user have an account
		if have_account((u:=(user or ctx.author)).id):
			await ctx.respond(embed=Embed(color=0x00ff40,description=f"**{u.mention} balance is: {user_points(u.id)} points.**"))
			# respond with the balance
		else: await ctx.respond(embed=Embed(color=0xff0000,description=f"**{(u)} isn't sign up!**"))

	@slash_command(description="Buy a fun fact!")
	async def buy_funfact(self,ctx):

		"""Slash command to buy a fun fact"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if 100<=user_points(d): update_points([d],[100],["-"])
			else:
				await ctx.author.send(embed=Embed(color=0xff0000,description="**You don't have enough points!**"))
				return
				# respond that he doesn't have enough points and stop
		else: update_points([d],[0],[""])
		# if user doesn't have an account
		# create one and substract points for fun fact

		await ctx.author.send(embed=Embed(color=0xffdf00,title="Fun fact",description=f"""**{random_fact("ff")}**"""))
		# respond with a random fun fact

	@slash_command(description="Buy a super fun fact!")
	async def buy_superfunfact(self,ctx):

		"""Slash command to buy a super fun fact"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if 1000<=user_points(d):
				update_points([d],[1000],["-"])
				# modify the database

				await ctx.author.send(embed=Embed(color=0xffdf00,title="Fun fact",description=f"""**{random_fact("ffs")}**"""))
				# respond with a random super fun fact
			else: await ctx.author.send(embed=Embed(color=0xff0000,description="**You don't have enough points!**"))
		else: await ctx.author.send(embed=Embed(color=0xff0000,description="**Make an account first!**"))

	@slash_command(description="Get your daily points!")
	@commands.cooldown(1,86400,commands.BucketType.user)
	async def daily(self,ctx):

		"""Slash command to get daily points"""

		# check if the user have an account
		if have_account(d:=(ctx.author.id)): update_points([d],[100],["+"])
		else: update_points([d],[200],[""])
		# if the user have an account add 100 points
		# else make an account for him and add 100 points

		await ctx.respond(embed=Embed(color=0x00ff40,description="**You received 100 points!**"))
		# respond that he recevied his points

	@slash_command(description="Sign up!")
	async def signup(self,ctx):

		"""Slash command to make an account"""

		# check if the user have an account
		if have_account(d:=(ctx.author.id)): await ctx.respond("**You are sign up already!**")
		else:
			await ctx.respond("**Now you are sign up!**")
			# respond that his account is created

			update_points([d],[100],[""])
			# create the account

	@slash_command(description="Transfer points to somebody!")
	async def transfer(self,ctx,
	name:Member,
	points:int=100):

		"""Slash command to transfer points to another user"""

		# check if the author and user have accounts
		if have_account((y:=ctx.author.id)) and have_account((h:=name.id)):
			# check if the accounts aren't the same
			if y!=h:
				# check if the number points is valid
				if 100<=points:
					# check if the user have enough points
					if points<=user_points(y):
						await ctx.respond(embed=Embed(color=0x00ff40,description=f"**{int(points*0.75)} points transfered to {name.mention}.**"))
						# respond that the transfer was successful

						update_points([y,h],[points,int(points*0.75)],["-","+"])
						# modify the database
					else: await ctx.respond(embed=Embed(color=0xff0000,description="**You don't have enough points!**"))
				else: await ctx.respond(embed=Embed(color=0xff0000,description="**Transfer minim 100 points!**"))
			else: await ctx.respond(embed=Embed(color=0xff0000,description="**You can't transfer points to yourself!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,description="**One of you isn't sign up!**"))

def setup(bot): bot.add_cog(Points(bot))
# setup this cog