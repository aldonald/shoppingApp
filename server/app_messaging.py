from firebase_admin import messaging
from accounts.models import AccountToken
import datetime

def send_notification(registration_token, item_added):
    message = messaging.MulticastMessage(
        data={'item': item_added, 'time': str(datetime.datetime.now())},
        tokens=registration_token,
    )

    response = messaging.send_multicast(message)
    print('{0} messages were sent successfully'.format(response.success_count))


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
