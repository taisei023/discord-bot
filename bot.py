import discord
from config import TOKEN
from commands import setup_commands  
from message_listener import handle_message
from time_signal import TimeSignal  # 時報機能をインポート

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # VCの状態変化を検知するために必要

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        self.time_signal = TimeSignal(self)  # 時報機能を初期化

    async def setup_hook(self):
        await setup_commands(self)
        print("全コマンドを追加しました")

        await self.tree.sync()
        print("スラッシュコマンドを同期しました")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")

@bot.event
async def on_message(message):
    await handle_message(bot, message)

@bot.event
async def on_voice_state_update(member, before, after):
    """ ボットのVC接続状態が変化したときに `time_signal.py` の処理を実行 """
    await bot.time_signal.on_voice_state_update(member, before, after)

bot.run(TOKEN)
