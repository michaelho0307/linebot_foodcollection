from __future__ import unicode_literals
### modules
# line bot sdk
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage



from flask import Flask, request, abort
import pymongo
import os
import re

app = Flask(__name__)

# LINE BOT basic info
line_bot_api = LineBotApi(os.environ["ChannelAccessToken"])
handler = WebhookHandler(os.environ["ChannelSecret"])
cluster = pymongo.MongoClient("mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority")

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


# talk
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    msg = str(event.message.text).strip()
    source_type = event.source.type
    print(cluster)

    if source_type == 'user':
        profile = line_bot_api.get_profile(event.source.user_id)
        user_name = profile.display_name
        uid = profile.user_id

        user = userInfo.getUser(uid)



    
    elif source_type == 'group':
        pass
    







if __name__ == "__main__":
    app.run()
