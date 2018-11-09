from flask import (
	Flask,
	render_template,
	request
	)
import requests

# Create the application instance
print('Creating webapp instance')
app = Flask(__name__, template_folder="templates")

@app.route('/showDetails', methods=['GET', 'POST'])
def showDetails():
	print('Showing details')
	return render_template('showdetails.html', parrotDetails = [])

def GetList():
	print('get list')
	response = requests.get('http://localhost:5000/blueparrot')
	responseData = response.json()['blue']
	return responseData

# Create a URL route in our application for "/"
@app.route('/', methods=['GET', 'POST'])
def home():
	print("Home")
	if request.method == 'GET':
		return render_template('home.html', parrotList = GetList())	
	return render_template('home.html', parrotList = [])

@app.route('/contactus')
def contactus():
	return "This is contact us page"

# if we are running in standalone mode, run the application
if __name__ == "__main__":
	print('running app.run')
	app.run(host='0.0.0.0', port=5002)
