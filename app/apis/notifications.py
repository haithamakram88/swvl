from app.factories.repository_factory import RepositoryFactory
from app.message_broker.rabbitmq import RabbitMQProducer
from app.utils.response import Response


def send_notification(data):
    response = Response()
    try:
        producer = RabbitMQProducer()
        repository_factory = RepositoryFactory()

        repository = repository_factory.get_repository(data.get("message_type"))

        if repository:
            is_valid = validate_ids(repository, data)

            if is_valid:
                response = producer.send_message(data)
            else:
                response.status = False
                response.add_data("message", "Couldn't send new notification because not valid ids")

    except Exception as e:
        print(e)
        response.status = False
        response.add_data("message", "Couldn't send new notification with error: {}".format(e))

    return response


def validate_ids(repository, data):
    ids = data.get("ids")
    valid_ids = repository.check_ids(ids)
    if len(valid_ids) == len(ids) and len(ids) > 0:
        return True
    else:
        return False
