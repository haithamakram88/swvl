import json
from fastapi import APIRouter, Response
from app.apis.groups import create_group
from app.models.group import Group
from app.parser.parser import parse_group_request
from app.utils.constans import StatusCodes

router = APIRouter()


@router.post("/group")
def create(body: Group):
    data = parse_group_request(body)
    response = create_group(data)
    if response.status:
        return Response(content=json.dumps(response.data), status_code=StatusCodes.CREATED.value)
    else:
        return Response(content=json.dumps(response.data), status_code=StatusCodes.BAD_REQUEST.value)
