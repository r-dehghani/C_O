import pika , json  
import smtplib

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq', 5672 , '/' , credentials , heartbeat=60)
print("this is one")
connection = pika.BlockingConnection(parameters)
print("this is two")
channel = connection.channel()

channel.exchange_declare(exchange='another_exchange', exchange_type='fanout')
channel.queue_declare(queue='email' , exclusive=False)
channel.queue_bind(exchange='another_exchange', queue="email")


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    email_service(data)
    

    
    
def email_service(data):

        sender_email = "r.dehghani.68@gmail.com"
        receiver_email = "r.dehghani.90@gmail.com"
        password = "Password-68_"
        server = smtplib.SMTP('smtp.gmail.com' , 587 )
        server.starttls()
        server.login(sender_email , password)
        print("login to email service success")
        
        message = f"""Hey there!
        your desired stock : {data[1]}
        at the desired condition with price :{data[3]}
        is ready!!!"""
        server.sendmail(sender_email , receiver_email , message)
        print("email has been sent to the receiver email !!")


channel.basic_consume(queue='email', on_message_callback=callback, auto_ack=True) 
print(' [*] start consuming in email service. To exit press CTRL+C')
channel.start_consuming()





