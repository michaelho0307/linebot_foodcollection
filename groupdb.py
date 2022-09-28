import pymongo
import random
import datetime
import certifi

### remember to change
client = pymongo.MongoClient("mongodb+srv://michaelho:root@cluster0.kgvqwtd.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
database = client['LinebotDB']

groupSchema = database['groupSchema']