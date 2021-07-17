import pika , json
import time
import random
import time

symbol = ["khafula", "fameli", "shepeli", "zoub"]
variation = ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]
top =           ["1000" , "1200" , "1300" , "1400" , "1500" , "1600" , "1700" , "1800" , "1900" , "2000", "2100"]
bottom =        ["900" , "1100" , "1200" , "1300" , "1400" , "1500" , "1600" , "1700" , "1800" , "1900" , "2000"]
opening_price = ["950" , "1000" , "1100" , "1200" , "1300" , "1400" , "1500" , "1600" , "1700" , "1800" , "1900"]


credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq', 5672 , '/' , credentials , heartbeat=60)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')


def publish(method , body):
    properties = pika.BasicProperties(method)
    # use publish to estabilish body. exchange is just saying that which queue has this routing key. i wanna send this body to it
    channel.basic_publish(exchange='logs', routing_key='' , body = json.dumps(body) , properties= properties)  
    print("published message ^_^")
    

while True:
    rand_num = random.randint(0, len(top)-1)
    x = {'symbolisin': symbol[random.randint(0 ,len(symbol)-1)], 'variation': variation[rand_num], 'top': top[rand_num], 'bottom': bottom[rand_num], 'opening_price': opening_price[rand_num]} 
    print(f"the data is : {x}")
    time.sleep(5.0)
    publish("adding_live_data", x)


