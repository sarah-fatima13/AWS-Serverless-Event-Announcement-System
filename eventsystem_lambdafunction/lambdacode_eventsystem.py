import json
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
sns = boto3.client('sns')

bucket_name = 'event-announcement-website-superfast'
events_file_key = 'events.json'
sns_topic_arn = 'arn:aws:sns:ap-south-1:215925484254:EventAnnouncementsfnew'

def lambda_handler(event, context):
    try:
        new_event = json.loads(event['body'])

        try:
            response = s3.get_object(Bucket=bucket_name, Key=events_file_key)
            events_data = json.loads(response['Body'].read().decode('utf-8'))
        except ClientError:
            events_data = []

        events_data.append(new_event)

        s3.put_object(
            Bucket=bucket_name,
            Key=events_file_key,
            Body=json.dumps(events_data, indent=2),
            ContentType='application/json'
        )

        message = f"New Event: {new_event['title']} on {new_event['date']}\n{new_event['description']}"

        sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject="New Event Announcement"
        )

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS, POST",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            'body': json.dumps({'message': 'Event created successfully!'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({'message': str(e)})
        }