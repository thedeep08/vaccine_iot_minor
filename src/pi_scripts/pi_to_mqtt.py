import sys
import paho.mqtt.client as mqtt # Import the MQTT library
import time # The time library is useful for delays
import Adafruit_DHT

mqttBroker ="helium.local"

client = mqtt.Client("TempHumid")
client.connect(mqttBroker) 

while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        client.publish("pi1/temprature", temperature)
        print("Just published", temperature, "to topic TEMPERATURE")
        time.sleep(1)



