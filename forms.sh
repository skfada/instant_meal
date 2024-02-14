#script for executing the database query from bash
cat ./main/database/schema.sql | mysql -uroot -p
------------------
show databases;
--------------------
 "for removing carriage retuen spaces in file"
sed -i 's/\r$//' ./*
sed -i "s/mysql+mysqldb:/mysql:/" ./main/database/config.py
-----
python3 -m pip install flask_bcrypt
------
#creating a new enabled file for the instant meal in nginx
sudo touch /etc/nginx/sites-enabled/instantmeal
sudo vim /etc/nginx/sites-enabled/instantmeal
-------------------
iserver {
    listen 80;
    server_name instant-meal.skfada.tech;

    location /static {
        alias /home/ubuntu/instant_meal/main/static;
    }

    location / {
        proxy_pass http://localhost:8000;
        include /etc/nginx/proxy_params;
        proxy_redirect off;
    }

}
=================
sudo lsof -i :8000

sudo kill -9 195187
sudo kill -9 195189
sudo kill -9 195190
sudo kill -9 195191

---------------
number of workers = `nproc -all`* 2 + 1 = 3
--------
gunicorn --bind 0.0.0.0:8000 run:app

gunicorn -w 3 run:app
---
sudo vim /etc/nginx/nginx.conf

sudo rm /etc/nginx/sites-enabled/instantmeal
--



# POST RESGISTRATION TESTING
name="user4"
mail="user4@gmail.com"
pass1="0000000000"
pass2="0000000000"
curl --location http://127.0.0.1:5000/api/user/register --data username=$name --data email=$mail --data pwd1=$pass1 --data pwd2=$pass2
## STATUS: TESTED OKAY


# POST LOGIN TESTING
name="user4"
pass2="0000000000"
curl --location http://127.0.0.1:5000/api/user/login --data username=$name --data pwd=$pass2
## STATUS: TESTED OKAY


# PASSWORD RESET TESTING
name="user1"
mail="user1@gmail.com"
pass1="0000000000"
pass2="0000000000"
curl --location http://127.0.0.1:5000/api/user/password_reset --data username=$name --data email=$mail --data pwd1=$pass1 --data pwd2=$pass2
## STATUS: TESTED OKAY


# USER INFORMATION UPODATE TESTING


curl --location http://127.0.0.1:5000/api/user/update
