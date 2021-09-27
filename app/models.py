from app import db, ma

class User(db.Model):
        __tablename__= "User"
        ids = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), unique=True)
        email = db.Column(db.String(), unique=True)
        password = db.Column(db.String)
        lastlogintime = db.Column(db.DateTime(), default = None)

        def __init__(self, name, email, password):
                self.name = name
                self.email = email
                self.password = password

class UserSchema(ma.Schema):
        class Meta:
                fields = ('ids', 'name', 'email', 'lastlogintime')