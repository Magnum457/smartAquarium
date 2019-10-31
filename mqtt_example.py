import paho.mqtt.client as mqtt

# O callback para quando o cliente receber um CONNACK do servidor
def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo de resultado: " + str(rc))
    
    # Subscribing em on_connect() siginifica que se você perder a conexão
    # e reconectar ela então que os subscriptions serão reiniciados
    client.subscribe("cozinha/jacquin")

# O callback quando uma PUBLISH message é recebida pelo servidor
def on_message(client, userdata, msg):
    print(msg.payload)
    
    
# Dados do cliente
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)

for i in range(5):
    client.publish("teste/jacquin", payload = "Dentro da carro hj vai ter putarria")
# Bloqueio de chamadas que processam o tráfego de rede, despacha retornos
# de chamada e manipula a reconecção
# Outras funções loop*() são avaliaveis que dão uma interface paralela e uma interface manual
client.loop_forever()