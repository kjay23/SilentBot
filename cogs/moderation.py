import os, sys, discord
from discord.ext import commands

if not os.path.isfile("config.py"):
	sys.exit("'config.py' not found! Please add it and try again.")
else:
	import config

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    async def kick(self, context, member: discord.Member, *args):
        """
        Kick a user out of the server.
        """
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Error!",
                    description="User has Admin permissions.",
                    color=config.error
                )
                await context.send(embed=embed)
            else:
                try:
                    reason = " ".join(args)
                    await member.kick(reason=reason)
                    embed = discord.Embed(
                        title="User Kicked!",
                        description=f"**{member}** was kicked by **{context.message.author}**!",
                        color=config.success
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    try:
                        await member.send(
                            f"You were kicked by **{context.message.author}**!\nReason: {reason}"
                        )
                    except:
                        pass
                except:
                    embed = discord.Embed(
                        title="Error!",
                        description="An error occurred while trying to kick the user.",
                        color=config.success
                    )
                    await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=config.error
            )
            await context.send(embed=embed)

    @commands.command(name="nick")
    async def nick(self, context, member: discord.Member, *, name: str):
        """
        Change the nickname of a user on a server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if name.lower() == "!reset":
                    name = None
                await member.change_nickname(name)
                embed = discord.Embed(
                    title="Changed Nickname!",
                    description=f"**{member}'s** new nickname is **{name}**!",
                    color=config.success
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An error occurred while trying to change the nickname of the user.",
                    color=config.success
                )
                await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=config.error
            )
            await context.send(embed=embed)

    @commands.command(name="unban")
    async def unban(self, context, member: discord.Member, *args):
        """
        Unbans a user from the server.
        """
        banned_users = await context.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
              await context.guild.unban(user)

    @commands.command(name="ban")
    async def ban(self, context, member: discord.Member, *args):
        """
        Bans a user from the server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                        title="Error!",
                        description="User has Admin permissions.",
                        color=config.success
                    )
                    await context.send(embed=embed)
                else:
                    reason = " ".join(args)
                    await member.ban(reason=reason)
                    embed = discord.Embed(
                        title="User Banned!",
                        description=f"**{member}** was banned by **{context.message.author}**!",
                        color=config.success
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    await member.send(f"You were banned by **{context.message.author}**!\nReason: {reason}")
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An error occurred while trying to ban the user.",
                    color=config.success
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=config.error
            )
            await context.send(embed=embed)

    @commands.command(name="warn")
    async def warn(self, context, member: discord.Member, *args):
        """
        Warns a user in his private messages.
        """
        if context.message.author.guild_permissions.administrator:
            reason = " ".join(args)
            embed = discord.Embed(
                title="User Warned!",
                description=f"**{member}** was warned by **{context.message.author}**!",
                color=config.success
            )
            embed.add_field(
                name="Reason:",
                value=reason
            )
            await context.send(embed=embed)
            try:
                await member.send(f"You were warned by **{context.message.author}**!\nReason: {reason}")
            except:
                pass
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=config.error
            )
            await context.send(embed=embed)

    @commands.command(name="purge")
    async def purge(self, context, number):
        """
        Delete a number of messages.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                number = int(number)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"`{number}` is not a valid number.",
                    color=config.error
                )
                await context.send(embed=embed)
                return
            if number < 1:
                embed = discord.Embed(
                    title="Error!",
                    description=f"`{number}` is not a valid number.",
                    color=config.error
                )
                await context.send(embed=embed)
                return
            purged_messages = await context.message.channel.purge(limit=number)
            embed = discord.Embed(
                title="Chat Cleared!",
                description=f"**{context.message.author}** cleared **{len(purged_messages)}** messages!",
                color=config.success
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=config.error
            )
            await context.send(embed=embed)

def setup(bot):
    bot.add_cog(moderation(bot))