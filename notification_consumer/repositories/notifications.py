from notification_consumer.repositories.mongo_base_repository import MongoBaseRepository
from notification_consumer.utils.constans import CollectionsNames


class NotificationsRepository(MongoBaseRepository):
    def __init__(self, db_client):
        collection_name = CollectionsNames.NOTIFICATIONS.value
        super().__init__(db_client, collection_name)


