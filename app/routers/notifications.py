from fastapi import APIRouter, Response
from app.apis.notifications import send_notification
from app.parser.parser import parse_notification_request
from app.models.notification import Notification
import json
from app.utils.constans import StatusCodes

router = APIRouter()


@router.post("/notification/send")
def send(body: Notification):
    message = parse_notification_request(body)
    response = send_notification(message)
    if response.status:
        return Response(content=json.dumps(response.data), status_code=StatusCodes.OK.value)
    else:
        return Response(content=json.dumps(response.data), status_code=StatusCodes.BAD_REQUEST.value)
