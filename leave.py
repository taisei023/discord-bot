import discord

async def setup(bot):
    @bot.tree.command(name="leave", description="ボイスチャンネルから退出するよ！")
    async def leave(interaction: discord.Interaction):
        """ボットをVCから退出させる"""

        # ボットがボイスチャンネルに接続しているかチェック
        if interaction.guild.voice_client is None:
            await interaction.response.send_message("ボイスチャンネルにいないよ！", ephemeral=True)
            return

        # 切断
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("👋 VCから退出したよ！")
