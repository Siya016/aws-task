import json
import base64


# Simulate the AWS Lambda function
def lambda_handler(event, context):
    import boto3
    import os

    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'test-bucket')

    try:

        body = json.loads(event['body'])
        file_data = body['file_data']
        file_name = body['file_name']


        decoded_file = base64.b64decode(file_data)

        # Simulate S3 upload (write locally instead of S3)
        local_test_folder = 'local_s3'
        os.makedirs(local_test_folder, exist_ok=True)
        file_path = os.path.join(local_test_folder, file_name)

        with open(file_path, 'wb') as f:
            f.write(decoded_file)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully',
                'file_path': file_path  # Local file path
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


# Local test script
if __name__ == "__main__":

    sample_file_content = b"%PDF-1.4\n%Test PDF content"
    encoded_file_data = base64.b64encode(sample_file_content).decode('utf-8')

    # Simulate an API Gateway event
    test_event = {
        "body": json.dumps({
            "file_name": "test.pdf",
            "file_data": encoded_file_data
        })
    }


    test_context = {}

    # Run the function locally
    response = lambda_handler(test_event, test_context)

    # Print the response
    print("Response:")
    print(json.dumps(json.loads(response['body']), indent=2))
