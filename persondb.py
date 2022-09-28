import pymongo
import random
import datetime
import certifi

### remember to change
client = pymongo.MongoClient("mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
database = client['LinebotDB']

personSchema = database['personSchema']

# User-Related

def userInfoInit(LineID) -> bool:
    userInfo = {
        'LineID': LineID,
        'groupID': '',
        'count': 0,
        'restaurants': [],
        'star': [],
        'payment': [],
        'history': []
    }
    personSchema.insert_one(userInfo)
    return True

def checkUser(LineID) -> dict:
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    if user is None:
        userInfoInit(LineID)
        return personSchema.find_one(condition)
    return user

def testCheckUser():
    checkUser('123')
    return

#testCheckUser()

# Restaurant-Related

def getRestaurants(LineID) ->list:
    user = checkUser(LineID)
    items = user['restaurants']
    itemList = []
    for item in items:
        name =  item['name']
        num  =  len(item['menu'])
        uri  =  f'https://www.google.com/search?q={name}&rlz=1C1CHBF_zh-TWTW904TW904&oq={name}&aqs=chrome.0.0i355i512j46i175i199i512j0i512j0i15i30l4.1712j0j15&sourceid=chrome&ie=UTF-8'
        itemDict = {
            'name': name,
            'num': num,
            'uri': uri
        }
        itemList.append(itemDict)
    return itemList

def getStarRestaurantItems(starList):
    user = checkUser(LineID)
    items = user['restaurants']
    itemList = []
    for item in items:
        if item['index'] in starList:
            name =  item['name']
            num  =  len(item['menu'])
            uri  =  f'https://www.google.com/search?q={name}&rlz=1C1CHBF_zh-TWTW904TW904&oq={name}&aqs=chrome.0.0i355i512j46i175i199i512j0i512j0i15i30l4.1712j0j15&sourceid=chrome&ie=UTF-8'
            itemDict = {
                'name': name,
                'num': num,
                'uri': uri
            }
            itemList.append(itemDict)
    return itemList

def getRandomRestaurant(LineID) -> str:
    user = checkUser(LineID)
    items = user['restaurants']
    if len(items) == 0: return '您目前並沒有任何餐廳'
    index = random.randint(0, len(items)-1)
    msg = '我要吃' + items[index]['name']
    return msg


# Payment-Related

def getPayment(LineID) ->dict:
    user = checkUser(LineID)
    content = user['payment']
    return content

# Star-Related

def getStarList(LineID) ->list:
    user = checkUser(LineID)
    itemsList = user['star']
    return itemList

# History-Related

def getHistory(LineID)->list:
    user = checkUser(LineID)
    itemList = user['history']
    return itemList

def getTimeInterval(str1, str2):
    date1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    return num

def getSpecificTimeOrder(LineID, interval):
    items = getHistory(LineID)
    time = datetime.datetime.now()
    itemList = []
    if interval == 'NOW': return items[-1]
    timeInterval = 7 if interval == 'WEEK' else 30
    for item in items:
        if getTimeInterval(item['time'], time) <= timeInterval: itemList.append(item)
    return itemList
    



def add_restaurant(personSchema, LineID, restaurant):
    condition = {'LineID': LineID}
    user = personSchema.find_one(condition)
    restaurants = user.get('restaurants') if user.get('restaurants') else []
    checker = [True for r in restaurants if r["name"] == restaurant]
    if not any(checker):
        restaurants.append(
            {
                "name": restaurant,
                "menu": [],
            }
        )
        val = {"$set": {'restaurants': restaurants}}
        personSchema.update_one(condition, val)
        return True
    return False

    
# Postback-Related

def delFunc(name, LineID):
    user = checkUser(LineID)
    pass

def starFunc(name, LineID):
    user = checkUser(LineID)
    pass
    

