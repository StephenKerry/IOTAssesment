#!/usr/bin/env python3

from time import sleep
import time, os
from datetime import datetime

from sense_hat import SenseHat
from picamera2 import Picamera2
import json
from upload_cloudinary import upload_image
import paho.mqtt.client as mqtt

import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "/<YOUR-ID>/event/doorbell"  # chan 

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

print("Warming up camera...")
sleep(2)

output_file = "test.jpg"
print(f"Capturing image to {output_file}...")
picam2.capture_file(output_file)

picam2.stop()
print("Done.")
