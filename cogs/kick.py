import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if reason is None:
            reason = "No Reason Provided"
        if ctx.author.guild_permissions.kick_members:
            await user.kick(reason=reason)
            await ctx.send(f'✅ {user.mention} foi expulso do servidor com sucesso, pelo motivo: "{reason}"!')
        else:
            await ctx.send("❌ Você não tem permissão para usar este comando!")
            return

    @kick.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ O comando não foi feito do jeito certo!\nSiga o exemplo: `.kick @user menor de idade`")

async def setup(bot):
    await bot.add_cog(Kick(bot))
    print("Kick - Pronto!")