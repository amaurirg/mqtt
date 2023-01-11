#!/usr/bin/env python3
import paho.mqtt.client as mqtt


def conectou(client, userdata, flags, rc):
    print(f"Conectado! Código recebido: {str(rc)}")
    client.subscribe("testes/primeiro")


def chegou_mensagem(client, userdata, msg):
    dado = str(msg.payload.decode())
    print(f"{msg.topic} {dado}")


client = mqtt.Client()
client.on_connect = conectou
client.on_message = chegou_mensagem
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
