import logging
import traceback
from flask import Flask, jsonify, request
from flask_cors import CORS

from controller.controller import create_chart
from logging_initializer.init_logging import init_logging
from utility.file_handler import validate_file_path_list

app = Flask(__name__)
CORS(app)

init_logging()

@app.errorhandler(Exception)
def handle_error(e):
    traceback.print_exc()  # エラーのトレースバックを表示
    app.logger.error(f"An error occurred: {str(e)}")  # エラーメッセージをログに記録
    return "An error occurred", 500  # 適切なエラーメッセージやステータスコードを返す

@app.route("/api", methods=("GET", "POST"))
def index():
    args = request.args.getlist('pathList')
    logging.info(request.args)
    create_chart(args)
    return jsonify({'recievedPath': args})

if __name__ == "__main__":
    app.run(host="localhost", port=5001)
