import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Botの設定
intents = discord.Intents.default() # Botの権限を取得
intents.message_content = True  # メッセージの取得を許可
bot = commands.Bot(command_prefix="!", intents=intents) # Botのインスタンスをcommands.Botで作る

TARGET_CHANNEL_ID = 1256457659662733357

# 特定のキーワードに反応
TRIGGER_WORDS = {
    "こんにちは": "おー！こんにちは！元気しとー？",
    "おはよう": "おはよー！今日も頑張ろうばい！",
    "ばいばい": "またねー！元気でねー！"
}

@bot.event
async def on_ready(): # on_ready()はBotがログインしたときに1回だけ呼ばれる
    print(f"ログインしました: {bot.user}")# bot.userはbotの名前

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
    
    await bot.process_commands(message)  # コマンド処理も実行

# Bot起動
bot.run(TOKEN)
