from asyncio import sleep as async_sleep,gather as async_gather
# import necessary functions from asyncio module

from discord.ext import commands
from discord.utils import find as discord_find,get as discord_get
from discord import Embed,Member,Object,Option,slash_command,PermissionOverwrite
# import embed, member, object, option, overwriting permission
# and commands/slash commands from pycord
# and import mecessary functions from discord.utils module

# create the class for games commands
class Moderation(commands.Cog):

	"""Moderation cog"""

	def __init__(self,bot): self.bot=bot
	# init the class

	@slash_command(description="Ban someone!")
	async def ban(self,ctx,
	member:Option(Member,"Select the person you want to ban!"),
	reason:Option(str,"Reason for the ban!",required=False,default=None)):

		"""Slash command to ban a member"""

		if ctx.author==member: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description=f"**{member.mention} can't ban yourself, silly!**"))
		elif member.guild_permissions.ban_members: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**I can't ban that user!**"))
		elif ctx.author.guild_permissions.ban_members: await async_gather(member.ban(reason=reason),
		ctx.respond(embed=Embed(color=0x00ff40,title="**Banned**",description=f"""**{member.mention} was banned{"" if reason is None else f" for {reason}"}!**""")),
		member.send(embed=Embed(color=0xff0000,title="**Banned**",description=f"""**You have been banned from {ctx.guild}{"" if reason is None else f" for {reason}"}!**""")))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have permissions for that!**"))
		# check all the errors and if no error is raised ban the user

	@slash_command(description="Kick someone!")
	async def kick(self,ctx,
	member:Option(Member,"Select the person you want to kick!"),
	reason:Option(str,"Reason for the kick!",required=False,default=None)):

		"""Slash command to kick a member"""

		if ctx.author==member: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description=f"**{member.mention} can't kick yourself, silly!**"))
		elif member.guild_permissions.kick_members: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**I can't kick that user!**"))
		elif ctx.author.guild_permissions.kick_members: await async_gather(member.kick(reason=reason),
		ctx.respond(embed=Embed(color=0x00ff40,title="**Kicked**",description=f"""**{member.mention} was kicked{"" if reason is None else f" for {reason}"}!**""")),
		member.send(embed=Embed(color=0xff0000,title="**Kicked**",description=f"""**You have been kicked from {ctx.guild}{"" if reason is None else f" for {reason}"}!**""")))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have permissions for that!**"))
		# check all the errors and if no error is raised kick the user

	@slash_command(description="Mute someone!")
	async def mute(self,ctx,
	member:Option(Member,"Select the person you want to mute!"),
	time:Option(int,"Time for the mute!",required=False,default=0)):

		"""Slash command to mute a member"""

		if ctx.author==member: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description=f"**{member.mention} can't mute yourself, silly!**"))
		elif member.guild_permissions.administrator or member.guild_permissions.manage_messages: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**I can't mute that user!**"))
		elif ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_messages:
			role=discord_find(lambda r:r.name=="Muted",ctx.guild.roles)
			if role is None:
				role=await ctx.guild.create_role(name="Muted")
				for channel in ctx.guild.text_channels: await channel.set_permissions(role,overwrite=PermissionOverwrite(send_messages=False))

			await async_gather(member.add_roles(role),
			ctx.respond(embed=Embed(color=0x00ff40,title="**Muted**",description=f"""**{member.mention} was muted{"" if time==0 else f" for {time}seconds"}!**""")),member.send(embed=Embed(color=0xff0000,title="**Muted**",description=f"""**You have been muted in {ctx.guild}{"" if time==0 else f" for {time}seconds"}!**""")))

			if time!=0: 
				await async_sleep(time)
				await member.remove_roles(role)
				await member.send(embed=Embed(color=0x00ff40,title="**Unmuted**",description=f"**You have been unmuted in {ctx.guild}!**"))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have permissions for that!**"))
		# check all the errors and if no error is raised create the role
		# give the role to the user
		# and wait for time and finnaly unmute the user

	@slash_command(description="Unban someone!")
	async def unban(self,ctx,
	id:Option(str,"Id for the person you want to unban!")):

		"""Slash command to unban a member"""

		if ctx.author.guild_permissions.ban_members: await async_gather(ctx.guild.unban(Object(id)),ctx.respond(embed=Embed(color=0x00ff40,title="**Unbanned**",description=f"**{id} was unbanned!**")))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have permissions for that!**"))
		# check all the errors and if no error is raised unban the user

	@slash_command(description="Unmute someone!")
	async def unmute(self,ctx,
	member:Option(Member,"Select the person you want to mute!")):

		"""Slash command to unmute a member"""

		if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.moderator: await async_gather(member.remove_roles(discord_get(ctx.guild.roles,name="Muted")),
		ctx.respond(embed=Embed(color=0x00ff40,title="**Unmuted**",description=f"**{member.mention} was unmuted!**")),
		member.send(embed=Embed(color=0x00ff40,title="**Unmuted**",description=f"**You have been unmuted in {ctx.guild}!**")))
		else: await ctx.respond(embed=Embed(color=0xff0000,title="**ERROR**",description="**You don't have permissions for that!**"))
		# check all the errors and if no error is raised mute the user

def setup(bot): bot.add_cog(Moderation(bot))
# setup this cog