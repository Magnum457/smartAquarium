import paho.mqtt.client as mqtt

# O callback para quando o cliente receber um CONNACK do servidor
def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo de resultado: " + str(rc))
    

# O callback quando uma PUBLISH message é recebida pelo servidor
def on_message(client, userdata, msg):
    print(msg.payload)
    
def send_message(topic, payload):
    # Dados do cliente
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message


    client.connect("localhost", 1883, 60)

    client.publish(topic, payload)

    #client.loop_forever()
