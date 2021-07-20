import psycopg2
import pika 
import sys , json
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

# con = psycopg2.connect(host='db', port="5432" , user="postgres" ,password ="dariush", database="postgres")
# cursor = con.cursor()

# SELECT_QUERY = """ SELECT * FROM "C_O_API_App_trigger" ORDER BY id DESC LIMIT 1; """
# cursor.execute(SELECT_QUERY)
# row = cursor.fetchone()
# con.commit()

# DELETE_QUERY = """ DELETE FROM "C_O_API_App_trigger"; """
# cursor.execute(DELETE_QUERY)
# con.commit()

# cursor.close()
# =======================================================================
# class trigger_definition():

#     user_symbol = row[0]
#     oper = row[1]
#     desired_price = row[2]

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
    rows = cursor.fetchall()
    # print(row[0] , type(row[1]))
    # print(row[1] , type(row[2]))
    # print(row[2] , type(row[3]))
    con.commit()    
    cursor.close()
    print(rows)
    return rows 

triggers_all = read_triggers()

list1 = list()
def callback(ch, method, properties, body):



    print(" [x] Received ")
  
    data = json.loads(body)
    print("the flowting data : ")
    symbolisin = data["symbolisin"]
    triggers = list(triggers_all)
    for record in triggers_all :
        if record[1] == symbolisin :
            list1.append(record)
    print(data)
    for row in list1:
        if row != None:
            
            print("trigger data  exists!")


            if row[1] == data["symbolisin"]:
                if row[2] == int(operator.equal.value) :
                    if row[3] == int(data['top']):
                        print(f"the {data['symbolisin']} stock is bught in equal!!!")
                        # del trigger_definition1
                        
                elif row[2] == int(operator.greater_or_equal.value) :
                    if row[3] >= int(data['top']):
                        print(f"the {data['symbolisin']} stock is bught in greater_or_equal!!!")
                        # del trigger_definition1
            
                elif row[2] == int(operator.less_or_equal.value) :
                    if row[3] <= int(data['top']):
                        print(f"the {data['symbolisin']} stock is bught in less_or_equal!!!")
                        # del trigger_definition1
            
                elif row[2] == int(operator.greater.value) :
                    if row[3] > int(data['top']):
                        print(f"the {data['symbolisin']} stock is bught in greater!!!")
                        # del trigger_definition1
            
                elif row[2] == int(operator.less.value) :
                    if row[3]< int(data['top']):
                        print(f"the {data['symbolisin']} stock is bught in less!!!")
                        # del trigger_definition1
                else:
                    print("something is wrong...")
            else: 
                print("this stock is not matter! :| ")
        else:
            print("there is no trigger!!! ")


        # if trigger_definition1.user_symbol == data["symbolisin"]:

    #         if trigger_definition1.oper == int(operator.equal.value) :
    #             if trigger_definition1.desired_price == int(data['top']):
    #                 print(f"the {data['symbolisin']} stock is bught in equal!!!")
    #                 del trigger_definition1
                    
    #         elif trigger_definition1.oper == int(operator.greater_or_equal.value) :
    #             if trigger_definition1.desired_price >= int(data['top']):
    #                 print(f"the {data['symbolisin']} stock is bught in greater_or_equal!!!")
    #                 del trigger_definition1
        
    #         elif trigger_definition1.oper == int(operator.less_or_equal.value) :
    #             if trigger_definition1.desired_price <= int(data['top']):
    #                 print(f"the {data['symbolisin']} stock is bught in less_or_equal!!!")
    #                 del trigger_definition1
        
    #         elif trigger_definition1.oper == int(operator.greater.value) :
    #             if trigger_definition1.desired_price > int(data['top']):
    #                 print(f"the {data['symbolisin']} stock is bught in greater!!!")
    #                 del trigger_definition1
        
    #         elif trigger_definition1.oper == int(operator.less.value) :
    #             if trigger_definition1.desired_price < int(data['top']):
    #                 print(f"the {data['symbolisin']} stock is bught in less!!!")
    #                 del trigger_definition1
    #         else:
    #             print("something is wrong...")
    #     else: 
    #         print("this stock is not matter! :| ")
    # else:
    #     print("there is no trigger!!! ")

channel.basic_consume(queue='hello2', on_message_callback=callback, auto_ack=True) 
print(' [*] start consuming in Trigger service. To exit press CTRL+C')
channel.start_consuming()


# ======================================================================