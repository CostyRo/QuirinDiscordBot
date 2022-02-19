from asyncio import gather as async_gather
# import gather from asyncio to await more coroutines in paralel

from discord.ext import commands
from discord import Embed,Option,slash_command
# import embed, option and commands/slash commands from pycord

# create the class for administration commands
class Administration(commands.Cog):

	"""Administration cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(name="purge",description="Delete messages!")
	async def deletemessages(self,ctx,
		messages:Option(int,"How many messages to be deleted?",required=False,default=10)):

		"""Slash command for deleting messages"""

		if messages<=0:
			await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR!**"))
			return
		# if number of messages is negative or zero respond with an error

		if ctx.author.guild_permissions.manage_messages:
			await async_gather(ctx.channel.purge(limit=messages),
			ctx.respond(embed=Embed(color=0x00ff40,title="**Purge!**",description=f"**{messages} messages have been cleared!**")))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR!**",description="**You don't have permissions for that!**"))
		# if the user have permission to manage messages delete the messages
		# and respond to the user

def setup(bot): bot.add_cog(Administration(bot))
# setup this cog