import pika , json
params = pika.URLParameters("amqps://qovczade:SltebwIvG3a5zJDbkYxKP7yHQQc8aPCf@fly.rmq.cloudamqp.com/qovczade")
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method , body):
    properties = pika.BasicProperties(method)
    # use publish to estabilish body. exchange is just saying that which queue has this routing key. i wanna send this body to it
    channel.basic_publish(exchange='', routing_key='hello' , body = json.dumps(body) , properties= properties)  ##1
    print("published message ^_^")
    