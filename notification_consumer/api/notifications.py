import json
import time
from datetime import datetime

from notification_consumer.factories.notification_factory import NotificationFactory
from notification_consumer.gateways.notification_gateway import send_message_to_queue
from notification_consumer.services.notification_service import NotificationService


def process(ch, method, props, data):
    try:
        data = json.loads(data)
        message_type = data.get("message_type")
        time_of_return = data.get("time_of_return", None)

        if time_of_return:
            check_returned_message(data)

        notification_factory = NotificationFactory()

        notification_type = notification_factory.get_notification_type(data.get("notification_type"))
        if notification_type:
            notification_service = NotificationService(notification_type, message_type)

            response = notification_service.send_notification(data)

            handle_send_notification_response(ch, method, response, data)

    except Exception as e:
        print(e)


def handle_send_notification_response(ch, method, response, data):
    is_sent = response.data.get("is_sent", None)
    if not is_sent:
        send_message_to_queue(data)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def check_returned_message(message):
    now = datetime.now()
    returned_time = datetime.strptime(message.get("time_of_return"), "%d/%m/%Y %H:%M:%S")
    minutes_diff = (now - returned_time).total_seconds() / 60.0
    if minutes_diff < 1:
        time.sleep(60)
