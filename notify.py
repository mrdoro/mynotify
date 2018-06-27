import boto3
import json
import urllib

#Create as python 2.7 runtime

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=1))
    client = boto3.client('sns')

    Image = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

    response = client.publish(
        #Provide correct phone number
        PhoneNumber = '+48111222333',
        Message = 'A new file was uploaded: ' + Image

    )

    return response
