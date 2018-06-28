import boto3
import json
import urllib
import os

#Create as python 2.7 runtime

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=1))
    client = boto3.client('sns')

    phonenum = os.environ['Phone']
    print(phonenum)

    Image = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

    response = client.publish(

        PhoneNumber = phonenum,
        Message = 'A new file was uploaded: ' + Image

    )

    return response
