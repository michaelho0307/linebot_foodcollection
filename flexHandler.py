import json
from linebot.models import FlexSendMessage, TextSendMessage

def get_add_menu():
    flexMessage = json.load(open('./template/add_menu.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='新增菜單', contents=flexMessage)
    return content

def get_menu_bubble(name, num, uri):
    bubble = json.load(open('./template/check_menu.json','r+',encoding='UTF-8'))
    body_content = bubble["body"]["contents"]
    body_content[1]["text"] = str(name)
    body_content[2]["text"] = f'菜單數量共計：{num} 件'
    body_content[4]["action"]["data"] = f'DEL-{name}'
    body_content[5]["action"]["uri"] = uri #modify
    body_content[6]["action"]["uri"] = uri #lookup

    footer_content = bubble["footer"]["contents"]
    footer_content[0]["action"]["data"] = f"STAR-{name}"
    return bubble

def get_menu_carousel(restaurant_list):
    restaurants = []
    for restaurant in restaurant_list:
        restaurants.append(get_menu_bubble(restaurant["name"], restaurant["num"], restaurant["uri"]))
    carousel = {
        "type": "carousel",
        "contents": restaurants
    }
    content = FlexSendMessage(alt_text='查閱菜單', contents=carousel)
    print(content)
    return content

def get_carousel(name):
    flexMessage = json.load(open('./template/carousel.json','r+',encoding='UTF-8'))
    flexMessage["body"]["contents"][3]["contents"][1]["action"]["text"] = f'我要吃{name}'
    print(flexMessage)
    content = FlexSendMessage(alt_text='旋轉轉盤', contents=flexMessage)
    return content

def get_history():
    flexMessage = json.load(open('./template/history.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='歷史訂單', contents=flexMessage)
    return content

# info = {
#    'restaurant': string,
#    'name': string,
#    'price': int,
# }
def get_reminder(info):
    restaurant = info['restaurant']
    name = info['name']
    price = info['price']
    msg = f'您有一筆來自{restaurant}的訂單，訂閱品項為{name}，消費金額一共是{price}元'
    content = TextSendMessage(msg)
    return content


def check_order(order_list):
    msg = '以下是您的訂單紀錄\n'
    for order in order_list:
        restaurant = order['restaurant']
        name = order['name']
        price = order['price']
        msg += f'{restaurant} 餐廳的 {name} 一共是 {price} 元\n'
    content = TextSendMessage(msg)
    return content
