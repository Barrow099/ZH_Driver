echo "Installing ZH-Driver v1.0 by BLSoft"
echo "Downloading files..."

mkdir "/tmp/zhdriver-install" > /dev/null 2>&1
wget -O "/tmp/zhdriver-install/ZH_Driver-1.0.0-py3.6.egg" "https://github.com/Barrow099/ZH_Driver/raw/master/dist/ZH_Driver-1.0.0-py3.6.egg" > /dev/null 2>&1
sudo apt install python3 > /dev/null 2>&1
sudo apt install python3-pip > /dev/null 2>&1
sudo pip3 install setuptools > /dev/null 2>&1
echo "Installing..."
sudo python3 -m easy_install "/tmp/zhdriver-install/ZH_Driver-1.0.0-py3.6.egg" > /dev/null 2>&1
rm -r "/tmp/zhdriver-install" > /dev/null 2>&1
sudo mkdir /etc/zh > /dev/null 2>&1
sudo chmod 777 /etc/zh
echo "Adding autostart"
sudo echo "/usr/local/bin/zh-driver" > /etc/init.d/start_zh_driver
sudo chmod +x /etc/init.d/start_zh_driver
sudo ln -s /etc/init.d/start_zh_driver /etc/rc.d/
echo "Done"

