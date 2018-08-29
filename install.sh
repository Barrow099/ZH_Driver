echo "Installing ZH-Driver v1.0 by BLSoft"
echo "Downloading files..."

mkdir "/tmp/zhdriver-install" > /dev/null 2>&1
wget -O "/tmp/zhdriver-install/ZH_Driver-1.0.0-py3.6.egg" "https://github.com/Barrow099/ZH_Driver/raw/master/dist/ZH_Driver-1.0.0-py3.6.egg" > /dev/null 2>&1
sudo apt-get -y install python3 python3-pip > /dev/null 2>&1
sudo pip3 install setuptools > /dev/null 2>&1
echo "Installing..."
sudo python3 -m easy_install "/tmp/zhdriver-install/ZH_Driver-1.0.0-py3.6.egg" > /dev/null 2>&1
rm -rf "/tmp/zhdriver-install" > /dev/null 2>&1
sudo mkdir /etc/zh > /dev/null 2>&1
sudo chmod 777 /etc/zh
echo "Done"

