import pika , json , os , psycopg2 , time

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq', 5672 , '/' , credentials , heartbeat=60)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_declare(queue='hello1' , exclusive=True)
channel.queue_bind(exchange='logs', queue="hello1")

def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    print(data)
    

    con = psycopg2.connect(host='db', port="5432" , user="postgres" ,password ="dariush", database="postgres")
    cursor = con.cursor()

    INSERT_QUERY = """
    INSERT INTO "C_O_API_App_indexes" 
        ("symbolisin", "variation", "top", "bottom" , "opening_price") VALUES (%s,%s,%s,%s,%s);"""
    
    cursor.execute(INSERT_QUERY, (f'{data["symbolisin"]}',f'{data["variation"]}',f'{data["top"]}',f'{data["bottom"]}',f'{data["opening_price"]}'))
    con.commit()
    cursor.close()
    con.close()
    

channel.basic_consume(queue='hello1', on_message_callback=callback, auto_ack=True) 
print(' [*] start consuming in consumer service. To exit press CTRL+C')
channel.start_consuming()

