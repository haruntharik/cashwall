from flask import Flask, redirect, render_template, request, session, abort
import mysql.connector
from datetime import datetime
import pandas as pd

db = mysql.connector.connect(host="localhost", user="root", passwd="///Tharik321", database="wallet")
cursor = db.cursor()

app = Flask(__name__)


@app.route('/',)
def my_form():
    return render_template('login.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['uname']
    global username
    password = request.form['pass']

    cursor.execute("SELECT * FROM users WHERE name='" + username + "' AND password='" + password + "'")
    data = cursor.fetchone()
    if data is None:

        return render_template('login.html')
    else:
        return render_template('page2.html')


@app.route('/start', methods=['POST', 'GET'])






def start():
    cursor=db.cursor(buffered=True)
    cursor.execute("SELECT walletid FROM users WHERE name='" + username + "'")

    wallid = cursor.fetchone()[0]



    date = None
    date = datetime.today()
    time = None
    time = datetime.now()




    if request.method == 'POST':
        cursor = db.cursor(buffered=True)


        amount = request.form['amount']
        amount_ch = float(amount)
        format(amount_ch, '.4f')

        cursor.execute("SELECT balance FROM users WHERE name='" + username + "'")
        balance = cursor.fetchone()[0]
        balance_ch=float(balance or 0)


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
                balance = cursor.fetchone()[0]
                balance_ch = float(balance or 0)
                format(balance_ch, '.4f')
                after= balance_ch - amount_ch
                format(after, '.4f')
                after_ch=str(after)
                cursor.execute("UPDATE users SET balance='" + after_ch + "' WHERE name='" + username + "'")
                db.commit()

                cursor.execute("INSERT INTO transde (walletid,data,time,transactionmode,amount,balance)VALUES(%s,%s,%s,%s,%s,%s)",
                       [wallid, date, time, debit,amount_ch,after_ch])
                db.commit()
                return render_template('page4.html')
            else:
                cursor.execute("SELECT balance FROM users WHERE name='" + username + "'")
                balance = cursor.fetchone()[0]
                balance_ch = float(balance or 0)
                after = balance_ch + amount_ch
                format(after, '.4f' )
                after_ch = str(after)
                cursor.execute("UPDATE users SET balance='" + after_ch + "' WHERE name='" + username + "'")
                db.commit()

                cursor.execute("INSERT INTO transde (walletid,data,time,transactionmode,amount,balance)VALUES(%s,%s,%s,%s,%s,%s)",
                    [wallid, date, time, credit,amount_ch, after_ch])
                db.commit()


                return render_template('page4.html')



@app.route('/route/')
def route1():
    return render_template('page2.html')



@app.route('/route1/')
def route2():
    return render_template('signup.html')


@app.route('/route3/',methods=['POST','GET'])
def route3():
    if request.method == 'POST':
        cursor = db.cursor(buffered=True)
        cursor.execute("SELECT walletid FROM users WHERE name='" + username + "'")

        wallid = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM transde WHERE walletid='" + wallid + "'")

        data = cursor.fetchall()
        df = pd.read_sql(data)

        df.to_csv(r'C:\Users\my\Downloads\exported_data.csv')

    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT walletid FROM users WHERE name='" + username + "'")

    wallid = cursor.fetchone()[0]


    cursor.execute("SELECT * FROM transde WHERE walletid='" + wallid +"'")
    headings = ("walletid", "Date", "Time", "Transaction mode", "Amount", "current balance")
    data = cursor.fetchall()
    return render_template('table.html', headings=headings, data=data)









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
        return "You were successully created new account goback to login again"


app.run()
cursor.close()
