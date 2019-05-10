from __future__ import print_function
import json
import boto3


def lambda_handler(event, context):
    # Process message from the Lex Service:
    print("Processing message from Twilio")

    message = {
        'type': "twilio_inbound",
        'from': event["From"],
        'body': event["Body"],
    }

    # Scrape:
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:245636212397:lexMessage',
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
    print(response)
    print("Important info: ", message)
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>' \
           '<Response><Message>Hello from DeepShack! We are calculating \
            your time-to-burger. Hang tight...</Message></Response>'
