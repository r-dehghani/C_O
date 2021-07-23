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
    # print(row[1] , type(row[1]))
    # print(row[2] , type(row[2]))
    # print(row[3] , type(row[3]))
    con.commit()    
    cursor.close()
    print(f"rows is :{rows}")
    return rows 

triggers_all = read_triggers()
keys = list()

# for item in triggers_all :

#     keys.append(item[])
        
print(f"this is triggers_all : {triggers_all}")
list1 = list()
def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    print("the flowting data : ")
    print(data)
    symbolisin = data["symbolisin"]
    # triggers = list(triggers_all)
    for record in triggers_all :
        if record != None:
            # if record[1] == symbolisin :
                # list1.append(record)
    # for row in list1:
            print("trigger data  exists!")

            if record[1] == data["symbolisin"]:
                if record[2] == int(operator.equal.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] == int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in equal and asking_price!!!")
                            # del trigger_definition1
                            print(f"record before del is : {record}")
                            del record
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] == int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in equal and biding_price!!!")
                            print(f"record before del is : {record}")
                            del record
                            

                elif record[2] == int(operator.greater_or_equal.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] >= int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater_or_equal and asking_price!!!")
                            # del trigger_definition1
                            print(f"record before del is : {record}")
                            del record
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] == int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater_or_equal and biding_price!!!")
                        # del trigger_definition1
                            print(f"record before del is : {record}")
                            del record
                            

                elif record[2] == int(operator.less_or_equal.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] <= int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in less_or_equal and asking_price!!!")
                        # del trigger_definition1
                            print(f"record before del is : {record}")
                            del record
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] <= int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in less_or_equal and biding_price!!!")
                            print(f"record before del is : {record}")
                            del record
                            

                elif record[2] == int(operator.greater.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] > int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater and asking_price!!!")
                            # del trigger_definition1
                            print(f"record before del is : {record}")
                            del record
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] > int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in greater and biding_price!!!")
                            print(f"record before del is : {record}")
                            del record
                            

                elif record[2] == int(operator.less.value) :
                    if record[4] == 'asking_price': # it is Asking_price
                        if record[3] < int(data['asking_price']):
                            print(f"the {data['symbolisin']} stock is bught in less and asking_price!!!")
                            # del trigger_definition1
                            print(f"record before del is : {record}")
                            del record
                            
                    elif record[4] == 'biding_price': # it is biding_price
                        if record[3] < int(data['biding_price']):
                            print(f"the {data['symbolisin']} stock is bught in less and biding_price!!!")
                            print(f"record before del is : {record}")
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