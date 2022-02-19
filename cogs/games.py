from random import randrange
# import randrange from random module to generate random numbers

from discord.ext import commands
from discord import Embed,Option,slash_command
# import embed, option and commands/slash commands from pycord

from func import have_account,update_points,user_points
# import necessary functions from my function module

# create the class for games commands
class Games(commands.Cog):

	"""Games cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(description="Role a dice!")
	async def dice(self,ctx,
	points:Option(int,"Set bet amount!",required=False,default=100)):

		"""Slash command for playing dice"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if points<=user_points(d):
				if [1,6,5,4,3,2].index(md:=randrange(1,7))>[1,6,5,4,3,2].index(yd:=randrange(1,7)):
					await ctx.respond(embed=Embed(color=0x00ff40,title="**Dice**",description=f"**My dice: {md}.\nYour dice: {yd}.\nYou win {2*points} points!**"))
					update_points([d],[points],["+"])
				elif md==yd: await ctx.respond(embed=Embed(color=0xffffff,title="**Dice**",description=f"**My dice: {md}.\nYour dice: {yd}.\nDraw!**"))
				else:
					await ctx.respond(embed=Embed(color=0xff0000,title="**Dice**",description=f"**My dice: {md}.\nYour dice: {yd}.\nYou lose {points} points!**"))
					update_points([d],[points],["-"])
				# determine the winner depending on who have a bigger number
				# on dice and respond to him and modify the database
			else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have enough points!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You are not sign up yet!**"))

	@slash_command(description="Play rock, paper or scissors!")
	async def rps(self,ctx,
	element:Option(str,"Select an element!",choices=["rock","scissors","paper"]),
	points:Option(int,"Set bet amount!",required=False,default=100)):

		"""Slash command for playing rps"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if points<=user_points(d):
				myelem="rock" if (n:=randrange(0,3))==0 else "paper" if n==1  else "scissors"
				# create the element for bot

				if element==myelem:
					await ctx.respond(embed=Embed(color=0xffffff,title="**Rps**",description=f"**Your element: {element}.\nMy element: {myelem}.\nDraw!**"))
				elif {"rock":"paper","paper":"scissors","scissors":"rock"}[element]==myelem:
					await ctx.respond(embed=Embed(color=0xff0000,title="**Rps**",description=f"**Your element: {element}.\nMy element: {myelem}.\nYou lose {points} points!**"))
					update_points([d],[points],["-"])
				else:
					await ctx.respond(embed=Embed(color=0x00ff40,title="**Rps**",description=f"**Your element: {element}.\nMy element: {myelem}.\nYou win {2*points} points!**"))
					update_points([d],[points],["+"])
				# determine the winner and respond to him
				# and modify the database
			else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have enough points!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You are not sign up yet!**"))

	@slash_command(description="Bet on a color on roulette!")
	async def roulettecolor(self,ctx,
	color:Option(str,"Select a color!",choices=["red","black","green"]),
	points:Option(int,"Set bet amount!",required=False,default=100)):

		"""Slash command for playing roulette with colors"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if points<=user_points(d):
				result="green" if (n:=randrange(0,37))==0 else "red" if n%2==0 else "black"
				# create the color of roulette

				#check if the color is correct
				if color==result:
					if result=="green":
						await ctx.respond(embed=Embed(color=0x00ff40,title="**Roulettecolor**",description=f"**Color from roulette is: {result}\nYou win {36*points} points!**"))
						update_points([d],[35*points],["+"])
					else:
						await ctx.respond(embed=Embed(color=0x00ff40,title="**Roulettecolor**",description=f"**Color from roulette is: {result}\nYou win {2*points} points!**"))
						update_points([d],[points],["+"])
					# respond to the user and
					# modify database depending on what color was on roulette
				else:
					await ctx.respond(embed=Embed(color=0xff0000,title="**Roulettecolor**",description=f"**Color from roulette is: {result}\nYou lose {points} points!**"))
					update_points([d],[points],["-"])
					# respond to the user and modify database
			else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have enough points!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You are not sign up yet!**"))

	@slash_command(description="Bet on a number from 0 to 36 on roulette!")
	async def roulettenumber(self,ctx,
	number:Option(int,"Select a number from 0 to 36!"),
	points:Option(int,"Set bet amount!",required=False,default=100)):

		"""Slash command for playing roulette with numbers"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if points<=user_points(d):
				# if the number is incorrect respond with an error
				if number>36 or number<0:
					await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description=f"**{number} is an invalid number!**"))
					# respond with an error if the number isn't correct
				else:
					if number==(n:=randrange(0,37)):
						await ctx.respond(embed=Embed(color=0x00ff40,title="**Roulettenumber**",description=f"**Number from roulette is: {n}.\nYou win {36*points} points!**"))
						update_points([d],[36*points],["+"])
					else:
						await ctx.respond(embed=Embed(color=0xff0000,title="**Roulettenumber**",description=f"**Number from roulette is: {n}.\nYou lose {points} points!**"))
						update_points([d],[points],["-"])
					# respond and modify the database depending on
					# if the number is correct or not
			else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have enough points!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You are not sign up yet!**"))

	@slash_command(description="Play russian roulette with the bot!")
	async def russianroulette(self,ctx,
	points:Option(int,"Set bet amount!",required=False,default=100)):

		"""Slash command for playing rusianroulette"""

		# check if the user have an account
		if have_account(d:=ctx.author.id):
			# check if the user have enough points
			if points<=user_points(d):
				final=randrange(1,7)
				# generate the bullete

				result="".join((f"""**Try#{t}: {"I" if t%2==1 else "You"} {"lose!" if t==final else "am alive!" if t%2==1 else "are alive!"}**\n""" for t in range(1,final+1)))
				# set the result

				if final%2==1:
					await ctx.respond(embed=Embed(color=0x00ff40,title="**Russian roulette**",description=result+f"**You win {2*points} points!**"))
					update_points([d],[points],["+"])
				else:
					await ctx.respond(embed=Embed(color=0xff0000,title="**Russian roulette**",description=result+f"**You lose {points} points!**"))
					update_points([d],[points],["-"])
				# respond and modify the database depending on who was shot

			else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have enough points!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You are not sign up yet!**"))

def setup(bot): bot.add_cog(Games(bot))
# setup this cog