import json
from linebot.models import FlexSendMessage, TextSendMessage

def getRestaurantItem(name, num, uri):
    template = json.load(open('./template/restaurantItem.json','r+',encoding='UTF-8'))

    content = template["body"]["contents"]
    content[1]["text"] = str(name)
    content[2]["text"] = f'菜單數量共計：{num} 件'
    content[4]["action"]["data"] = f'DEL-{name}'
    content[5]["action"]["uri"] = uri #modify
    content[6]["action"]["uri"] = uri #lookup

    content = template["footer"]["contents"]
    content[0]["action"]["data"] = f"STAR-{name}"
    return template

def getRestaurantItems(itemList):
    items = []
    for item in itemList:
        items.append(getMenuItem(item['name'], item['num'], item['uri']))
    carousel = {
        "type": "carousel",
        "contents": items
    }
    content = FlexSendMessage(alt_text='查閱菜單', contents=carousel)
    return content

def getAddRestaurant():
    template = json.load(open('./template/addRestaurant.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='新增菜單', contents=template)
    return content

def getRestaurantDecider(name):
    template = json.load(open('./template/restaurantDecider.json','r+',encoding='UTF-8'))
    template["body"]["contents"][3]["contents"][1]["action"]["text"] = name
    content = FlexSendMessage(alt_text='旋轉轉盤', contents=template)
    return content

def getReminder(itemList):
    if len(itemList)==0: return TextSendMessage('您目前尚無訂單')
    msg = '您有以下訂單'
    for item in itemList:
        restaurnt = itemList['restaurant']
        name = itemList['name']
        price = itemList['price']
        msg += f'來自{restaurant}的訂單，訂閱品項為{name}，消費金額一共是{price}元\n'
    content = TextSendMessage(msg)
    return content

def getOrderRecord():
    template = json.load(open('./template/restaurantDecider.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='歷史訂單', contents=template)
    return content

def checkOrderRecord():
    pass

def getStarRestaurantItem(name, num, uri):
    pass

def getStarRestaurantItems(itemList):
    pass

