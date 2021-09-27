
from app import app, db
from models import User, UserSchema
from datetime import datetime
from flask import request, jsonify
import hashlib


user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/login", methods= ['POST'])
def login_user():
        email = request.json['email']
        password = request.json['password']

        password_hash = hashlib.sha256(password.encode())
        password_hash = password_hash.hexdigest()

        user = User.query.filter_by(email=email).first()

        if user:
                if user.password == password_hash:
                        user.lastlogintime = datetime.utcnow()
                        db.session.commit()
                        response = { 'message': 'Login Successful'}
                        return jsonify(response), 200
                else:
                        response = { 'message': 'Wrong Password!'}
                        return jsonify(response), 401
        else: 
                response = {'message': "Email doesn't exist"}
                return jsonify(response), 401


@app.route("/create", methods= ['POST'])
def create_user():
        name =  request.json['name']
        email = request.json['email']
        password = request.json['password']

        password_hash = hashlib.sha256(password.encode())
        password_hash = password_hash.hexdigest()

        new_user = User(name, email, password_hash)
        db.session.add(new_user)
        db.session.commit()
        
        return user_schema.jsonify(new_user)


@app.route("/list", methods= ['GET'])
def list_users():

        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)


@app.route("/list/<id>", methods= ['GET'])
def list_user(id):

        user = User.query.get(id)
        if user:
                return user_schema.jsonify(user)
        else:
                response = {
                        "Message" : "User doesn't exist"
                }
                return jsonify(response)


@app.route("/update/<id>", methods= ['PUT'])
def update_user(id):
        user = User.query.get(id)
        if user.name:
                name_new = request.json['name']
                email_new = request.json['email']

                user.name = name_new
                user.email = email_new
                db.session.commit()
                response = {
                        "message": "User name and email Updated"
                }
                return jsonify(response)
        else:
                response = {
                        "Message" : "User doesn't exist"
                }
                return jsonify(response)


@app.route("/delete/<name>", methods= ['DELETE'])
def delete_user(name):
        user = User.query.filter_by(name=name).first()
        if user:
                db.session.delete(user)
                re = f"user {name} is deleted"
                response = {"Message": re }
                return jsonify(response)
        else:
                response = {
                        "Message" : "User doesn't exist"
                }
                return jsonify(response)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
