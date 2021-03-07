import pytest
from app.databases.mongodb import MongodbClient

@pytest.mark.parametrize("collection_name,data,result", [("users", {"name": "test-haitham"}, "test-haitham"),
                                                         ("groups", {"name": "test-group",
                                                                     "users_ids": ["603f96411ab33032f86d33af"]},
                                                          "test-group")],
                        ids=["test-users-collection", "test-groups-collection"])
def test_insert(collection_name, data, result):
    mongo_client = MongodbClient()
    mongo_client.insert(collection_name, data)
    collection = mongo_client.db[collection_name]
    response = collection.find({"name": data.get("name")})
    assert response[0].get("name") == result



def test_get_by_ids():
    mongo_client = MongodbClient()
    created_user1 = mongo_client.insert("users", {"name": "test1-haitham"})
    created_user2 = mongo_client.insert("users", {"name": "test2-haitham"})
    result = mongo_client.get_by_ids("users", [created_user1, created_user2])
    valid_ids = [str(obj.get("_id")) for obj in result]
    result_ids = [str(created_user1), str(created_user2)]
    assert valid_ids == result_ids
