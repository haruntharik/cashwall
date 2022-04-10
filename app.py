from flask import Flask, redirect, render_template, request, session, abort
from sqlalchemy import MetaData,create_engine,Table,Column,Integer,String,select
from datetime import datetime

meta_data= MetaData()
app = Flask(__name__)

db_connection="postgresql://ecwwvulyvbibsm:2737c91e60320a8599b9f8a910fb13334b0bb9caf6f290a99c5a66b9376ab879@ec2-34-207-12-160.compute-1.amazonaws.com:5432/d4m54k1v5ld5cb"

users = Table('users',meta_data,
              Column('name',String(80)),
              Column('walletid',String(80)),
              Column('password',String(80)),
              Column('balance',Integer()),
              )


engine = create_engine(db_connection)
conn = engine.connect()


@app.route('/',)
def my_form():
    return render_template('login.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    global username
    username = request.form['uname']
    
    password= request.form['pass']

    #result =select(users).where(users.name==username,users.password==password)
    #data=conn.execute(result)
    result=conn.execute("SELECT * FROM users WHERE name='" + username + "' AND password='" + password + "'")
    data =result.fetchone()




    if data is None:

        return render_template('login.html')
    else:
        return render_template('page2.html')






@app.route('/start', methods=['POST', 'GET'])


def start():
    #cursor=db.cursor(buffered=True)
    result=conn.execute("SELECT walletid FROM users WHERE name='" + username + "'")

    wallid = result.fetchone()[0]



    date = None
    date = datetime.today()
    time = None
    time = datetime.now()




    if request.method == 'POST':
        #cursor = db.cursor(buffered=True)


        amount = request.form['amount']
        amount_ch = float(amount)
        format(amount_ch, '.4f')

        result= conn.execute("SELECT balance FROM users WHERE name='" + username + "'")
        balance = result.fetchone()[0]
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
                result=conn.execute("SELECT balance FROM users WHERE name='" + username + "'")
                balance = result.fetchone()[0]
                balance_ch = float(balance or 0)
                format(balance_ch, '.4f')
                after= balance_ch - amount_ch
                format(after, '.4f')
                after_ch=str(after)
                conn.execute("UPDATE users SET balance='" + after_ch + "' WHERE name='" + username + "'")


                conn.execute("INSERT INTO transde (walletid,data,time,transactionmode,amount,balance)VALUES(%s,%s,%s,%s,%s,%s)",
                       [wallid, date, time, debit,amount_ch,after_ch])

                return render_template('page4.html')
            else:
                result=conn.execute("SELECT balance FROM users WHERE name='" + username + "'")
                balance = result.fetchone()[0]
                balance_ch = float(balance or 0)
                after = balance_ch + amount_ch
                format(after, '.4f' )
                after_ch = str(after)
                conn.execute("UPDATE users SET balance='" + after_ch + "' WHERE name='" + username + "'")


                conn.execute("INSERT INTO transde (walletid,data,time,transactionmode,amount,balance)VALUES(%s,%s,%s,%s,%s,%s)",
                    [wallid, date, time, credit,amount_ch, after_ch])



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
       # cursor = db.cursor(buffered=True)
        result=conn.execute("SELECT walletid FROM users WHERE name='" + username + "'")

        wallid = result.fetchone()[0]
        conn.execute("SELECT * FROM transde WHERE walletid='" + wallid + "'")



    #cursor = db.cursor(buffered=True)
    result=conn.execute("SELECT walletid FROM users WHERE name='" + username + "'")

    wallid = result.fetchone()[0]


    result=conn.execute("SELECT * FROM transde WHERE walletid='" + wallid +"'")
    headings = ("walletid", "Date", "Time", "Transaction mode", "Amount", "current balance")
    data = result.fetchall()
    return render_template('table.html', headings=headings, data=data)









@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        details = request.form
        name = details['usern']
        password = details['passw']
        walletid = details['wallid']
        balance = details['balance']

        conn.execute(users.insert(), name=name,password=password,walletid=walletid,balance=balance)




        return "You were successully created new account goback to login again"





