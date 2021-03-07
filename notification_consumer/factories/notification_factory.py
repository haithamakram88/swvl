from notification_consumer.notifications.push_notification import PushNotification
from notification_consumer.notifications.sms_notification import SMSNotification
from notification_consumer.utils.constans import NotificationsTypes


class NotificationFactory:

    def get_notification_type(self, notification_type):

        if notification_type == NotificationsTypes.SMS.value:
            return SMSNotification()

        elif notification_type == NotificationsTypes.PUSH.value:
            return PushNotification()

        else:
            return None
