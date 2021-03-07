import pika
from notification_consumer import config
from notification_consumer.api.notifications import process


class RabbitMQConsumer:
    def __init__(self):
        try:
            self.credentials = pika.PlainCredentials(username=config.MESSAGE_QUEUE_USERNAME,
                                                     password=config.MESSAGE_QUEUE_PASSWORD)
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.MESSAGE_QUEUE_HOST,
                                                                                credentials=self.credentials))
            self.channel = self.connection.channel()

            print("finish init consumer")
        except Exception as e:
            print("consumer init error {}".format(e))

    def start_consumer(self):
        try:
            # self.channel.queue_declare(queue="notification", arguments={'x-message-ttl': 300000}, durable=True)
            self.channel.queue_declare(queue=config.MESSAGE_QUEUE_NAME, durable=True)
            self.channel.basic_qos(prefetch_count=1)
            self.channel.basic_consume(config.MESSAGE_QUEUE_NAME, process, auto_ack=False)
            self.channel.start_consuming()

        except Exception as e:
            print(e)

    def close_connection(self):
        self.connection.close()
