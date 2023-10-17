from flask import *
from connection_with_oops import *
ob=myclass()

# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",root="user",password="",database="bhai")
# mycur=mydb.cursor()

l=[]  
d=[]
a=[]
app = Flask(__name__) #creating the Flask class object   
 ## show all data
@app.route('/') #decorator drfines the   
def home():  
    # a.append(ob.getdata("one"))
    l=ob.getdata("one")
    # a.append(l)
    return render_template("home.html",data=l)

## delete table row
@app.route("/delete/<id>")
def delete(id):
    ob.delete("one",id)
    return redirect('/')   

## insert data
@app.route("/add")
def add():
    return render_template("form.html")

@app.route("/list",methods=["GET","POST"])
def list():
    if(request.method=="POST"):
        name=request.form["uname"]
        city=request.form["ucity"]
        sale=request.form["usale"]
        
        d=[name,city,sale]
        ob.insert("one",d) 
    
    return redirect("/")

## edit
@app.route("/edit/<id>")
def edit(id):
    a=ob.getdata("one")
    edt=[]
    for i in range(len(a)):
        if(str(id)==str(a[i][0])):
            edt.append(a[i])
            break
         
    return render_template("update.html",data=edt)

@app.route("/myedit" ,methods=["GET","POST"])
def myedit():
    my=[]
    if(request.method=="POST"):
        id=request.form["uid"]
        name=request.form["uname"]
        city=request.form["ucity"]
        sale=request.form["usale"]
        my=[id,name,city,sale]
    ob.update("one",my)
    return redirect("/")




if __name__ == '__main__':  
    app.run(debug = True)  