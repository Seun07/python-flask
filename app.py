from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome to cloud computing training"

@app.route('/add')
def add():
    a=10
    b=15
    c=25
    d=a+b+c
    return "This is the added result " + str(d)


@app.route('/multiply')
def multiply():
    a=100
    b=50
    c=90
    d=a*b*c
    return "This is the multiplied result " + str(d)


@app.route('/mountain')
def mountain():
    mountains=["kilimanjaro", "everest", "idanre hills", "zuma rock", "olumo rock"]
    return render_template("index.html", mountain=mountains)


@app.route('/career')
def career():
    roles=["product manager", "marketing executive", "sales representative", "facility manager", "engineer"]
    return render_template("career.html", career=roles)


@app.route('/product')
def product():
    userDetails=["electronics", "phones", "tablets", "gaming device", "gaming pads"]
    return render_template("product2.html", product=userDetails)








if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5008, debug =True)


