from __future__ import unicode_literals

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
import certifi
from dotenv import load_dotenv
import flexHandler
import persondb
import groupdb

app = Flask(__name__)

if os.environ.get("ChannelAccessToken") == None:
    load_dotenv()

# LINE BOT basic info
line_bot_api = LineBotApi(os.environ["ChannelAccessToken"])
handler = WebhookHandler(os.environ["ChannelSecret"])
client = pymongo.MongoClient(
    "mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
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

        ### default functionality
        if re.match("@查閱餐廳菜單" ,msg): ##### check_menu
            itemList = persondb.getRestaurants(uid)
            content = flexHandler.getRestaurantItems(itemList) if len(itemList) else TextSendMessage('您目前沒有加入餐廳')
            line_bot_api.push_message(uid, content)

        elif re.match("@新增餐廳", msg): ##### add_menu
            content = flexHandler.getAddRestaurant()
            line_bot_api.push_message(uid, content)

        
        elif re.match("@應付金額及點餐提醒",msg): ##### reminder
            itemList = persondb.getPayment(uid)
            content = flexHandler.getReminder(itemList)
            line_bot_api.push_message(uid, content)
        
        
        elif re.match("@我的最愛", msg): ##### favorite
            starList = persondb.getStarList(uid)
            itemList = persondb.getStarRestaurantItems(uid, starList)
            content = flexHandler.getStarRestaurantItems(itemList) #if len(itemList) else TextSendMessage(text='您目前沒有最愛餐廳')
            line_bot_api.push_message(uid, content)

        elif re.match("@旋轉轉盤", msg): ##### carousel
            item = persondb.getRandomRestaurant(uid)
            content = flexHandler.getRestaurantDecider(item)
            line_bot_api.push_message(uid, content)
        
        
        elif re.match("@歷史訂單",msg): ##### history
            content = flexHandler.getOrderRecord()
            line_bot_api.push_message(uid, content)

        ### @查閱餐廳菜單：no message event.

        # @新增菜單
        elif re.match('探索更多周邊美食', msg):
            pass

        ### @應付金額及點餐提醒

        ### @我的最愛
        
        ### @旋轉轉盤
        
        ##### @歷史訂單
        elif re.match('查看當月訂單',msg):
            itemList = persondb.getSpecificTimeOrder(uid, 'MONTH')
            content = flexHandler.checkOrderRecord(itemList)
            line_bot_api.push_message(uid,content)

        elif re.match('查看一周訂單', msg):
            itemList = persondb.getSpecificTimeOrder(uid, 'WEEK')
            content = flexHandler.checkOrderRecord(itemList)
            line_bot_api.push_message(uid,content)

        elif re.match('查看最新訂單', msg):
            itemList = persondb.getSpecificTimeOrder(uid, 'NOW')
            content = flexHandler.checkOrderRecord(itemList)
            line_bot_api.push_message(uid, content)

    # Group-related Development
    elif source_type == 'group':
        gid = event.source.group_id
        uid = event.source.user_id
        
        if re.match('我餓了', msg):
            content = flexHandler.getFunctionList()
            line_bot_api.push_message(gid, content)
        
        elif re.match('@旋轉轉盤', msg):
            item = groupdb.getRandomRestaurant(gid)
            content = flexHandler.getRestaurantDecider(item)
            line_bot_api.push_message(gid, content)

        elif re.match('@匯入餐廳', msg):
            content = flexHandler.getRestaurantImporter(uid)
            line_bot_api.push_message(uid, content)

        elif re.match('@查閱餐廳', msg):
            content = flexHandler.getRestaurantChecker()
            line_bot_api.push_message(gid, content)
        
        elif re.match('@開始訂餐',msg):
            _ , name = msg.split('-')
            print(name)
            content = flexHandler.getOrderStarter(name)
            line_bot_api.push_message(gid, content)

        elif re.match('@訂餐統計', msg):
            content = flexHandler.getOrderStatistic()
            line_bot_api.push_message(gid, content)


# Postback Event 
@handler.add(PostbackEvent)
def handle_postback(event):
    msg = event.postback.data
    source_type = event.source.type

    if source_type == 'user':
        profile = line_bot_api.get_profile(event.source.user_id)
        user_name = profile.display_name
        uid = profile.user_id
        
        key, val = msg.split('-')

        if re.match('DEL', msg):
            persondb.delFunc(uid, val)

    elif source_type == 'group':
        gid = event.source.group_id
        uid = event.source.user_id
        if re.match('SEND', msg):
            content = flexHandler.getOrderStarter()
            line_bot_api.push_message(gid, content)


if __name__ == "__main__":
    app.run()
