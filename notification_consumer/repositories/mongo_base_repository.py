class MongoBaseRepository:
    def __init__(self, db_client, collection_name):
        self._db_client = db_client
        self._collection_name = collection_name

    def insert(self, query):
        return self._db_client.insert(self._collection_name, query)
