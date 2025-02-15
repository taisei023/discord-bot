import discord
import os
import asyncio
from discord import FFmpegPCMAudio

AUDIO_PATH = "audio/don.mp3"  # 再生するMP3ファイルのパス

async def setup(bot):
    @bot.tree.command(name="play", description="現在ボイスチャンネルにいるボットが音楽を再生します")
    async def play(interaction: discord.Interaction):
        voice_client = interaction.guild.voice_client  # 現在のVC情報を取得

        if voice_client is None:
            await interaction.response.send_message("ボイスチャンネルに接続していません。先に `/join` を実行してください。")
            return

        if not os.path.exists(AUDIO_PATH):
            await interaction.response.send_message(f"音楽ファイルが見つかりません: {AUDIO_PATH}")
            return

        if voice_client.is_playing():
            await interaction.response.send_message("現在、すでに音楽を再生中です。")
            return

        ffmpeg_options = {
            'options': '-vn'  # 映像を無視して音声だけ再生
        }
        voice_client.play(FFmpegPCMAudio(AUDIO_PATH, **ffmpeg_options))

        await interaction.response.send_message(f"{voice_client.channel.name} で音楽を再生しています。")

        # 再生が終わるまで待機
        while voice_client.is_playing():
            await asyncio.sleep(1)