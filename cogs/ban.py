import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if reason is None:
            reason = "No Reason Provided"
        if ctx.author.guild_permissions.ban_members:
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(f'`{user.name}` foi banido com sucesso pelo motivo: "{reason}"!')
        else:
            await ctx.send("Você não tem permissão para usar este comando!")
            return
        
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("O comando não foi feito do jeito certo!\nSiga o exemplo: `.ban @user menor de idade`")
        
async def setup(bot):
    await bot.add_cog(Ban(bot))
    print("Ban - Pronto!")