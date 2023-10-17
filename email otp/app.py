from flask import *
import random
from flask_mail import*
app = Flask(__name__)
mail=Mail(app)
app.secret_key="xyz"
# start mail configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'saktibook@gmail.com'
app.config['MAIL_PASSWORD'] = 'bemrsvjbbthtgtlp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
# end configuration

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/varify",methods=["POST"])
def varify():
   session['mail']=request.form["email"]
   session['otp']=otp=random.randint(111111,999999)
   msg = Message('Forget Password configration', sender = 'saktibook@gmail.com', recipients =[session['mail']])
   msg.body = "This OTP -> "+ str(otp) +" for forgetpassword Please do not share otp to anyone"
   mail.send(msg)
   return render_template("otp.html")

@app.route("/otp",methods=["POST"])
def otp():
   cod=request.form["xotp"]
   if(str(cod)==str(session['otp'])):
      return render_template("otp.html",msg="email varify successful")
   else:
      return render_template("otp.html",msg="otp not match!!!!")



if __name__ == '__main__':
   app.run(debug = True)
