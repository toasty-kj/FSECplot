import logging
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

log_file = 'projects\main\src\logging\server.log'  # ログを保存するファイル名

# ロガーを設定してファイルにログを出力
# コンソール用のハンドラを作成して設定
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8')

file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.INFO)

# ルートロガーにファイルハンドラーを追加
logging.getLogger().addHandler(file_handler)

@app.route("/api", methods=("GET", "POST"))
def index():
    args = request.args.getlist('pathList')
    logging.info(request.args)
    return jsonify({'recievedPath': args})

if __name__ == "__main__":
    app.run(host="localhost", port=5001)

