import discord
import os
import asyncio
import datetime
from discord import FFmpegPCMAudio

AUDIO_PATH = "audio/don.mp3"  # 時報の音声ファイル

class TimeSignal:
    def __init__(self, bot):
        self.bot = bot
        self.voice_loop_running = False  # 時報ループが動作中かどうかのフラグ

    async def time_signal_loop(self):
        """ 毎時00分ちょうどに音声を再生する """
        self.voice_loop_running = True
        while self.voice_loop_running:
            now = datetime.datetime.utcnow()
            next_hour = (now + datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            wait_time = (next_hour - now).total_seconds()

            print(f"[{now.strftime('%H:%M:%S')}] 次の時報: {next_hour.strftime('%H:%M:%S')} UTC (あと {int(wait_time)} 秒)")

            await asyncio.sleep(wait_time)  # 次の00分まで待機

            voice_client = self.bot.guilds[0].voice_client
            if voice_client and os.path.exists(AUDIO_PATH):
                ffmpeg_options = {'options': '-vn'}
                voice_client.play(FFmpegPCMAudio(AUDIO_PATH, **ffmpeg_options))
                print(f"[{datetime.datetime.utcnow().strftime('%H:%M:%S')}] 時報を再生しました")

    async def start_time_signal(self):
        """ ボイスチャンネルにいる間、時報ループを開始 """
        if not self.voice_loop_running:
            await self.time_signal_loop()

    async def on_voice_state_update(self, member, before, after):
        """ ボイスチャンネルの接続状況を監視 """
        if member.id == self.bot.user.id:  # ボット自身の動作のみ監視
            if after.channel is not None and not self.voice_loop_running:
                print(f"ボイスチャンネル {after.channel.name} に接続しました。時報ループ開始。")
                await self.start_time_signal()
            elif after.channel is None:
                print("ボイスチャンネルから切断しました。時報ループ終了。")
                self.voice_loop_running = False
