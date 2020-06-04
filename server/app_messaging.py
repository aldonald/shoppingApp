import datetime
import pusher
from pusher_push_notifications import PushNotifications
import logging

beams_client = PushNotifications(
    instance_id='8d9473dd-0a61-4ac4-88de-d5dc18ad095a',
    secret_key='DFF47EC3886A6D1C2947F6A1C3ADD2D91D1256DF73E52A408D247A7A8E8BCA11',
)

def send_notification(users, items_added):
    logging.warning("Sending notifiaction to Pusher.")
    logging.warning(f"Users in request: {users}. Items added are: {items_added}.")
    response = beams_client.publish_to_users(
        user_ids=users,
        publish_body={
            'apns': {
                'aps': {
                    'alert': 'Shopping list',
                },
            },
            'fcm': {
                'notification': {
                    'title': 'Shopping List',
                    'body': f'{items_added} has been added to your shopping list!',
                },
            },
            'web': {
                'notification': {
                    'title': 'Shopping List',
                    'body': f'{items_added} has been added to your shopping list!',
                },
            },
        },
    )
    print(response['publishId'])
