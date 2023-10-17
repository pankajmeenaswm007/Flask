from flask import *
from fileinput import filename
from connection_with_oops import *
ob=myclass()
app=Flask(__name__)
l=[]
show=[]
@app.route("/")
def home():
    return render_template("Sign-up.html")

# add user
@app.route("/sign",methods=["GET","POST"])
def sign():
    j=0
    ch=ob.getdata("login2")
    if(request.method=="POST"):
        name=request.form["xname"]
        mob=request.form["xtel"]
        xpass=request.form["xpsw"]

        mfile=request.files["xfile"]
        mfile.save("static/image/"+mfile.filename)

        l=[name,mob,xpass,mfile.filename]
        temp=len(ch)
        for i in range(len(ch)):
            j=j+1
            if(ch[i][2]==mob):
                return render_template("Sign-up.html",msg="Number is alerady use")
            if(temp==j):
                if(len(name)>=5 and len(mob)==10 and len(xpass)>=5):
                    ob.insert("login2",l)  
                    return redirect("/show")
                else:
                    return render_template("Sign-up.html",msg="Wrong details")
    else:
        return render_template("Sign-up.html")

# show user
@app.route("/show")
def user():
    show=ob.getdata("login2")
    return render_template("show.html",data=show)

# forget page
@app.route("/forget")
def forget():
    return render_template("Forgot-pass.html")

@app.route("/forgetuser" , methods=["GET","POST"])
def forgetuser():
    j=0
    ch=ob.getdata("login2")
    if(request.method=="POST"):
        mob=request.form["xtel"]
        xpass=request.form["xpsw"]
        l=[mob,xpass]
        temp=len(ch)
        for i in range(len(ch)):
            j=j+1
            if(ch[i][2]==mob):
                ob.update("login2",l)
                return render_template("Forgot-pass.html" ,msg="Successful reset password")
                break
            if(temp==j):
                return render_template("Forgot-pass.html",msg="Wrong user mobile number !!!!")
    return redirect("/show")

# login page
@app.route("/Loginp")
def Loginp():
    return render_template("Login-Page.html")

# login user
@app.route("/loginuser", methods=["GET","POST"])
def login():
    j=0
    ch=ob.getdata("login2")
    if(request.method=="POST"):
        mob=request.form["xtel"]
        xpass=request.form["xpsw"]
        # l=[mob,xpass]
        temp=len(ch)
        for i in range(len(ch)):
            j=j+1
            if(ch[i][2]==mob and ch[i][3]==xpass):
                l=[mob,ch[i][1],ch[i][4]]
                return render_template("base.html", data=l)
            if(temp==j):
                return render_template("Login-Page.html",msg="Wrong user details !!!!")


if __name__ == '__main__':  
    app.run(debug = True)  