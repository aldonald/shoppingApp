from firebase_admin import messaging
from fcm_django.models import FCMDevice
from accounts.models import AccountToken
import datetime
import pusher
from pusher_push_notifications import PushNotifications

beams_client = PushNotifications(
    instance_id='8d9473dd-0a61-4ac4-88de-d5dc18ad095a',
    secret_key='DFF47EC3886A6D1C2947F6A1C3ADD2D91D1256DF73E52A408D247A7A8E8BCA11',
)

def send_notification(users, items_added):
    response = beams_client.publish_to_users(
        user_ids=users,
        publish_body={
            'apns': {
                'aps': {
                    'alert': 'Hello!',
                },
            },
            'fcm': {
                'notification': {
                    'title': 'Hello',
                    'body': 'Hello, world!',
                },
            },
            'web': {
                'notification': {
                    'title': 'Hello',
                    'body': 'Hello, world!',
                },
            },
        },
    )
    print(response['publishId'])

    # tok = "cPowB_QiSKShfWI6WYRGV1:APA91bF4Jlj5NtQLuP0DHx08HjbsJJ1ZYTQZo1z5CsR7TKwxoYVJJRy0RatVhuGaNM-xCDLKJbsY43-TujKYHsV5Z65c3eOG0sF5fZq_fzY9plr4Dg1hFM2hk0geecw5u4IX_MFYGVlA"

    # import pdb
    # pdb.set_trace()

    # pusher_client = pusher.Pusher(
    #     app_id='1011339',
    #     key='e1cde031e4a88ff3bede',
    #     secret='e73248583ee4a0dd7cc8',
    #     cluster='ap1',
    #     ssl=True
    # )

    # pusher_client.trigger('my-channel', tok, {'message': 'hello world'})
        
    
    # registration_tokens.append(tok)
    # device_list = FCMDevice.objects.filter(registration_id__in=registration_tokens)
    # for device in device_list:
    #     device.send_message(title="New Item Added", body=f"{items_added} was added to your shopping list.", data={
    #                     'item': items_added, 'time': str(datetime.datetime.now())})
    
    # firebase_admin.get_app()
    # message = messaging.MulticastMessage(
    #     data={'item': items_added, 'time': str(datetime.datetime.now())},
    #     tokens=registration_tokens,
    # )

    # response = messaging.send_multicast(message)
    # print('{0} messages were sent successfully'.format(response.success_count))


def send_dry_run():
    token = AccountToken.objects.get(user_id=1)
    
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=token,
    )

    response = messaging.send(message, dry_run=True)

    print('Dry run successful:', response)
