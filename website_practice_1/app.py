from flask import Flask #import Flask class, which is an instance of WSGI application, WSGI = web server gateway interface, how web server communicates with web app
from flask import render_template #help run templating in html file

app = Flask(__name__) #create instance of Flask class and assigns to variable app __name__ is a dunder which is a double underscore variable that is the name of the module

@app.route("/") #telling Flask which URL to trigger our function
def index(): #function name
    # return "<p>Hello, World!</p>" #what will be returned via web browser
    message = "This is the home page"
    return render_template('index.html', message = message)

if __name__== '__main__':
    app.run(debug=True)
    