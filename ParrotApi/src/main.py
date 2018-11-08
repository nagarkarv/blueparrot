from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

blueParrots = [
	{
		"name": "Macaws"
	},
	{
		"name": "Conures"
	},
	{
		"name": "Budgies",
	},
	{
		"name": "Parrotlets"
	}
]

class Parrot(Resource):
	def get(self, parrotName):
		for parrot in blueParrots:
			if(parrotName == parrot["name"]):
				return {parrotName: parrot}
		return {'error': 'Not Found'}, 404

	def put(self, parrotName):
		return {'put': 'Hello'}, 200
	
	def post(self, parrotName):
		pass

class ParrotList(Resource):
	def get(self):
		return { "blue": blueParrots }, 200

api.add_resource(Parrot, '/blueparrot/name/<string:parrotName>')
api.add_resource(ParrotList, '/blueparrot')

if __name__ == '__main__':
    app.run(port=5000,debug=True)