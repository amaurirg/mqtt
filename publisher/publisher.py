#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from time import sleep


TOPICO = "testes/primeiro"
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

while True:
    st = "Meu computador"
    payload = st.encode()
    client.publish(TOPICO, payload, qos=0)
    print(f"TOPICO {payload.decode()}")
    sleep(5)
