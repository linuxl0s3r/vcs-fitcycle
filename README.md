# OS Requirements (Tested on Ubuntu 18.04)

sudo apt-get update & sudo apt-get upgrade -y
sudo apt-get install python python-pip libmysqlclient-dev -y
pip install "django<2" mysqlclient statsd

# Install fitcycle

git clone https://github.com/theseanodell/vcs-fitcycle.git ~/fitcycle

# Run fitcycle

modify/update ID, Password and Server in fitcycle/settings.py


MYSQL_ID='db_user'
MYSQL_PASSWORD='abc123'
MYSQL_SERVER='10.10.10.10'


to run  ./startfitcycle.sh