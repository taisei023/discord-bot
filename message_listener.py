from config import TARGET_CHANNEL_ID  # 設定をインポート

# 特定のキーワードに反応する辞書
TRIGGER_WORDS = {
    "こんにちは": "おー！こんにちは！元気しとー？",
    "おはよう": "おはよー！今日も頑張ろうばい！",
    "ばいばい": "またねー！元気でねー！"
}

async def handle_message(bot, message):

    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return
    
    # 指定したチャンネル以外では無視する
    if message.channel.id != TARGET_CHANNEL_ID:
        return

    # キーワードに反応する
    for word, response in TRIGGER_WORDS.items():
        if word in message.content:
            await message.channel.send(response)
            break