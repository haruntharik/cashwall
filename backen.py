from flask import Flask,redirect,render_template,request,session,abort

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('login.html')
app.run()
