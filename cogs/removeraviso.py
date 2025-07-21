import discord
from discord.ext import commands
import json
import os

class removerAviso(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def removeraviso(self, ctx, user: discord.User, index: int):
        if ctx.author.guild_permissions.kick_members and ctx.author.guild_permissions.ban_members:
            if not os.path.exists('warnings.json'):
                with open('warnings.json', 'w') as f:
                    json.dump({}, f)
            try:
                with open('warnings.json', 'r') as f:
                    warnings = json.load(f)
            except json.JSONDecodeError:
                warnings = {}

            if str(user.id) in warnings and len(warnings[str(user.id)]) >= index > 0:
                removed_warning = warnings[str(user.id)].pop(index - 1)
                with open('warnings.json', 'w') as f:
                    json.dump(warnings, f, indent=4)
                await ctx.send(f"✅ Tirei o aviso: **'{removed_warning['motivo']}'** de {user.mention}\nVocê agora tem {len(warnings[str(user.id)])} avisos!")
            else:
                await ctx.send(f"❌ {user.mention} não tem nenhum aviso.")
        else:
            await ctx.send("❌ Você não tem permissão para usar este comando!")

    @removeraviso.error
    async def removeraviso_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Mencione um usuário primeiro.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Inválido!")

async def setup(bot):
    await bot.add_cog(removerAviso(bot))
    print("RemoverAviso - Pronto!")