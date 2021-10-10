
#distributed under GNU public license https://www.gnu.org/licenses/gpl.txt

#this program requires the script to be run on the same server as you
#have elasticsearch running
#change the server and port data according to your installation
#the program is simple, but should work fine for testing
#the program will cope with a mixture of string and numeric data
#however it would be wise to develop further if a variety of data types
#such as json is to be used


mqttServer="hydrogen.local"
mqttPort="1883"

# channelSubs="$SYS/#"
#use below as alternative to subscribe to all channels
channelSubs="#"

import paho.mqtt.client as mqtt
from datetime import datetime
from elasticsearch import Elasticsearch


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("pi1/temprature")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print('Hello World')
    print(msg.topic+" "+str(msg.payload))
    msg1 = msg.payload.decode("utf-8")

# this is the syntax to follow for the elasticSearch update taken from documentation
#    es.index(index="my-index", doc_type="test-type", id=42, body={"any": +str(msg.payload, "timestamp": datetime.now()})
#    {u'_id': u'42', u'_index': u'my-index', u'_type': u'test-type', u'_version': 1, u'ok': True}

# our implementation uses this to separate numeric(float) from string data

    # try:
    msg1 = float(msg1)
    es.index(index="temprature_pi1", doc_type="numeric", body={"topic" : msg.topic, "Float" : msg1, "timestamp": datetime.utcnow()})

    # except:
    #      es.index(index="temprature_pi1", doc_type="string", body={"topic" : msg.topic, "dataString" : msg1, "timestamp": datetime.utcnow()})

# by default we connect to elasticSearch on localhost:9200
es = Elasticsearch()

client = mqtt.Client("mainsys")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()






