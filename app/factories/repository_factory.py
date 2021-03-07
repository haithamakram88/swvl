from app.repositories.groups import GroupsRepository
from app.repositories.users import UsersRepository
from app.databases.mongodb import MongodbClient
from app.utils.constans import MessageTypes


class RepositoryFactory:
    def get_repository(self, message_type):
        db_client = MongodbClient()

        if message_type == MessageTypes.SINGLE.value:
            return UsersRepository(db_client)

        elif message_type == MessageTypes.GROUP.value:
            return GroupsRepository(db_client)
        else:
            return None
