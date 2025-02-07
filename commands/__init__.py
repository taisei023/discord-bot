import os
import importlib

async def setup_commands(bot):
    # このファイルがあるパスを取得したあとにこのファイル以外の語尾が.pyで終わるファイルをリスト化、その際に.pyを切り落とす
    command_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".py") and f != "__init__.py"]

    for file in command_files:
        module = importlib.import_module(f"commands.{file}")  # `commands/` の各ファイルをインポート
        print(f"{file} をロード中...")  # 確認用ログ
        await module.setup(bot)  # 各コマンドの setup(bot) を実行
        print(f"{file} をロード完了")  # 確認用ログ