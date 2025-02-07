import os
from dotenv import load_dotenv

# 環境変数をロード
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Bot の設定
TARGET_CHANNEL_ID = 1256457659662733357