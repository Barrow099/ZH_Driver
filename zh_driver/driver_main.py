import configparser
import os
from .serial_driver import SerialDriver



def loadConfig():
    configFile = "/etc/zh/config.cfg"
    config = configparser.ConfigParser()
    if os.path.exists(configFile):
        print("Config file: " + os.path.abspath(configFile))
        config.read(configFile)
    else:
        print("Config not found, writing default config to file")
        config["General"] = {}
        general = config["General"]
        general["port"] = "ttyUSB0"
        general["baudrate"] = "9600"
        general['command'] = "amixer -c 1 set Master {value}%%"
        with open(configFile,"w") as configfile:
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