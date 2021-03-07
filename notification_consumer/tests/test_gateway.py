import pytest
from notification_consumer.gateways.notification_gateway import send_message_to_queue
from notification_consumer.utils.constans import StatusCodes


def test_send_message_to_queue():
    data = {
        "notification_type": "sms_notification",
        "message": "test",
        "message_type": "single",
        "ids": ["60422e21d5c54a75349e6943"],
        "time_of_return": "27/2/2021 10:30:20"
    }
    response = send_message_to_queue(data)
    assert response.status_code == StatusCodes.OK.value
