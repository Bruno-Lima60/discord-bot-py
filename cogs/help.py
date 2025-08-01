import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="**LISTA DE COMANDOS:**", color=discord.Color.blue())
        embed.add_field(name=".avisar <@usuário> <razão>", value="Adiciona um aviso a um usuário.", inline=False)
        embed.add_field(name=".addcargo <user> <nome-do-cargo>", value="Atribui um cargo a um membro do servidor.", inline=False)
        embed.add_field(name=".ban <@membro> [razão]", value="Bane um membro do servidor.", inline=False)
        embed.add_field(name=".kick <@membro> [razão]", value="Expulsa um membro do servidor.", inline=False)
        embed.add_field(name=".listavisos <@membro>", value="Exibe todos os avisos registrados para um membro.", inline=False)
        embed.add_field(name=".ping", value="Retorna a latência do bot, útil para verificar sua disponibilidade.", inline=False)
        embed.add_field(name=".removeraviso <@membro> <numero>", value="Remove um aviso de um membro do servidor.", inline=False)
        embed.add_field(name=".removercargo <@membro> <nome-do-cargo>", value="Remove um cargo de um membro específico.", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
    print("Help - Pronto!")