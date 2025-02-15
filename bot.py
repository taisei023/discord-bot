import discord
import importlib
from config import TOKEN  # 環境変数を読み込む
import commands as command_loader  # commands.py を読み込む
from message_listener import handle_message  # メッセージ処理

GUILD_ID = 1256457659662733352  # ここが正しいサーバーIDか確認！

# Bot の設定
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # ボイスチャンネルの操作を有効化！

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)  # スラッシュコマンド用のツリー

    async def setup_hook(self):  # 🔧 botの起動時にコマンドをセットアップ
        print("🔍 setup_hook() が実行された")  # デバッグ用
        await command_loader.setup(self)  # `commands.py` を実行

        await self.tree.sync(guild=discord.Object(id=GUILD_ID))  # コマンドを同期
        print("✅ スラッシュコマンドを同期しました")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"✅ ログインしました: {bot.user}")

@bot.event
async def on_message(message):
    await handle_message(bot, message)  # メッセージ応答を処理

bot.run(TOKEN)
