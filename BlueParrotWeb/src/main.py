from flask import (
	Flask,
	render_template
	)

# Create the application instance
print('Creating webapp instance')
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/contactus')
def contactus():
	return "This is contact us page"

# if we are running in standalone mode, run the application
if __name__ == "__main__":
	print('running app.run')
	app.run(host='0.0.0.0', port=5002)
	