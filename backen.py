from flask import Flask,redirect,render_template,request,session,abort

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('page3.html')
@app.route('/route/')
def route1():
    return render_template('page2.html')

app.run()
