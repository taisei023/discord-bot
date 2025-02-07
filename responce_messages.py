import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
TARGET_CHANNEL_ID = 1256457659662733357

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Botの設定
intents = discord.Intents.default() # Botの権限を取得
intents.message_content = True  # メッセージの取得を許可

# commands.Bot ではなく discord.Clientを使う
# discord.Clientとはbotの基本的な機能を提供するクラス
class MyBot(discord.Client):
    def __init__(self): # コンストラクタでMyBotのクラスインスタンスを作った際に最初に実行される関数、__init__()には自動的にselfを渡そうとするのがpython
        super().__init__(intents=intents) # 親クラス(discord.Client)の__init__()を呼ぶためのもの、discord.Clientを作るときにintentsを設定する必要がある
        self.tree = discord.app_commands.CommandTree(self) # self.treeはスラッシュコマンドを管理するためのもの

# 特定のキーワードに反応
TRIGGER_WORDS = {
    "こんにちは": "おー！こんにちは！元気しとー？",
    "おはよう": "おはよー！今日も頑張ろうばい！",
    "ばいばい": "またねー！元気でねー！"
}

# Botを作成
bot = MyBot()

# asyncを使うことにより非同期処理ができる→他の処理と並行して動ける
# また、async関数の中ではawaitを使える
# awaitを使うことによって時間がかかる処理が終わるまで待てる
# この場合、メッセージを送る処理は時間がかかるのでそれが終わるまで待つことができる

# @bot.eventはDiscord APIのメッセージ受信イベントに対応する関数であることがわかる
@bot.event
async def on_ready(): # on_ready()はBotがログインしたときに1回だけ呼ばれる
    await bot.tree.sync()  # スラッシュコマンドを同期
    print(f"ログインしました: {bot.user}")# bot.userはbotの名前

@bot.tree.command(name="hello", description="このコマンドは「やっほー！」と返します")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("やっほー！")

@bot.event
async def on_message(message): # on_message()は誰かがメッセージを送信するたびに呼ばれる
    if message.author == bot.user: # message.authorは送った人を取得する
        return  # Bot自身のメッセージには反応しない
    
    # 指定したチャンネル以外では無視する
    if message.channel.id != TARGET_CHANNEL_ID:
        return  # 指定したチャンネル以外では何もしない

    for word, response in TRIGGER_WORDS.items(): # これはTRIGGER_WORDS.items()で登録された単語と返信メッセージのペアを順番通りに取り出す
        if word in message.content: # message.contentはユーザーが送信したメッセージの内容,メッセージの中に登録されている単語が含まれているかをチェック
            await message.channel.send(response) #見つかったら返信メッセージを送信
            break  # 1つ目のマッチで返信して終了

# Bot起動
bot.run(TOKEN)
