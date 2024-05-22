import os
from MessageBrokers import RabbitMQ

# Get the environment variables
queue_name = os.getenv('RABBITMQ_QUEUE_NAME')
target_queue_name = os.getenv('RABBITMQ_TARGET_QUEUE_NAME')
exchange = os.getenv('RABBITMQ_EXCHANGE')
host = os.getenv('RABBITMQ_HOST')
username = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')

# Initialize a connection to RabbitMQ message broker
rabbitmq = RabbitMQ(queue_name=queue_name, target_queue_name=target_queue_name, exchange=exchange, host=host, username=username, password=password)

# Receive messages from the queue
messages = rabbitmq.ReceiveMessages()

for message in messages:
    # Process the received message
    print(f"Received message: {message}")

# Send a message to the queue
rabbitmq.SendMessage("Hello, RabbitMQ!")

# Close the connection
rabbitmq.Close()