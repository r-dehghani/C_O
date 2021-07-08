import pika 
params = pika.URLParameters("amqps://qovczade:SltebwIvG3a5zJDbkYxKP7yHQQc8aPCf@fly.rmq.cloudamqp.com/qovczade")
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received ")
    print(body)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True) 


print(' [*] start consuming. To exit press CTRL+C')
channel.start_consuming()
