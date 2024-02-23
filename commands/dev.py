from discord.ext import commands
import os

class DevCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='devrestart', hidden=True)
    async def dev_restart(self, ctx):
        if ctx.author.id not in dev_user_ids:
            return

        await ctx.send("Restarting...")
        await self.bot.close()

def setup(bot):
    bot.add_cog(DevCog(bot))
