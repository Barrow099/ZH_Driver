import configparser
import os
from .serial_driver import SerialDriver


def loadConfig():
    config = configparser.ConfigParser()
    if not os.path.exists("~/zh"):
        os.mkdir("~/zh")
    if os.path.exists("~/zh/config.cfg"):
        print("Config file: " + os.path.abspath("~/zh/config.cfg"))
        config.read("~/zh/config.cfg")
    else:
        print("Config not found, writing default config to file")
        config["General"] = {}
        general = config["General"]
        general["port"] = "ttyUSB0"
        general["baudrate"] = "9600"
        general['command'] = "amixer -c 1 set Master {value}%%"
        with open("~/zh/config.cfg","w") as configfile:
            config.write(configfile)
            
    return config


def startDriver(cfg):
    drv = SerialDriver(cfg)


def main():
    print("Starting ZH Multi Driver v1.0")
    print("Loadin config...")
    cfg = loadConfig()
    startDriver(cfg)






if __name__ == '__main__':
    main()    