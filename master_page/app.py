from flask import *
from connection_with_oops import *
ob=myclass()
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/show")
def show():
    return render_template("show.html")
if __name__ == '__main__':  
    app.run(debug = True)  