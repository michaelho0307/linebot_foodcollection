import json
from linebot.models import FlexSendMessage

def get_history():
    flexMessage = json.load(open('./template/history.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='歷史訂單', contents=flexMessage)
    return content