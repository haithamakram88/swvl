import json
import pika

from app import config
from app.utils.response import Response


class RabbitMQProducer:
    def __init__(self):
        try:
            self.credentials = pika.PlainCredentials(config.MESSAGE_QUEUE_USERNAME, config.MESSAGE_QUEUE_PASSWORD)
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.MESSAGE_QUEUE_HOST,
                                                                                credentials=self.credentials))
            self.channel = self.connection.channel()
            print("finish init producer")
        except Exception as e:
            print("producer init error {}".format(e))

    def send_message(self, message):
        message = json.dumps(message)
        response = Response()
        try:
            # self.channel.queue_declare(queue="notification", arguments={'x-message-ttl': 300000}, durable=True)
            self.channel.queue_declare(queue=config.MESSAGE_QUEUE_NAME, durable=True)
            self.channel.basic_publish(
                exchange="",
                routing_key=config.MESSAGE_QUEUE_NAME,
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,
                )
            )
            self.connection.close()
            response.add_data("message", "notification sent to queue successfully")

        except Exception as e:
            print(e)
            response.status = False
            response.add_data("message", "Couldn't send notification to queue with error: {}".format(e))

        return response
