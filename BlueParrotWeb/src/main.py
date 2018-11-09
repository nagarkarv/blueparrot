from flask import (
	Flask,
	render_template,
	request
	)

# Create the application instance
print('Creating webapp instance')
app = Flask(__name__, template_folder="templates")

@app.route('/GetList')
def GetList():
	print('get list')
	#response = request.post(, data=data)
	parrotList = [
		{	"Item": "data1" },
		{	"Item": "data2" }
	]
	return render_template('home.html', parrotList = parrotList) 	

# Create a URL route in our application for "/"
@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html', parrotList = [])

@app.route('/contactus')
def contactus():
	return "This is contact us page"

# if we are running in standalone mode, run the application
if __name__ == "__main__":
	print('running app.run')
	app.run(host='0.0.0.0', port=5002)
