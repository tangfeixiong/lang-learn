#!/usr/bin/python3

# Inspired by:
#   - https://github.com/sagaragarwal94/python_rest_flask/blob/master/server.py
#   - https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
#   - https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///example.db')
app = Flask(__name__)
api = Api(app)

credentials = [
    {
        'id': 1,
        'username': u'foo',
        'password': u'bar', 
        'disabled': False
    },
    {
        'id': 2,
        'username': u'baz',
        'password': u'qux', 
        'disabled': False
    }
]

class Authentication(Resource):
    def post(self):
        print(request.get_json())
        username = request.json['username']
        password = request.json['password']
        cred = [cred for cred in credentials if cred['username'] == username and cred['password'] == password]
        if len(cred) == 0:
            abort(404)
        print(cred)
        return jsonify({'id': cred[0]['id']})

class UserCreation(Resource):        
    def post(self):
        print(request.json)
        if not request.json or not 'username' in request.json:
            abort(400)
        cred = {
            'id': credentials[-1]['id'] + 1,
            'username': request.json['username'],
            'password': request.json.get('password', "1234"),
            'disabled': False
        }
        credentials.append(cred)
        return jsonify({'id': cred['id']})
    
class SecurityUpdation(Resource):        
    def put(self, id):
        if not request.json or not 'password' in request.json:
            abort(400)
        cred = [cred for cred in credentials if cred['id'] == id]
        if len(cred) == 0:
            abort(404)
        cred['password'] = request.json.get('password', "1234")
        return jsonify({'message': "updated"})

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName,FirstName,Title,
                             ReportsTo, BirthDate, HireDate, Address,
                             City, State, Country, PostalCode, Phone, Fax,
                             Email))
        return {'status':'success'}

    
class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

api.add_resource(Authentication, '/authenticate')
api.add_resource(UserCreation, '/users') # create user credential
api.add_resource(SecurityUpdation, '/users/<id>') # update user password


if __name__ == '__main__':
     app.run()
