from flask import Flask, render_template
#Flask is imorted from the flask module
#render_template is imported from the flask module to render html templates that will be created
from flask_bootstrap import Bootstrap5
#Bootstrap is imported from the flask_bootstrap module to use bootstrap in the app
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('home.html')
#Here is where the home page will be created and rendered, the def home is a function that returns the home.html template
@app.route('/about')
def about():
    return render_template('about.html')
#Here is where the about page will be created and rendered, the def about is a function that returns the about.html template
#The app.run(debug=True) is used to run the app in debug mode, which means that the app will be reloaded when changes are made to the code
#The app.run() is used to run the app on the local server
#The if __name__ == '__main__': is used to check if the app is being run directly or imported as a module in this cas it is being run directly
#in the .flaskenv file, the FLASK_ENV=development is set to run the app in debug mode because of the same reason as above the reason we write it again is to ensure that the app is run in debug mode this time not just in the app.py file
#Also both debug modes show you an error when you make a mistake in the code, but the flask debug mode is more detailed and shows you the line number of the error
if __name__ == '__main__':
    app.run(debug=True)