import pika
import uuid


class MQService:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )

    async def send_message(self, message):
        channel = self.connection.channel()
        channel.exchange_declare(exchange="scrap", exchange_type="fanout")

        correlation_id = str(uuid.uuid4())
        result = channel.queue_declare(queue="", exclusive=True)
        queue_name = result.method.queue
        channel.basic_publish(
            exchange="scrap",
            routing_key="",
            body=message,
            properties=pika.BasicProperties(
                reply_to=queue_name, correlation_id=correlation_id
            ),
        )

        # TODO: 작업 결과 대기 로직 구성
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True
        )

        channel.start_consuming()
