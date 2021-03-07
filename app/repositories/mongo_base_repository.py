class MongoBaseRepository:
    def __init__(self, db_client, collection_name):
        self.db_client = db_client
        self.collection_name = collection_name

    def insert(self, query):
        return self.db_client.insert(self.collection_name, query)

    def get_by_ids(self, ids):
        return self.db_client.get_by_ids(self.collection_name, ids)
