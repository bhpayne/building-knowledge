### Operating system ###
# tested on Ubuntu 14.04 64bit
#http://www.ubuntu.com/download/desktop

### install required software packages ###
## install pip ##
sudo apt-get install python-pip -y

## install redis ##
# on Ubuntu #
sudo apt-get install redis-server -y

#http://redisdesktop.com/download
wget https://github.com/uglide/RedisDesktopManager/releases/download/0.8.2/redis-desktop-manager_0.8.2-117_amd64.deb
sudo dpkg -i redis-desktop-manager_0.8.2-117_amd64.deb # expect errors from this attempt
sudo apt-get -f install -y # this resolves the missing packages for redis-desktop
sudo dpkg -i redis-desktop-manager_0.8.2-117_amd64.deb

## install redis for python ##
sudo pip install redis

## install docx parser for python ##
sudo pip install python-docx

## install yaml for python ##
sudo pip install pyyaml

## install pdfminer ##
# Note: do not run "sudo apt-get install python-pdfminer" as this package is broken

# https://pypi.python.org/pypi/pdfminer/
wget https://pypi.python.org/packages/source/p/pdfminer/pdfminer-20140328.tar.gz

tar zxvf pdfminer-20140328.tar.gz
cd pdfminer-20140328
sudo python setup.py install

