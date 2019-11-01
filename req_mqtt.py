import paho.mqtt.client as mqtt

# O callback para quando o cliente receber um CONNACK do servidor
def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo de resultado: " + str(rc))
    

# O callback quando uma PUBLISH message é recebida pelo servidor
def on_message(client, userdata, msg):
    print(msg.payload)
    
def receive_message(topic):
    # Dados do cliente
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message


    client.connect("localhost", 1883, 60)

    client.subscribe(topic, qos=1)
    
    client.loop_forever()
