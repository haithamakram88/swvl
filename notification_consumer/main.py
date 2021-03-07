from fastapi import FastAPI
from notification_consumer.message_broker.rabbitmq import RabbitMQConsumer

app = FastAPI()

if __name__ == "__main__":
    consumer = RabbitMQConsumer()
    consumer.start_consumer()
