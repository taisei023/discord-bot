import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数からトークンを取得
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Botを起動
bot.run(TOKEN)
