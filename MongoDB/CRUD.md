# READ
```py
import pymongo
ATLAS_PASSWORD = "codeforfun2020"
atlas_conn = f'mongodb+srv://simon:{ATLAS_PASSWORD}@cluster0.23jm7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
with pymongo.MongoClient(atlas_conn) as mongo_client:
    db = mongo_client.scooters_DB
    collection = db.scooters1
    collection.delete_many({"saved_at": {"$lt": 1618794376}})
```