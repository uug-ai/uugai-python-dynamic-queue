# MessageBrokers

MessageBrokers is a Python library that provides a simple and efficient way to work with message brokers. It abstracts away the complexities of interacting with different message broker systems, allowing you to focus on writing your application logic.

## Installation
To install MessageBrokers, you can use pip:
`pip install python_queue_reader`

importing in python via:
`from python_queue_reader import MessageBrokers`

## Example usage
The code snippet provided demonstrates the usage of the MessageBrokers library in Python. It showcases how to initialize a connection to a message broker system, receive messages from a queue, send a message to the queue, and close the connection. The library abstracts away the complexities of interacting with different message broker systems, allowing developers to focus on writing their application logic. Let's dive into the details of each feature and method.

```
from python_queue_reader import MessageBrokers

# Initialize a connection to RabbitMQ message broker
rabbitmq = MessageBrokers.RabbitMQ(queue_name='my_queue', target_queue_name = 'my_target_queue', exchange='my_exchange', host='host', username='guest', password='guest')

# Receive messages from the queue
messages = rabbitmq.ReceiveMessages()

for message in messages:
    # Process the received message
    print(f"Received message: {message}")

# Send a message to the queue
rabbitmq.SendMessage("Hello, RabbitMQ!")

# Close the connection
rabbitmq.Close()
```

## Features
Supports popular message broker systems such as **RabbitMQ**, **SQS**, and **Kafka**. Abstracted to following methods:

### Initialization
The initialization methods in the MessageBrokers library allow you to create instances of different message broker systems. Here are the available initialization methods:

- `RabbitMQ(queue_name: str, exchange: str, host: str, username: str, password: str)`:
 Initializes a connection to a RabbitMQ message broker. You need to provide the queue name, exchange, host, username, and password.

- `SQS(queue_name: str, aws_access_key_id: str, aws_secret_access_key: str)`:
 Initializes a connection to an Amazon Simple Queue Service (SQS) message broker. You need to provide the queue name, AWS access key ID, and AWS secret access key.

- `Kafka(queue_name: str, broker: str, group_id: str, mechanism: str, security: str, username: str, password: str)`: Initializes a connection to a Kafka message broker. You need to provide the queue name, broker address, group ID, authentication mechanism, security protocol, username, and password.

### ReceiveMessages
The `ReceiveMessages()` method is a part of the MessageBrokers library in Python. It is used to receive messages from the message broker system that you have initialized.

Once you have established a connection to a specific message broker system using one of the initialization methods (`RabbitMQ()`, `SQS()`, or `Kafka()`), you can call the `ReceiveMessages()` method to start receiving messages from the specified queue.

This method allows you to retrieve messages from the message broker and process them in your application logic. It provides a simple and efficient way to consume messages from the message broker system without having to handle the complexities of interacting with different message broker systems directly.


### SendMessage
The `SendMessage(message: str)` method is a part of the MessageBrokers library in Python. It is used to send a message to the message broker system that you have initialized.

Once you have established a connection to a specific message broker system using one of the initialization methods (`RabbitMQ()`, `SQS()`, or `Kafka()`), you can call the `SendMessage` method to send a message to the specified queue.

This method takes a single parameter message, which is a string representing the content of the message you want to send. You can use this method to publish messages to the message broker system, allowing other applications or services to consume and process them.

### Close
The `Close()` method is a part of the MessageBrokers library in Python. It is used to close the connection to the message broker system that you have initialized.

After you have finished using the message broker system and no longer need to receive or send messages, you can call the `Close()` method to gracefully close the connection. This ensures that any resources used by the message broker system are properly released.

