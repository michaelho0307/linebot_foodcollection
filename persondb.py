import pymongo


'''
personSchema = {
    id: ObjectId,
    LineID: string,
    state: int,
    mode: int,
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
    star: [index_1, index_2, ...],
    payment: [
        {
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
        LineID: LineID,
        state: 0,
        mode: 0,
        restaurnts: [],
        star: [],
        payment: [],
        history: []
    }
    personSchema.insert_one(Info)
    return True

def getUser(personSchema, LineID):
    condition = { 'LineID': LineID }
    user = userInfo.find_one(condition)
    if user is None:
        userInfoInit(personSchema, LineID)
        return userInfo.find_one(condition)
    return user


def get_resaurant(personSchema, LineID):
    # return the list of my restaurant which contains name(string), num(int), uri(string).
    restaurant_list = [
        {
            'name': 'test',
            'num': 10,
            'uri': 'https://www.youtube.com/watch?v=0-4mm0e2h44'
        }
    ]
    return restaurant_list

def get_favorite(personSchema, LineID):
    # return a list of restaurants, which should contain 'name', 'num', 'uri'
    pass


def get_random_restaurant(personSchema, LineID):
    # return a random restaurant' s name -> string
    pass

def get_specific_time_order(personSchema, LineID, time):
    # return the history order within the specific time.
    pass

def add_restaurent(personSchema, LineID, restaurant):
    pass

def star_restaurant(personSchema, LineID, restaurant):
    pass