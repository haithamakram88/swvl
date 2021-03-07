from enum import Enum


class StatusCodes(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400


class CollectionsNames(Enum):
    NOTIFICATIONS = "notifications"
    USERS = "users"
    GROUPS = "groups"


class MessageTypes(Enum):
    SINGLE = "single"
    GROUP = "group"
