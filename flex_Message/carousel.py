import json
from linebot.models import FlexSendMessage

def get_carousel():
    flexMessage = json.load(open('./template/carousel.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='旋轉轉盤', contents=flexMessage)
    return content