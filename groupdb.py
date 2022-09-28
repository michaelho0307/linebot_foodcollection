import pymongo
import random
import datetime
import certifi

### remember to change
client = pymongo.MongoClient("mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
database = client['LinebotDB']

groupSchema = database['groupSchema']

def groupInfoInit(gid, members):
    groupInfo = {
        'groupID': gid,
        'groupMember': members,
        'count': 0,
        'restaurants': [],
        'payment': [],
    }
    groupSchema.insert_one(groupInfo)
    return True



def checkGroup(gid, members):
    condition = {'groupID': gid}
    group = groupSchema.find_one(condition)
    if group is None:
        groupInfoInit(gid, members)
        return groupSchema.find_one(condition)
    return group

