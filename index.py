# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('dwzJBC7/J1LV0BFLiuWFNQay6/b+VU4O7FfuWexUPrOvHVKgzxhJaeSB0PcqJ13s+xuPca5neo4eQnCq7T/rcrZyTVJY06HlQ+8phJPchWL/fxRLZOO9FuA6NJ/y683Cxqd+GsltIOKEQEeWjfstlAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b212af754eba3e46229e1d1b7f531121')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()