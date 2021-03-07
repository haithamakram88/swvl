import requests
from notification_consumer import config
from datetime import datetime
from notification_consumer.utils.constans import StatusCodes

def send_message_to_queue(message):
    try:
        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")
        message.update(time_of_return=current_time)
        response = requests.post(config.PRODUCER_URL, json=message)
        if response.status_code != StatusCodes.OK.value:
            print("could not send this message: {} ,to broker with error: {}".format(message, response.text))
        return response
    except Exception as e:
        print("could not send this message: {} ,to broker with error: {}".format(message, e))
