from notification_consumer.notifications.INotification import INotification
from notification_consumer.utils.response import Response


class SMSNotification(INotification):

    def send_group_notification(self, body):
        response = Response()
        response.add_data("is_sent", True)
        return response

    def send_single_notification(self, body):
        response = Response()
        response.add_data("is_sent", True)
        return response
