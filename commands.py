import os
import importlib

async def setup(bot):
    """commands フォルダ内のスラッシュコマンドをすべて読み込む"""
    
    command_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".py") and f != "__init__.py"]

    for file in command_files:
        module = importlib.import_module(f"commands.{file}")  # `commands/` 内の各ファイルをロード
        print(f"🔄 {file} をロード中...")  # 確認用ログ
        await module.setup(bot)  # 各コマンドの `setup(bot)` を実行
