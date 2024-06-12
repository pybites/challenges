import time

from pika import BlockingConnection, URLParameters


class amqp:
    def __init__(self, amqp_url):
        self.amqp_url = amqp_url
        self.connection = None
        self.channel = None

    def __enter__(self):
        self.connection = BlockingConnection(URLParameters(self.amqp_url))
        self.channel = self.connection.channel()
        return self.connection, self.channel

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.channel.close()
        self.connection.close()


# Publish messages to the RabbitMQ queue
with amqp("amqp://zcrmi:crm_zia@172.20.36.0:5672/model_training_test") as (connection, channel):
    for i in range(10):
        channel.basic_publish(exchange='',
                              routing_key='queue_name',
                              body=f'My message {i}')


def on_message(channel, method_frame, header_frame, body):
    print(f'Got the message {body.decode()}')
    time.sleep(10)  # Imitating processing time


# Consume messages from the RabbitMQ queue
with amqp("amqp://zcrmi:crm_zia@172.20.36.0:5672/model_training_test") as (connection, channel):
    channel.basic_qos(1)
    channel.basic_consume(on_message_callback=on_message, queue='queue_name', auto_ack=True)
    channel.start_consuming()
