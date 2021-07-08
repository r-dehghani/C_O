import pika , json
# from C_O_API_App.models import 
params = pika.URLParameters("amqps://qovczade:SltebwIvG3a5zJDbkYxKP7yHQQc8aPCf@fly.rmq.cloudamqp.com/qovczade")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    print(data)
    

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True) 


print(' [*] start consuming. To exit press CTRL+C')
channel.start_consuming()
