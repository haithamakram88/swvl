import json


def parse_notification_request(body):
    data = {
        "notification_type": body.notification_type,
        "message": body.message,
        "message_type": body.message_type,
        "ids": body.ids,
        "time_of_return": body.time_of_return
    }
    return data


def parse_group_request(body):
    data = {
        "name": body.name,
        "users_ids": body.users_ids
    }
    return data


def parse_user_request(body):
    data = {
        "name": body.name
    }
    return data
