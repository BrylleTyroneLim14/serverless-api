
import sys
sys.path.append("../")
from os import environ as env
from twilio.rest import Client


def index(event,context):

    mobile_num = event['body']['mobile_num']
    message = event['body']['message']
    
    client = Client(env['account_sid'], env['auth_token'])

    message = client.messages \
                    .create(
                        body=message,
                        from_='+12015966684',
                        to=mobile_num
                    )
    response = {
        "statusCode": 200,
        "body": "Message Sent!"
    }

    return response
