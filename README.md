## Overview
    The perpose of this application is handle sending two types of notifications:
    (push notifications and sms messages) for specific users or groups with limited
    number of requests per minute according to the support of the provider.
 
### Technologies:
- FastAPI Framework (python)
- Mongodb Database
- RabbitMQ 
- Docker

### Requirements
  - **Docker** 
    - if you don't know how to install Docker please go to **(https://docs.docker.com/engine/install/ubuntu/)**
  - **Docker Compose**
    - if you don't know how to install Docker Compose please go to **(https://docs.docker.com/compose/install/)**

### Installation

* Fork the repository and clone it
* clone the repository by running `git clone <repository-url>`
* changing the directory `cd swvl`
* You must copy this file `app/.example.env` and paste it with new name `app/.env`
* You must copy this file `notification_consumer/.example.env` and paste it with new name `notification_consumer/.env`
* run docker-compose `sudo docker-compose up -d --build`


**Note: Please run sudo docker-compose ps and make sure that 4 services running well**

## Documentation

 - There are three apis:
    - One for create user, and it's return response that contains user_id.
    - One for create group with users that assigned to it, 
      and it's return response that contains group_id.
    - finally one for send notification either push notification or 
      sms message depending on type of notification and for groups 
      or users depending on type of message
 
### Working flow
    
* Create new user by running this request:
```curl
curl --location --request POST '0.0.0.0:3000/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Haitham"
}'
```
* Create new group with user ids by running this request:
```curl
curl --location --request POST '0.0.0.0:3000/group' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Group1",
    "users_ids": ["USER ID THAT RETURNED FROM THE ABOVE REQUEST"]
}'
```
* Send notification by running this request:
```curl
curl --location --request POST '0.0.0.0:3000/notification/send' \
--header 'Content-Type: application/json' \
--data-raw '{
    "notification_type": "sms_notification" OR "push_notification,
    "message": "First Notification",
    "message_type": "group" OR "single",
    "ids": ["USER ID OR GROUP ID ACCORDING TO MESSAGE TYPE"]
}'
```
## Architecture

* When send notification api called, the notification app validate the request ids
  according to message_type key.

* If it's valid then send the notification to the queue 

* Then notification consumer starts to consume the message and send it to the provider
  according to notification_type key.

* If it sent successfully the notification saved in database and removed from queue.

* If the provider response was that we arrived to limited requests per minute,
  the notification consumer send the message again to the queue with added key 
  `time_of_return` to check on it at the second time the message
  will be return back to the consumer, If the difference time between `now` and 
  the `time_of_return` key less than one minute then the consumer will wait for one
  minute before trying to call the provider again.
  