from app.databases.mongodb import MongodbClient
from app.repositories.groups import GroupsRepository
from app.repositories.users import UsersRepository
from app.utils.response import Response


def create_group(data):
    response = Response()
    try:
        db_client = MongodbClient()
        group_repository = GroupsRepository(db_client)
        user_repository = UsersRepository(db_client)

        is_valid = validate_users_ids(user_repository, data)

        if is_valid:
            created_group = group_repository.insert(data)
            response.add_data("message", "New group created successfully")
            response.add_data("group_id", str(created_group))

        else:
            response.status = False
            response.add_data("message", "Couldn't create new group because not valid users ids")

    except Exception as e:
        print(e)
        response.status = False
        response.add_data("message", "Couldn't create new group with error: {}".format(e))

    return response


def validate_users_ids(user_repository, data):
    ids = data.get("users_ids")
    valid_ids = user_repository.check_ids(ids)
    if len(valid_ids) == len(ids):
        return True
    else:
        return False
