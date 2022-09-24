import pymongo
import random
import datetime
import certifi

'''
personSchema = {
    id: ObjectId,
    LineID: string,
    state: int,
    mode: int,
    count: int,
    restaurants: [
        {
            name: string,
            index: int,
            menu: [
                {
                    item: string,
                    price: int,
                },
            ]
        }
    ],
    star: [index_1, index_2, ...], -> int
    payment: [
        {
            restaurant: string,
            name: string,
            price: int,
        }
    ],
    history: [
        {
            name: string,
            price: int,
            time: string,
        }
    ]
}
'''


def userInfoInit(personSchema, LineID):
    userInfo = {
        'LineID': LineID,
        'state': 0,
        'mode': 0,
        'count': 0,
        'restaurants': [],
        'star': [],
        'payment': [],
        'history': []
    }
    personSchema.insert_one(userInfo)
    return True


def getUser(personSchema, LineID):
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    if user is None:
        userInfoInit(personSchema, LineID)
    return

#getUser(personSchema, LineID)


restaurant_info = {
    'name': '食堂1',
    'index': 0,
    'menu': [
        {
            'item': 'food1',
            'price': 10,
        },
        {
            'item': 'food2',
            'price': 20,
        }
    ]
}


def update_restaurant(personSchema, LineID, restaurant_info):
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    restaurants = user['restaurants']
    restaurants.append(restaurant_info)
    val = {"$set": {'restaurants': restaurants}}
    personSchema.update_one(condition, val)
    return


def get_resaurant(personSchema, LineID):
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    restaurants = user['restaurants']

    restaurant_list = []
    for restaurant in restaurants:
        name = restaurant['name']
        num = len(restaurant['menu'])
        restaurant_dict = {
            'name': name,
            'num': num,
            'uri': f'https://www.google.com/search?q=test'
        }
        restaurant_list.append(restaurant_dict)
    return restaurant_list


def get_favorite(personSchema, LineID):
    # return a list of restaurants, which should contain 'name', 'num', 'uri'
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    stars = user['star']
    restaurants = user['restaurants']
    restaurant_list = []
    for restaurant in restaurants:
        if restaurant['index'] in stars:
            name = restaurant['name']
            num = len(restaurant['menu'])
            restaurnt_dict = {
                'name': name,
                'num': num,
                'uri': f'https://www.google.com/search?q={name}&rlz=1C1CHBF_zh-TWTW904TW904&oq={name}&aqs=chrome.0.0i355i512j46i175i199i512j0i512j0i15i30l4.1712j0j15&sourceid=chrome&ie=UTF-8'
            }
            restaurant_list.append(restaurnt_dict)
    return restaurant_list


def get_random_restaurant(personSchema, LineID):
    # return a random restaurant' s name -> string
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    restaurnts = user['restaurants']
    index = random.randint(0, len(restaurnts)-1)
    name = restaurnts[index]['name']
    return name


def get_day_interval(str1, str2):
    date1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    return num

# three choices: now, week, month


def get_specific_time_order(personSchema, LineID, interval):
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    history = user['history']
    time = datetime.datetime.now()
    order_list = []
    time_interval = 7 if interval == 'WEEk' else 30

    if interval == 'NOW':
        return history[-1]
    else:
        for order in history:
            if get_day_interval(order['time'], time) <= time_interval:
                order_list.append(order)
    return order_list


def get_reminder(personSchema, LineID):
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    payment = user['payment']
    return payment


def add_restaurant(personSchema, LineID, restaurant):
    # condition = {'LineID': LineID}
    # user = personSchema.find_one(condition)
    # restaurants = user['restaurants']
    # restaurants.append(
    #     {
    #         "name": restaurant,
    #         "menu": [],
            
    #     }
    # )
    # val = {"$set": {'restaurants': restaurants}}
    # personSchema.update_one(condition, val)
    return


def star_restaurant(personSchema, LineID, restaurant):
    pass


def del_restaurant(personSchema, LineID, restaurant):
    pass
