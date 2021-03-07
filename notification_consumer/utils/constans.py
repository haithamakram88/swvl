from enum import Enum

class StatusCodes(Enum):
    OK = 200


class NotificationsTypes(Enum):
    SMS = "sms_notification"
    PUSH = "push_notification"


class CollectionsNames(Enum):
    NOTIFICATIONS = "notifications"
    USERS = "users"
    GROUPS = "groups"


class MessageTypes(Enum):
    SINGLE = "single"
    GROUP = "group"
