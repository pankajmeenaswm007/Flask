from flask import *
from connection_with_oops import *
from fileinput import filename 
ob=myclass()
app=Flask(__name__)

d=[]
@app.route("/")
def home():
    d=ob.getdata("item")
    return render_template("home.html",data=d)

@app.route("/admin")
def admin():
    return render_template("login.html")

@app.route("/add")
def base():
    return render_template("add.html")


# login admin
@app.route("/ulogin",methods=["POST"])
def ulogin():
    d=[]
    d=ob.getdata("login")
    nam=request.form["user"]
    pas=request.form["psw"]
    j=0
    temp=len(d)
    for i in range(len(d)):
        j=j+1
        if(d[i][1]==nam and d[i][2]==pas):
            return render_template("add.html")
        if(j==temp):
            return render_template("login.html",msg="Wrong user name password")

# insert item
@app.route("/insert",methods=["POST"])
def insert():
    my=[]
    ufile=request.files["xfile"]
    utitle=request.form["title"]
    uprice=request.form["price"]
    ufile.save("static/image/"+ufile.filename)
    my=[ufile.filename,utitle,uprice]
    ob.insert("item",my)
    return render_template("add.html")

# show data
@app.route("/show")
def show():
    d=ob.getdata("item")
    return render_template("show.html",data=d)

# delete
@app.route("/del/<un>")
def delete(un):
    ob.delete("item",un)
    return redirect("/show")

if __name__ == '__main__':  
    app.run(debug = True)  