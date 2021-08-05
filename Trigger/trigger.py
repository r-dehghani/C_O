import psycopg2 , pika , json
import smtplib 
# from . import sending_email
from enum import Enum # this is for enumeration
# from sys import argv
# scrips , symbolisin , order_price , operator = argv
class operator(Enum):
    equal = 0
    greater_or_equal = 1
    less_or_equal = 2
    greater = 3
    less = 4
# ======================================================================
'''
sender_email = "r.dehghani.68@gmail.com"
receiver_email = "r.dehghani.90@gmail.com"
password = "Password-68_"


server = smtplib.SMTP('smtp.gmail.com' , 587 )
server.starttls()
server.login(sender_email , password)
print("login to email service success")
'''

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq', 5672 , '/' , credentials , heartbeat=60)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_declare(queue='hello2' , exclusive=False)
channel.queue_bind(exchange='logs', queue="hello2")
# =========================================================



channel_email = connection.channel()
channel_email.exchange_declare(exchange='another_exchange', exchange_type='fanout')
def publish(method , body):
    properties = pika.BasicProperties(method)
    # use publish to estabilish body. exchange is just saying that which queue has this routing key. i wanna send this body to it
    channel.basic_publish(exchange='another_exchange', routing_key='' , body = json.dumps(body) , properties= properties)  
    print("published message ^_^")


def read_triggers():
    con = psycopg2.connect(host='db', port="5432" , user="postgres" ,password ="dariush", database="postgres")
    cursor = con.cursor()

    SELECT_QUERY = """ SELECT * FROM "C_O_API_App_trigger" ORDER BY id DESC ; """
    cursor.execute(SELECT_QUERY)
    rows = cursor.fetchall() #[(...),(...)] return a list of tuples
    
    con.commit()    
    cursor.close()
    print(f"this is all available triggers :{rows}")
    return rows 




def update_trigger(record_id):
    try :

        con = psycopg2.connect(host='db', port="5432" , user="postgres" ,password ="dariush", database="postgres")
        cursor = con.cursor()

        MODIFY_QUERY = f""" UPDATE "C_O_API_App_trigger" SET is_fired = FALSE WHERE ID = {record_id} ; """
        cursor.execute(MODIFY_QUERY)
        
        con.commit()
        print("modifying trigger from database succeeded...")    
        cursor.close()
    except :
        connection.rollback()
        print("modifying trigger from database failed...")



def run_action(record , data):
    sample_of_operator = operator(record[2]).value
    record[4] = False
    print(f"the {data['symbolisin']} stock is bught!!")
    
    print("email has been sent to the receiver email !!")
    update_trigger(record[0])
    del record
                            
bole_f = False


def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    print("the flowting data : ")
    print(data)
    symbolisin = data["symbolisin"]
    triggers_all = read_triggers() # a list of tuple [(..) , (..)]
    list_tuple = list()
    for tuples in triggers_all :
        list_tuple.append(list(tuples))

    for record in list_tuple :
        bole_f = False
        if record[4] == True:
            
            if record[1] == data["symbolisin"]:
                value = int(data[record[5]])
                if record[2] == int(operator.equal.value) :
                    
                    if record[3] == value:
                        
                        bole_f = True
                       
                elif record[2] == int(operator.greater_or_equal.value) :
                    if record[3] >= value:
                        
                        bole_f = True
                                                     
                elif record[2] == int(operator.less_or_equal.value) :
                    if record[3] <= value:
                        
                        bole_f = True
                            
                elif record[2] == int(operator.greater.value) :
                    if record[3] > value:
                        
                        bole_f = True
                            
                elif record[2] == int(operator.less.value) :
                    if record[3] < value:
                        
                        bole_f = True                         
                                      
                else:
                    print("something is wrong...")
            else: 
                print("this stock is not matter! :| ")
        else:
            print("there is no trigger!!! ")
        if bole_f == True :
            run_action(record , data )
            # sending_email.email_service(record)
            publish("adding_live_data", record)


 

channel.basic_consume(queue='hello2', on_message_callback=callback, auto_ack=True) 
print(' [*] start consuming in Trigger service. To exit press CTRL+C')
channel.start_consuming()


# ======================================================================