from flask import Flask, redirect, render_template, request, session, abort
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="///Tharik321", database="wallet")
cursor = db.cursor()

app = Flask(__name__)


@app.route('/', )
def my_form():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['uname']
    global username
    password = request.form['pass']
    cursor.execute("SELECT * FROM users WHERE name='" + username + "' AND password=" + password + "")
    data = cursor.fetchone()
    if data is None:

        return render_template('login.html')
    else:
        return render_template('page2.html')


@app.route('/start', methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
        amount = request.form['amount']
        amount_ch=int(amount)
        cursor.execute("SELECT balance FROM users WHERE name='" + username + "'")
        balance = cursor.fetchone()
        balance_ch=int(balance[0])
        c=balance_ch-amount_ch
        trans_method = request.form['transaction']
        trans_method_ch=str(trans_method)
        debit = "debit"
        credit = "credit"
        if c<0 and trans_method_ch == debit:

            return render_template('page3.html')
        else:
            if trans_method_ch == debit:
                cursor.execute("SELECT balance FROM users WHERE name='" + username + "'")
                balance = cursor.fetchone()
                balance_ch = int(balance[0])
                after= balance_ch - amount_ch
                after_ch=str(after)
                cursor.execute("UPDATE users SET balance='" + after_ch + "' WHERE name='" + username + "'")
                db.commit()
                return render_template('page4.html')
            else:
                cursor.execute("SELECT balance FROM users WHERE name='" + username + "'")
                balance = cursor.fetchone()
                balance_ch = int(balance[0])
                after = balance_ch + amount_ch
                after_ch = str(after)
                cursor.execute("UPDATE users SET balance='" + after_ch + "' WHERE name='" + username + "'")
                db.commit()


                return render_template('page4.html')









@app.route('/route/')
def route1():
    return render_template('page2.html')


@app.route('/route1/')
def route2():
    return render_template('signup.html')


@app.route('/route3/')
def route3():
    return render_template(('table.html'))


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        details = request.form
        name = details['usern']
        password = details['passw']
        walletid = details['wallid']
        balance = details['balance']

        cursor.execute("INSERT INTO users (name,password,walletid,balance) VALUES(%s,%s,%s,%s)",
                       [name, password, walletid, balance])

        db.commit()
        return render_template('page2.html')


app.run()
cursor.close()
