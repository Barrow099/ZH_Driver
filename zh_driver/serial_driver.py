import os
import platform
import subprocess
import time

import serial


class SerialDriver:
    def __init__(self, config):
        print("Initializing driver...")
        print(config)
        general = config["General"]
        self.port = general["port"]
        self.baud = int(general["baudrate"])
        self.comamnd_base = general["command"]
        self.device = serial.Serial()


        while not self.device.is_open:
            self.connect()
            time.sleep(2)


    def startLoop(self):
        print("Connected to device")
        while self.device.is_open:
            try:
                line_b = self.device.readline()
                line = str(line_b,"UTF-8").strip()
                cmd = self.comamnd_base.replace("{value}",line)
                #print(cmd)
                subprocess.call(cmd.split(" "), stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            except serial.SerialException:
                print("Connection lost")
                break
        print("Lost connection")
        #time.sleep(2)
        self.device = serial.Serial()
        while not self.device.is_open:
            self.connect()
            time.sleep(2)

    def connect(self):
        try:
            if platform.system() == "Windows":
                self.device = serial.Serial(self.port, self.baud)
                self.startLoop()
            else:
                self.device = serial.Serial("/dev/" + self.port, self.baud)
                self.startLoop()
        except serial.SerialException:
            print("Connection error")
