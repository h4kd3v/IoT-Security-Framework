import paho.mqtt.client as mqtt
import ssl
from utils.logger import log

def on_connect(client, userdata, flags, rc):
    log(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    log(f"Message received: {msg.payload.decode()}")

def setup_secure_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set(ca_certs="path/to/ca.crt",
                   certfile="path/to/client.crt",
                   keyfile="path/to/client.key",
                   tls_version=ssl.PROTOCOL_TLSv1_2)

    client.connect("mqtt.example.com", 8883, 60)
    client.loop_forever()

if __name__ == "__main__":
    setup_secure_mqtt()
