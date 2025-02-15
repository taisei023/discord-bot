import os
import importlib

async def setup_commands(bot):
    # このファイルがあるパスを取得したあとにこのファイル以外の語尾が.pyで終わるファイルをリスト化、その際に.pyを切り落とす
    command_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".py") and f != "__init__.py"]

    print(f"ロードするファイル一覧: {command_files}")  # ここで確認！

    for file in command_files:
        try:
            module = importlib.import_module(f"commands.{file}")
            print(f"{file} をロード中...")  
            await module.setup(bot)  
            print(f"{file} をロード完了")
        except Exception as e:
            print(f"{file} のロード中にエラー発生: {e}")  # エラー内容を出力