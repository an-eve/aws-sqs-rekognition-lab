import boto3
import sys

def list_queues():
    # Create SQS client
    sqs = boto3.client('sqs')
    # List SQS queues
    response = sqs.list_queues()
    print(response)
    print("SQS Queues:")
    for url in response.get('QueueUrls', []):
        print(url)

def create_queue(queue_name):
    sqs = boto3.client('sqs')
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes={
            'DelaySeconds': '60',
            'MessageRetentionPeriod': '86400'
        }
    )
    print(f"Queue '{queue_name}' created. URL: {response['QueueUrl']}")

def send_message(queue_url, message_body):
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    print(f"Message sent. Message ID: {response['MessageId']}")

def receive_message(queue_url):
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    
    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        body = message['Body']
        print(f"Received message: {body}")
        
        # Delete the received message from the queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print(f"Message deleted from the queue.")
    else:
        print("No messages in the queue.")

def delete_queue(queue_name: str):
    sqs = boto3.client('sqs')
    # Get URL for SQS queue
    response = sqs.get_queue_url(QueueName=queue_name)
    queue_url = response['QueueUrl']
    # Delete SQS queue
    sqs.delete_queue(QueueUrl=queue_url)
    print(f"Queue deleted: {queue_url}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python aws_sqs.py <action> [args]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "list":
        list_queues()

    elif action == "create":
        if len(sys.argv) != 3:
            print("Usage: python sqs_program.py create <queue_name>")
            sys.exit(1)
        create_queue(sys.argv[2])

    elif action == "send":
        if len(sys.argv) != 4:
            print("Usage: python sqs_program.py send <queue_url> <message_body>")
            sys.exit(1)
        send_message(sys.argv[2], sys.argv[3])

    elif action == "receive":
        if len(sys.argv) != 3:
            print("Usage: python sqs_program.py receive <queue_url>")
            sys.exit(1)
        receive_message(sys.argv[2])

    elif action == "delete":
        if len(sys.argv) != 3:
            print("Usage: python sqs_program.py delete <queue_url>")
            sys.exit(1)
        delete_queue(sys.argv[2])

    else:
        print(f"Unknown action: {action}")
        sys.exit(1)
