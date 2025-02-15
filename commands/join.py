import discord
from config import VOICE_CHANNEL_ID  # ボイスチャンネルのIDを読み込む

async def setup(bot):
    @bot.tree.command(name="join", description="指定のボイスチャンネルに接続します")
    async def join(interaction: discord.Interaction):
        # ギルド（サーバー）のオブジェクトからボイスチャンネルを取得
        channel = interaction.guild.get_channel(VOICE_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message("指定されたボイスチャンネルが見つかりません。")
            return

        if not isinstance(channel, discord.VoiceChannel):
            await interaction.response.send_message("指定されたIDはボイスチャンネルではありません。")
            return

        if interaction.guild.voice_client:
            await interaction.response.send_message(f"すでに {interaction.guild.voice_client.channel} に接続しています。")
            return

        await channel.connect()
        await interaction.response.send_message(f"{channel.name} に接続しました。")
