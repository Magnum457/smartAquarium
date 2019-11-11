import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883

def on_connect():
    print('Conectado com o resultado de codigo:')

def on_disconnect():
    print('Desconectado')
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
print('Vamos ver se vai conectar: ')
client.connect('localhost', 1883)
print('teste')

client.disconnect()

