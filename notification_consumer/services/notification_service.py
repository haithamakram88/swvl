from notification_consumer.databases.mongodb import MongodbClient
from notification_consumer.repositories.notifications import NotificationsRepository
from notification_consumer.utils.response import Response
from notification_consumer.utils.constans import MessageTypes


class NotificationService:

    def __init__(self, notification_type, message_type):
        self.notification_type = notification_type
        self.message_type = message_type
        self.client = MongodbClient()
        self.notification_repository = NotificationsRepository(self.client)

    def send_notification(self, data):
        response = Response()
        try:
            if self.message_type == MessageTypes.SINGLE.value:
                response = self.notification_type.send_single_notification(data)

            elif self.message_type == MessageTypes.GROUP.value:
                response = self.notification_type.send_group_notification(data)

            if response.data.get("is_sent", None):
                self.create_notification_in_db(data)

        except Exception as e:
            print(e)
            response.status = False
            response.exception = e

        return response

    def create_notification_in_db(self, data):
        data.pop("time_of_return")
        return self.notification_repository.insert(data)
