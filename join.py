import discord

async def setup(bot):
    @bot.tree.command(name="join", description="ボイスチャンネルに参加するよ！")
    async def join(interaction: discord.Interaction):
        """ボットをユーザーのボイスチャンネルに参加させる"""

        # ユーザーがボイスチャンネルにいるか確認
        if interaction.user.voice is None or interaction.user.voice.channel is None:
            await interaction.response.send_message("VCに参加するには、まず自分がボイスチャンネルに入ってね！", ephemeral=True)
            return

        channel = interaction.user.voice.channel  # 参加するボイスチャンネルを取得

        # すでにVCに接続しているかチェック
        if interaction.guild.voice_client is not None:
            await interaction.response.send_message("もうVCに入ってるよ！", ephemeral=True)
            return

        # VC に接続
        await channel.connect()
        await interaction.response.send_message(f" {channel.name} に参加したよ！")
