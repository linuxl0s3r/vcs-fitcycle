### Credits

This report was forked from https://github.com/bshetti/api_server.git. Bill Shetti is the original creator of Fitcycle. Modification have been made to the codebase and installation with input from Jacob Cherkas and myself.

## Contributors
Bill Shetti
Jacob Cherkas
Sean O'Dell

# OS Requirements (Tested on Ubuntu 18.04)

sudo apt-get update & sudo apt-get upgrade -y

sudo apt-get install python python-pip libmysqlclient-dev -y

pip install "django<2" mysqlclient statsd

# Install fitcycle

sudo git clone https://github.com/theseanodell/vcs-fitcycle.git ~/fitcycle

# Run fitcycle

cd fitcycle/

modify/update ID, Password and Server in fitcycle/settings.py

    MYSQL_ID='db_user'

    MYSQL_PASSWORD='abc123'

    MYSQL_SERVER='10.10.10.10'

Migrate Manage.py

    python manage.py migrate

to run  ./startfitcycle.sh