"""This File will create connection and consume messages"""
import pika
from schemas import schema

class RabbitMQConsumer:
    """This class will consume messages from RabbitMQ"""
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.exchange_name = 'subscription_updates'
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='#')
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
    
    def callback(self, ch, method, properties, body):
        print("Received message:", body)

    def start_consuming(self):
        self.channel.start_consuming()
