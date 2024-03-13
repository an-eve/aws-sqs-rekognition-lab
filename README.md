# Exploring AWS

# Exploring AWS

## Amazon Rekognition:
1. **Connecting to Rekognition:** To connect to Amazon Rekognition, users need to use the `boto3` library in Python. This library provides an interface to interact with various AWS services, including Rekognition. Initialize a Rekognition client using `boto3.client('rekognition')`.

2. **Using Rekognition:** Once the Rekognition client is initialized, users can call specific functionalities provided by the Rekognition service. For example, in the provided code snippet, the `detect_labels_local_file()` function is used to detect labels in an image file. Pass the image data to the Rekognition service using the `detect_labels()` method.

To run the code use the command:

```bash
python aws_rekognition.py 
```

The result is  a list of lable and the corresponding confidence:

![Uploading](images/labels.png)

## Amazon SQS:
1. **Connecting to SQS:** Similar to Rekognition, users connect to Amazon SQS using the `boto3` library in Python. Initialize an SQS client using `boto3.client('sqs')`.

2. **Using SQS:** After initializing the SQS client, users can interact with SQS queues by calling methods provided by the SQS service. In the provided code snippet, functionalities such as creating a queue (`create`), listing existing queues (`list`), sending messages to a queue (`send`), receiving and deleting messages from a queue (`receive`), and deleting a queue (`delete`) are demonstrated. Provide the necessary parameters such as queue URL and message content to these methods to perform respective actions on SQS queues.

The available functionalities are:

1. **create**: Create a new empty queue


```bash
python aws_sqs.py create queue_1
``` 
The response is: 

```
Queue 'queue_1' created. URL: https://sqs.us-east-1.amazonaws.com/654654507474/queue_1
```

We could see the queue also from the AWS Console:

![Uploading](images/create_queue.png)



2. **list**: List all existing queues

```bash
python aws_sqs.py list
```

The result is:

```
SQS Queues:
https://sqs.us-east-1.amazonaws.com/654654507474/queue_1
```

3. **send**: Send a message to a specific queue

```bash
python aws_sqs.py send 'https://sqs.us-east-1.amazonaws.com/654654507474/queue_1' "New message"
```

The result is:

```
Message sent. Message ID: d6af810b-34c3-4994-9f34-6216094c2b9b
```

The new message is accessable from the AWS Console:

![Uploading](images/message.png)


4. **receive**: Receive the oldest message from a specific queue and delete it

```bash
python aws_sqs.py receive 'https://sqs.us-east-1.am
azonaws.com/654654507474/queue_1' 
```

The result is:

```
Received message: New message
Message deleted from the queue.
```
5. **delete**: Delete the queue

```bash
python aws_sqs.py delete queue_1
```

The result is:

```
Queue deleted: https://sqs.us-east-1.amazonaws.com/654654507474/queue_1
```
