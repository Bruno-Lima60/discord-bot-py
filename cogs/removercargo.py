import discord
from discord.ext import commands

class RemoverCargo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def removercargo(self, ctx, member: discord.Member, role_name):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if ctx.author.guild_permissions.manage_roles:
            if role:
                if role not in member.roles:
                    await ctx.send(f'❌ Esse membro já não tem esse cargo!')
                else:
                    await member.remove_roles(role)
                    await ctx.send(f'✅ {member.mention} agora não tem mais o cargo "{role.name}"!')
            else:
                await ctx.send("❌ Esse cargo não existe!")
        else:
            await ctx.send("Você não tem permissão para usar este comando!")
            return
        
    @removercargo.error
    async def addcargo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Especifique um cargo, por favor!")

async def setup(bot):
    await bot.add_cog(RemoverCargo(bot))
    print("RemoverCargo - Pronto!")