import json
from linebot.models import FlexSendMessage

def get_add_menu():
    flexMessage = json.load(open('./template/add_menu.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='新增菜單', contents=flexMessage)
    return content