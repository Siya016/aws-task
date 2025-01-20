import json
import boto3
import base64
import os


def lambda_handler(event, context):

    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'your-s3-bucket-name')

    try:
        # Parse the incoming request
        body = json.loads(event['body'])
        file_data = body['file_data']
        file_name = body['file_name']


        decoded_file = base64.b64decode(file_data)

        # Upload the file to S3
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=file_name,
            Body=decoded_file,
            ContentType='application/pdf'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully',
                'file_url': f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error uploading file',
                'error': str(e)
            })
        }
