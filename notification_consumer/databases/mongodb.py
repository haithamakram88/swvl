from pymongo import MongoClient

from notification_consumer import config


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
