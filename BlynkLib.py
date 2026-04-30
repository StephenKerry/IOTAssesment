import socket
import time

class Blynk:
    def __init__(self, token, server='blynk.cloud'):
        self.token = token

    def run(self):
        time.sleep(0.1)

    def log_event(self, name, msg):
        print(f"[BLYNK EVENT] {name}: {msg}")
