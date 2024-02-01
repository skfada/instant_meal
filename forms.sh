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
