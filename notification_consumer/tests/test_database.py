import pytest
from bson import ObjectId

from notification_consumer.databases.mongodb import MongodbClient
from notification_consumer.services.notification_service import NotificationService


def test_create_notification_in_db():
    data = {
        "notification_type": "sms_notification",
        "message": "test",
        "message_type": "single",
        "ids": ["60422e21d5c54a75349e6943"],
        "time_of_return": "27/2/2021 10:30:20"
    }
    mongo = MongodbClient()
    notification_service = NotificationService(data.get("notification_type"), data.get("message_type"))
    notification_id = notification_service.create_notification_in_db(data)
    collection = mongo.db["notifications"]
    response = collection.find({"_id": ObjectId(notification_id)})
    assert response[0].get("notification_type") == data.get("notification_type")
    assert response[0].get("message") == data.get("message")
    assert response[0].get("message_type") == data.get("message_type")
    assert response[0].get("ids") == data.get("ids")
    assert response[0].get("time_of_return", "") == ""


