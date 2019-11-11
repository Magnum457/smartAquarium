import paho.mqtt.client as mqtt

# Retorna o identificador do aquario
def getAquarioId():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
    

  return "SmarthAquario#"+str(cpuserial)

# O callback para quando o cliente receber um CONNACK do servidor
def on_connect(client, userdata, flags, rc):
    print(getAquarioId() + " conectado com codigo de resultado: " + str(rc))
    
    # Subscribing em on_connect() siginifica que se você perder a conexão
    # e reconectar ela então que os subscriptions serão reiniciados
    # client.subscribe("cozinha/jacquin")

# O callback quando uma PUBLISH message é recebida pelo servidor
def on_message(client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic + " -> " + message)
    print(getAquarioId())
    
# Dados do cliente
client = mqtt.Client(getAquarioId())
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)

client.subscribe("topico/teste") # Subscribe

#for i in range(5):
#    client.publish("teste/jacquin", payload = "Dentro da carro hj vai ter putarria")
# Bloqueio de chamadas que processam o tráfego de rede, despacha retornos
# de chamada e manipula a reconecção
# Outras funções loop*() são avaliaveis que dão uma interface paralela e uma interface manual
client.loop_forever()