import json
import boto3
import os

def send_email(event, context):
    try:
        body=json.loads(event['body'])
        receiver=body.get('receiver')
        subject=body.get('subject')
        body_text=body.get('body')

        if not receiver or not subject or not body_text:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required fields: receiver, subject, body'})
            }
        ses=boto3.client('ses', region_name=os.environ['AWS_REGION'])
        response=ses.send_email(
            Source=os.environ['SENDER_EMAIL'],
            Destination={'ToAddresses': [receiver]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully', 'response': response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error sending email', 'error': str(e)})
        }
