# import logging
# from utility.file_handler import create_file_if_not_exists


# def init_logging():
#     log_file = 'server.log'  # ログを保存するファイル名
#     create_file_if_not_exists(log_file)
#     # ロガーを設定してファイルにログを出力
#     # コンソール用のハンドラを作成して設定
#     logging.basicConfig(level=logging.INFO,
#                         format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8')

#     file_handler = logging.FileHandler(log_file, encoding='utf-8')
#     file_handler.setLevel(logging.INFO)

#     # ルートロガーにファイルハンドラーを追加
#     logging.getLogger().addHandler(file_handler)