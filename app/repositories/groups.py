from bson import ObjectId
from app.repositories.mongo_base_repository import MongoBaseRepository
from app.utils.constans import CollectionsNames


class GroupsRepository(MongoBaseRepository):
    def __init__(self, db_client):
        collection_name = CollectionsNames.GROUPS.value
        super().__init__(db_client, collection_name)

    def check_ids(self, ids):
        _ids = [ObjectId(_id) for _id in ids]
        result = self.get_by_ids(_ids)
        valid_ids = [str(obj.get("_id")) for obj in result]
        return valid_ids
