from pymongo import MongoClient
from app import config


class MongodbClient:
    def __init__(self):
        try:
            uri = "mongodb://{}:{}".format(config.MONGODB_HOST, config.MONGODB_PORT)
            self.client = MongoClient(uri)
            self.db = self.client[config.MONGODB_DATABASE]
        except Exception as e:
            print(e)

    def insert(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert(data)

    def get_by_ids(self, collection_name, ids):
        collection = self.db[collection_name]
        return collection.find({"_id": {"$in": ids}})
