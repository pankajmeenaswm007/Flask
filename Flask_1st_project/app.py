from flask import *
l=[]  

var="9"
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/home') #decorator drfines the   
def home():  
    return render_template("home.html",data="Default") 
  

@app.route('/')
def form():
    
    return render_template("form.html")

@app.route('/list',methods=["GET","POST"])
def list():
    
    if(request.method=="POST"):
        
        name=request.form["xname"]
        sale=request.form["xpsw"]
        city=request.form["xcity"]
           
        d=[(len(l)+1),name,sale,city] 

        l.append(d)
    
    return render_template("list.html",data=l)

@app.route("/del/<un>")
def del_(un):
    for i in range(0,len(l)):
        if int(un)==l[i][0]:
          l.pop(i)
          break
    return redirect("/list")

@app.route("/update/<my>")

def update(my):
    up=[]
    var=my
    for i in range(0,len(l)):
        if(str(my)==str(l[i][0])):
            print("yes")
            up.append(l[i])
            break
    return render_template("update.html",update=up)

@app.route("/list2",methods=["GET","POST"])
def list2():

    if(request.method=="POST"):
        uid=request.form["xid"]
        name=request.form["xnam"]
        sale=request.form["psw"]
        city=request.form["xct"]
        #d=[" ",name,sale,city]

        for i in range(len(l)):
            if(uid==str(l[i][0])):
                l[i][1]=name
                l[i][2]=sale
                l[i][3]=city

        return render_template("list.html",data=l)
        
    
        

if __name__ =='__main__':  
    app.run(debug = True)  