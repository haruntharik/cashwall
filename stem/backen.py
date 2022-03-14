from flask import Flask,redirect,render_template,request,session,abort

app = Flask(__name__)
@app.route('/',)
def my_form():
    return render_template('login.html')
@app.route('/login',methods =['POST','GET'])
def login():
    if request.method =='POST' and request.form['uname']=='admin' and request.form['pass']=='admin123':
        return  render_template('page2.html')

@app.route('/route/')
def route1():
    return render_template('page2.html')
@app.route('/route1/')
def route2():
    return render_template('signup.html')
@app.route('/route3/')
def route3():
    return render_template(('table.html'))

app.run()
