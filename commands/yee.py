import discord

async def setup(bot):
    
    @bot.tree.command(name="yee", description="このコマンドは「イェーイ」と返します")
    async def yee(interaction: discord.Interaction):
        await interaction.response.send_message("イェーイ")