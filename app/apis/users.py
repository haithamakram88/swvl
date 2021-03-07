from app.databases.mongodb import MongodbClient
from app.repositories.users import UsersRepository
from app.utils.response import Response


def create_user(data):
    response = Response()
    try:
        db_client = MongodbClient()
        user_repository = UsersRepository(db_client)
        created_user = user_repository.insert(data)
        response.add_data("message", "New user created successfully")
        response.add_data("user_id", str(created_user))

    except Exception as e:
        print(e)
        response.status = False
        response.add_data("message", "Couldn't create new user with error: {}".format(e))

    return response

