import psycopg2 , pika , json

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


credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq', 5672 , '/' , credentials , heartbeat=60)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_declare(queue='hello2' , exclusive=True)
channel.queue_bind(exchange='logs', queue="hello2")

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


def delete_trigger(record_id):
    try :

        con = psycopg2.connect(host='db', port="5432" , user="postgres" ,password ="dariush", database="postgres")
        cursor = con.cursor()

        DELETE_QUERY = f""" DELETE FROM "C_O_API_App_trigger" WHERE ID = {record_id} ; """
        cursor.execute(DELETE_QUERY)
        
        con.commit()
        print("Deleting trigger from database succeeded...")    
        cursor.close()
    except :
        connection.rollback()
        print("Deleting trigger from database failed...")
 





        
# print(f"this is all available triggers : {triggers_all}")
# list1 = list()
def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    print("the flowting data : ")
    print(data)
    symbolisin = data["symbolisin"]
    triggers_all = read_triggers()
    for record in triggers_all :
        if record != None:
            
            # print("trigger data  exists!")

            if record[1] == data["symbolisin"]:
                if record[2] == int(operator.equal.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] == int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in equal and asking_price!!!")
                            
                            delete_trigger(record[0])
                            del record
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] == int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in equal and biding_price!!!")
                            
                            delete_trigger(record[0])
                            del record
                            

                elif record[2] == int(operator.greater_or_equal.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] >= int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater_or_equal and asking_price!!!")
                            
                            delete_trigger(record[0])
                            del record
                            
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] >= int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater_or_equal and biding_price!!!")
                       
                            delete_trigger(record[0])
                            del record
                            
                            

                elif record[2] == int(operator.less_or_equal.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] <= int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in less_or_equal and asking_price!!!")
                        
                            delete_trigger(record[0])
                            del record
                            
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] <= int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in less_or_equal and biding_price!!!")
                            
                            delete_trigger(record[0])
                            del record
                            
                            

                elif record[2] == int(operator.greater.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] > int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater and asking_price!!!")
                           
                            delete_trigger(record[0])
                            del record
                            
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] > int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater and biding_price!!!")
                            delete_trigger(record[0])
                            del record
                            
                            

                elif record[2] == int(operator.less.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] < int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in less and asking_price!!!")
                            # del trigger_definition1
                            delete_trigger(record[0])
                            del record
                            
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] < int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in less and biding_price!!!")
                            delete_trigger(record[0])
                            del record
                            
                            
            
                else:
                    print("something is wrong...")
            else: 
                print("this stock is not matter! :| ")
        else:
            print("there is no trigger!!! ")


 

channel.basic_consume(queue='hello2', on_message_callback=callback, auto_ack=True) 
print(' [*] start consuming in Trigger service. To exit press CTRL+C')
channel.start_consuming()


# ======================================================================