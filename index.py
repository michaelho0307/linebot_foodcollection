from __future__ import unicode_literals
### modules
# line bot sdk
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    PostbackEvent
)

from flask import Flask, request, abort
import pymongo
import os
import re

from flex_Message import (
    add_menu, carousel, check_menu, 
    favorite, reminder
)

app = Flask(__name__)

# LINE BOT basic info
line_bot_api = LineBotApi(os.environ["ChannelAccessToken"])
handler = WebhookHandler(os.environ["ChannelSecret"])
client = pymongo.MongoClient("mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority")
database = client['LinebotDB']
personSchema = database['personSchema']
groupSchema = database['groupSchema']


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



# Message Event
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).strip()
    source_type = event.source.type

    # User-related Development
    if source_type == 'user':
        profile = line_bot_api.get_profile(event.source.user_id)
        user_name = profile.display_name
        uid = profile.user_id

        #user = userInfo.getUser(personSchema,uid)

        ### default functionality
        if re.match("@查閱餐廳菜單" ,msg): ##### check_menu
            restaurant_list = [
                {
                    'name': 'test',
                    'num': 10,
                    'uri': 'https://www.youtube.com/watch?v=0-4mm0e2h44'
                }
            ]
            content = check_menu.get_carousel(restaurant_list)
            print(content)
            line_bot_api.push_message(uid, content)

        elif re.match("@新增菜單", msg): ##### add_menu
            content = add_menu.get_add_menu()
            line_bot_api.push_message(uid, content)

        elif re.match("@應付金額及點餐提醒"): ##### reminder
            pass
        
        elif re.match("@我的最愛", msg): ##### favorite
            pass

        elif re.match("@旋轉轉盤", msg): ##### carousel
            pass


        

        ##### @新增菜單
        elif re.match('探索更多周邊美食', msg):
            pass
        
        elif re.match('自行加入餐廳',msg):
            pass

        elif re.match('查看餐廳列表', msg):
            pass
        

    # Group-related Development
    elif source_type == 'group':
        pass


# Postback Event
@handler.add(PostbackEvent)
def handle_postback(event):
    msg = event.postback.data
    source_type = event.source.type

    if source_type == 'user':
        profile = line_bot_api.get_profile(event.source.user_id)
        user_name = profile.display_name
        uid = profile.user_id

        if re.match('ADD',msg):
            pass
        
        if re.match('DEL', msg):
            pass
        
        if re.match('STAR', msg):
            pass

    elif source_type == 'group':
        pass

if __name__ == "__main__":
    app.run()
