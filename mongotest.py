import pymongo
client = pymongo.MongoClient("mongodb+srv://hardikraval:hardik999@atlascluster.kjdhjgo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"hardik",
    "email":"hardik9@gmail.com",
    "surname":"raval",
}
db1=client['mongotest']
coll = db1['test']
coll.insert_one(d)