import os
from flask import Flask ##capital F on Flask indicates is a class name, import the Flask cask


app = Flask(__name__) ##create an instance of Flask and store it in a variable named app. Name of the package, __name__ is a built-in Python variable. Flask needs this to know where to look for templates and files. 


@app.route("/") ##a decorator starts with the @ symbol, its a way of wrapping functions. When we try to browse the root directory, by "/", it triggers the function
def index(): ##create function Index
    return "Hello, World"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), ##using the OS module from the standard library to get the IP variable from the Library (if it exists), and if not 0.0.0.0 as default
        port=int(os.environ.get("PORT", "5000")), ##same for port, but as an integer 5000 - a common port. 
        debug=True) ##should never be in published or submitted work. Should always be =False in reality. 