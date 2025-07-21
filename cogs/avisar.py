import discord
from discord.ext import commands
import json
import os

class Avisar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avisar(self, ctx, user: discord.User, *, reason=None):
        if reason is None:
            await ctx.send("❌ É necessário que cite um motivo para dar um aviso a alguém!")
            return
            
        if ctx.author.guild_permissions.kick_members and ctx.author.guild_permissions.ban_members:
            if not os.path.exists('warnings.json'):
                with open('warnings.json', 'w') as f:
                    json.dump({}, f)

            try:
                with open('warnings.json', 'r') as f:
                    warnings = json.load(f)
            except json.JSONDecodeError:
                warnings = {}

            if str(user.id) not in warnings:
                warnings[str(user.id)] = []

            warnings[str(user.id)].append({
                "motivo": reason,
                "emitido_por": f"{ctx.author.mention} `({ctx.author.name})`"
            })

            with open('warnings.json', 'w') as f:
                json.dump(warnings, f, indent=4)

            await ctx.send(f"✅ {user.mention} foi avisado pelo motivo: '{reason}'\nVocê agora tem **{len(warnings[str(user.id)])}** avisos!")
        else:
            await ctx.send("❌ Você não tem permissão para usar este comando!")

async def setup(bot):
    await bot.add_cog(Avisar(bot))
    print("Avisar - Pronto!")