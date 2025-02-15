import discord
from config import TOKEN
from commands import setup_commands  
from message_listener import handle_message

intents = discord.Intents.default()
intents.message_content = True

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

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

bot.run(TOKEN)
