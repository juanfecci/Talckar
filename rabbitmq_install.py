import os

os.system("sudo apt-get install rabbitmq-server")

os.system("sudo rabbitmqctl add_user user1 pass1")
os.system("sudo rabbitmqctl add_vhost host1")
os.system("sudo rabbitmqctl set_user_tags user1 tag1")
os.system('sudo rabbitmqctl set_permissions -p host1 user1 ".*" ".*" ".*"')