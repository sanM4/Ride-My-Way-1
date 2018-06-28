from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt) 
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from flask import Flask
from flask import Response
import json, decimal
import psycopg2
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'this are the secret keys for now'
jwt = JWTManager(app)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='XABC'")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Users( id SERIAL, username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,PRIMARY KEY(id))''')

cur.execute('''CREATE TABLE IF NOT EXISTS Users( id SERIAL, username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,PRIMARY KEY(id))''')
@app.route("/", methods=["POST"])
def login():
    cur = conn.cursor()
    data = parser.parse_args()
    if data["username"] and data["email"] and data["password"]:
        try:
            if cur.execute('''SELECT from Users where username=data["username"] '''):
                return {'message': 'that username is taken'}
            username = data['username']
            email = data['email']
            password = generate_password_hash(data['password'])
                
            cur.execute('''INSERT INTO Users(username, email, password) VALUES(username, email, password)''')
            conn.commit()
            return {'message': 'User {} was created'.format(data['username']), 'access_token': create_access_token(identity = data['username']),'refresh_token': create_refresh_token(identity = data['username'])}
        except:
            return {'message': 'Something went wrong'}, 500    
        finally:
            cur.close()
            conn.close()
    else:
        return {'message':'enter email, password, email'}

if __name__ == '__main__':
    app.run(debug=True) 



