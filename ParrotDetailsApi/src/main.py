from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

parrotsDetails = [
			{
				"name": "Macaws",
				"country": "South America",
				"average_weight": "34-44 grams"
			},
			{
				"name": "Conures",
				"country": "Central & South America",
				"average_weight": "50-60 grams"
			},
			{
				"name": "Budgies",
				"country": "Australia",
				"average_weight": "80-70 grams"
			},
			{
				"name": "Parrotlets",
				"country": "Peru and Ecuador",
				"average_weight": "80-90 grams"
			}
		]

class ParrotDetails(Resource):
	def get(self, parrotName):
		for parrot in parrotsDetails:
			if(parrotName == parrot["name"]):
				return {'info': parrot}
		return {'error': 'Not Found'}

	def put(self, parrotName):
		return {'put': 'Hello'}, 200
	
	def post(self, parrotName):
		pass

class ParrotDetailsList(Resource):
	def get(self):
		return { "info": parrotsDetails }

api.add_resource(ParrotDetails, '/parrotdetails/name/<string:parrotName>')
api.add_resource(ParrotDetailsList, '/parrotdetails')

if __name__ == '__main__':
    app.run(port=5001, debug=True,host='0.0.0.0')