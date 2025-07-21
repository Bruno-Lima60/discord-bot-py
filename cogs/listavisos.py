import discord
import os
import json
from discord.ext import commands

class listAvisos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def listavisos(self, ctx, user: discord.User):
        if ctx.author.guild_permissions.kick_members and ctx.author.guild_permissions.ban_members:
            if not os.path.exists('warnings.json'):
                with open('warnings.json', 'w') as f:
                    json.dump({}, f)
            try:
                with open('warnings.json', 'r') as f:
                    warnings = json.load(f)
            except json.JSONDecodeError:
                warnings = {}

            if str(user.id) in warnings:
                user_warnings = warnings[str(user.id)]
                if user_warnings:
                    for index, warning in enumerate(user_warnings, start=1):
                        embed = discord.Embed(
                            title=f"Aviso {index} ({user.name})",
                            description=f"{warning['motivo']}\nEmitido por: {warning['emitido_por']}",
                            color=discord.Color.red()
                        )
                        await ctx.send(embed=embed)
                else:
                    await ctx.send(f"❌ {user.mention} não tem nenhum aviso.")
            else:
                await ctx.send(f"❌ {user.mention} não tem nenhum aviso.")
        else:
            await ctx.send("❌ Você não tem permissão para usar este comando!")

    @listavisos.error
    async def listavisos_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Mencione um usuário primeiro.")

async def setup(bot):
    await bot.add_cog(listAvisos(bot))
    print("ListAvisos - Pronto!")