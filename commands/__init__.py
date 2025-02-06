import os
import importlib

async def setup_commands(bot):
    """ commands/ フォルダ内のすべてのコマンドを自動的に登録する """
    command_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".py") and f != "__init__.py"]

    for file in command_files:
        module = importlib.import_module(f"commands.{file}")  # `commands/` の各ファイルをインポート
        await module.setup(bot)  # 各コマンドの setup(bot) を実行
