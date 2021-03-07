from fastapi import APIRouter, Response
from app.apis.users import create_user
from app.models.user import User
from app.parser.parser import parse_user_request
import json
from app.utils.constans import StatusCodes

router = APIRouter()


@router.post("/user")
def create(body: User):
    data = parse_user_request(body)
    response = create_user(data)
    if response.status:
        return Response(content=json.dumps(response.data), status_code=StatusCodes.CREATED.value)
    else:
        return Response(content=json.dumps(response.data), status_code=StatusCodes.BAD_REQUEST.value)
