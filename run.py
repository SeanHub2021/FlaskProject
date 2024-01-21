import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
##capital F on Flask indicates is a class name, import the Flask cask
##import render_template from the Framework


app = Flask(__name__) ##create an instance of Flask and store it in a variable named app. Name of the package, __name__ is a built-in Python variable. Flask needs this to know where to look for templates and files. 
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/") ##a decorator starts with the @ symbol, its a way of wrapping functions. When we try to browse the root directory, by "/", it triggers the function
def index(): ##create function Index
    return render_template("index.html") ##call the render_template we imported from Flask earlier. Flask expects it to be in a directory named Templates, so we create that.
##leave 2 lines gap between functions to be PEP8 compliant


@app.route("/about")##this view we name "/about" also then becoems a URL
def about(): ##bind that to a view we will also call "about"
    data =[] ##initialise an empty array/list
    with open("data/company.json", "r") as json_data: ##python is opening the json file as 'r'ead only and assigning the contents of the file to a new variable, json_data
        data = json.load(json_data) ##we need to set our empty data list to equal the parsed json data we've sent through
    return render_template("about.html", page_title="About", company=data) ##create new variable company, and pass the 'data' we just created, after the function is ran.


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), ##using the OS module from the standard library to get the IP variable from the Library (if it exists), and if not 0.0.0.0 as default
        port=int(os.environ.get("PORT", "5000")), ##same for port, but as an integer 5000 - a common port. 
        debug=True) ##should never be in published or submitted work. Should always be =False in reality. 