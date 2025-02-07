import discord
from config import TOKEN  # 環境変数を読み込む
from commands import setup_commands  # コマンドをセットアップ
from message_listener import handle_message  # メッセージ処理

# Bot の設定
intents = discord.Intents.default()
intents.message_content = True

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self): # botの起動時にコマンドをセットアップ
        await setup_commands(self)  # コマンドフォルダから全部読み込む
        await bot.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}") # fを記述することによって文字列の中に変数の値を埋め込むことができる

@bot.event
async def on_message(message):
    await handle_message(bot, message)  # メッセージ応答を処理

bot.run(TOKEN)
