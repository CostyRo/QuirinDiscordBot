from asyncio import gather as async_gather
# import gather from asyncio to await more coroutines in paralel

from discord.ext import commands
from discord import Embed,Option,slash_command
# import embed, member, option and commands/slash commands from pycord

from func import update_suggestion,suggestion_channel
# and import necessary functions from my function module

# create the class for suggestions commands
class Suggestions(commands.Cog):

	"""Suggestions cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(description="Create the channel for suggestions!")
	async def suggestionschannel(self,ctx):

		"""Slash command for selecting the channel for suggestions"""

		# if the user have administrator permission
		if ctx.author.guild_permissions.administrator:
			await ctx.respond(embed=Embed(color=0x00ff40,description=f"**Channel set as: {ctx.channel}**"))
			# respond that the channel was set

			update_suggestion(ctx.guild.id,ctx.channel.id)
			# update databse with suggestion channels
		else: await ctx.respond(embed=Embed(color=0xff0000,description=f"**You don't have permissions for that!**"))

	@slash_command(description="Suggest something!")
	async def suggest(self,ctx,
	suggestion:Option(str,"Write a suggestion here!",required=True)):

		"""Slash command for suggest something"""

		channel=await self.bot.get_channel(suggestion_channel(ctx.guild.id)).\
		send(embed=Embed(title="Suggestion",description=suggestion,color=0x6e42ff).\
		set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",icon_url=ctx.author.avatar.url))
		# get the channel and send the suggestion there

		await async_gather(channel.add_reaction("⬆️"),channel.add_reaction("🆗"),channel.add_reaction("⬇️"),
		ctx.respond(embed=Embed(color=0x00ff40,description="Done!")))
		# add reactions to the suggestion
		# and respond that sending suggestion was successful

def setup(bot): bot.add_cog(Suggestions(bot))
# setup this cog