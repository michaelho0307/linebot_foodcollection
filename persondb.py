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


        