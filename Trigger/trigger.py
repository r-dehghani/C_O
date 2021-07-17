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


class trigger_definition():
    user_symbol = "shepeli"
    oper = 1
    desired_price = 1800


credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq', 5672 , '/' , credentials , heartbeat=60)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_declare(queue='hello2' , exclusive=True)
channel.queue_bind(exchange='logs', queue="hello2")

def callback(ch, method, properties, body):
    print(" [x] Received ")
    data = json.loads(body)
    print(data)
    print(type(data))
    if trigger_definition.user_symbol == data["symbolisin"]:
        if trigger_definition.oper == operator.equal.value :
            if trigger_definition.desired_price == int(data['top']):
                print(f"the {data['symbolisin']} stock is bught in equal!!!")

        elif trigger_definition.oper == operator.greater_or_equal.value :
            if trigger_definition.desired_price >= int(data['top']):
                print(f"the {data['symbolisin']} stock is bught in greater_or_equal!!!")

    
        elif trigger_definition.oper == operator.less_or_equal.value :
            if trigger_definition.desired_price <= int(data['top']):
                print(f"the {data['symbolisin']} stock is bught in less_or_equal!!!")

    
        elif trigger_definition.oper == operator.greater.value :
            if trigger_definition.desired_price > int(data['top']):
                print(f"the {data['symbolisin']} stock is bught in greater!!!")

    
        elif trigger_definition.oper == operator.less.value :
            if trigger_definition.desired_price < int(data['top']):
                print(f"the {data['symbolisin']} stock is bught in less!!!")
        else:
            print("Error...")
    else:
        print("nothing happened")


    # if data["symbolisin"] == "shepeli" :
    #     if int(data["top"]) >= 1100 :
    #         print(f"the trigger is activated : symbol : {data['symbolisin']}-- Price {data['top']}")
    #         desired_data = data
    # else:
    #     print("!!!your desiered symbol isn't reached to the top price!!!")
    


# if(TriggerDefinition.Operator == Operator.LessThan) 
# {
#    var condition =  leftOperand < rightOperand;
# }

# if(TriggerDefinitino.Operator == Operator.GreaterThan)
# {
#     var condition = leftOperand > rightOperand;
# }
    

channel.basic_consume(queue='hello2', on_message_callback=callback, auto_ack=True) 
print(' [*] start consuming in Trigger service. To exit press CTRL+C')
channel.start_consuming()


