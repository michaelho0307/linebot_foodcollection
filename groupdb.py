import pymongo
import random
import datetime
import certifi

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    PostbackEvent
)


### remember to change
client = pymongo.MongoClient("mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
database = client['LinebotDB']

groupSchema = database['groupSchema']

def groupInfoInit(gid):
    members = line_bot_api.get_group_member_ids(gid)
    groupInfo = {
        'groupID': gid,
        'groupMember': members,
        'count': 0,
        'restaurants': [],
        'payment': [],
    }
    groupSchema.insert_one(groupInfo)
    return True



def checkGroup(gid):
    condition = {'groupID': gid}
    group = groupSchema.find_one(condition)
    if group is None:
        groupInfoInit(gid)
        return groupSchema.find_one(condition)
    return group

