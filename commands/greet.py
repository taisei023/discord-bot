import discord

async def setup(bot):
    """ /greet コマンドの設定 """
    
    @bot.tree.command(name="greet", description="指定した名前の人に挨拶するよ！")
    @discord.app_commands.describe(name="挨拶する相手の名前")
    async def greet(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f"やっほー！{name}！")