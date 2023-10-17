from flask import *
from connection_with_oops import *
from fileinput import filename
from flask_mail import *
import random

ob=myclass()
app =Flask(__name__)

app.secret_key="xyz"
# start mail configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pm1405105@gmail.com'
app.config['MAIL_PASSWORD'] = 'reytkhhxtliefylq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
# end configuration

show=[]
Mob=""
app.secret_key ="mylogin"
@app.route('/')
def hello_world():
   return render_template("layout.html")


@app.route("/show")
def show():
   l=ob.getdata("register")
   my=ob.rowcount()
   # show=[l,my]
   return render_template("show.html" ,data=l,rc=my)

@app.route("/login")
def login():
   return render_template("login.html")

@app.route("/register")
def register():
   return render_template("register.html")

@app.route("/otp")
def otp():
   return render_template("otp.html")

@app.route("/forget")
def forget():
   
   return render_template("forget.html")


# email otp
@app.route("/varify",methods=["POST"])
def varify():
   gmail=request.form["email"]
   session['uotp']=request.form["xotp"]
   session['otp']=otp=random.randint(111111,999999)
   msg = Message('Forget Password configration', sender = 'pm1405105@gmail.com', recipients =[gmail])
   msg.body = "This OTP -> "+ str(otp) +" for forgetpassword Please do not share otp to anyone"
   mail.send(msg)
   return redirect("/uotp")

@app.route("/uotp")
def uotp():
   if(str(session['uotp'])==str(session['otp'])):
      return render_template("otp.html",msg="email varify successful")
   else:
    return render_template("otp.html",msg="email varify not found")

# add user
@app.route("/add" ,methods=["GET","POST"])
def add():
   l=ob.getdata("register")
   add=[]
   if(request.method=="POST"): 
      name=request.form["xname"]
      mobile=request.form["xtel"]
      psw=request.form["xpsw"]
      session['mail']=email=request.form["xemail"]
      date=request.form["xdate"]

      file=request.files["xfile"]
      file.save("static/image/"+file.filename)

      add=[name,mobile,psw,email,date,file.filename]
      temp=len(l)
      j=0
      for i in range(len(l)):
         j=j+1
         if(l[i][2]==mobile):
            return render_template("register.html", my="Number is alerady used")
            break
      if(temp==j):
         if(len(name)>5  and len(psw)>=6 and len(email)>=10):
            qry=ob.insert("register",add)
            return render_template("otp.html",data=add)
         return render_template("register.html",my="Please enter user details")
            
   else:
        return redirect("/login")




# login user
@app.route("/userlogin",methods=["GET","POST"])
def userlogin():
   ins=[]
   l=ob.getdata("register")
   if(request.method=="POST"):
      mobile=request.form["xtel"]
      psw=request.form["xpsw"]
      temp=len(l)
     
      j=0
      for i in range(len(l)):
         j=j+1
         if(l[i][2]==mobile and l[i][3]==psw):
            ins=l[i]
            return render_template("user.html", my=ins)
            break
         elif(temp==j):
             return render_template("login.html", my="Please enter user curect details")
             break
   else:
      return redirect("/show")

# reset password
@app.route("/userforget",methods=["GET","POST"])
def userforget():
   l=ob.getdata("register")
   if(request.method=="POST"):
      mobile=request.form["xtel"]
      
      for i in range(len(l)):
         if(l[i][2]==mobile):
            session['mob']=mobile
            return render_template("userforget.html")
            break

   else:
      return redirect("/forget")

@app.route("/userpsw",methods=["GET","POST"])
def userpsw():
   if(request.method=="POST"):
      password=request.form["xpsw"]
      ss=ob.update("register",password,session['mob'])
      return redirect("/login")
   else:
      return render_template("/register")
   


if __name__ == '__main__':
   app.run(debug = True)
