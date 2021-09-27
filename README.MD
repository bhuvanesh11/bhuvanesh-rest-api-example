# bhuvanesh-rest-api-example

This is just a small implementation of rest api based on the requirement

The app s based on flask.

######## initialize db ########
install sqlite and the run the shell script create_table.sh

######## Build docker image ########
docker build -t flask-example .

######## Run app ########
docker run --rm -it -v /path/to/db/file:/db -p '8080:5000' flask-example

######## Test using ########

  1) curl -X POST \
		  -H "Content-Type: application/json" \
		  -d '{ "id": 1 , "name": "jim", "email": "jim@gmail.com", "password": "welcome@123" }
		  http://localhost:8080/create
  
  2) curl -X GET http://localhost:8080/list to list all users
  
  3) curl -X GET http://localhost:8080/list/1 to list user based on id
  
  4) curl -X PUT \
		  -H "Content-Type: application/json" \
		  -d '{ "name": "JIM", "email": "JIM@hmail.com" }
		  http://localhost:8080/update/1
		  
  5) curl -X POST \
		  -H "Content-Type: application/json" \
		  -d '{ "email": "JIM@gmail.com", "password": "welcome@123" }
		  http://localhost:8080/login

  6) curl -X DELETE http://localhost:8080/delete/JIM
