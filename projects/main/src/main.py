import logging
import traceback
from flask import Flask, jsonify, request
from flask_cors import CORS

from controller.controller import create_chart
from logging_initializer.init_logging import init_logging

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
    """渡された変数を用いてプロットを行う"""
    logging.info(request.args)
    path_list = request.args.getlist('pathList')
    title = request.args.get('title')
    is_gfp_or_typ = request.args.get('fluorescence')
    create_chart(path_list=path_list,title=title, is_gfp_or_typ=is_gfp_or_typ)
    return jsonify({'recievedPath': path_list})

@app.route("/api/get-default-data-title-name")
def _get_default_data_name():
    return jsonify({'data':'WIP'})

if __name__ == "__main__":
    app.run(host="localhost", port=5001)
