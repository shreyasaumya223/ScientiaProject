from flask import Flask, render_template, request, redirect
from tables import Results
from flask_mysqldb import MySQL
#from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12303597'
app.config['MYSQL_PASSWORD'] = 'mX6QHPamhm'
app.config['MYSQL_DB'] = 'sql12303597'

mysql = MySQL(app)

#to list all employees
@app.route('/', methods=['GET', 'POST'])
def userlist():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Employee")
        rows = cur.fetchall()
        messages = rows
        print('Total Row(s):', cur.rowcount)
        for row in rows:
            print(row)
        table = Results(rows)
        table.border = True
        cur.close()
        return render_template('users.html', table=table)

#to add employee
@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        details = request.form
        vName = details['name']
        vDesignation = details['desig']
        vAddress = details['addr']
        vPhone = details['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Employee(Name, Designation, Address, Phone) VALUES (%s, %s, %s, %s)", (vName,vDesignation,vAddress,vPhone))
        mysql.connection.commit()
        cur.close()
        return 'successfully added for ' + vName + ' ' + vDesignation + ' ' + vAddress + ' ' + vPhone
    return render_template('index.html')
      
#to delete employee
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        vName = details['name']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Employee WHERE Name=%s", [vName])
        mysql.connection.commit()
        cur.close()
        return 'successfully deleted record for' + vName
    return render_template('index.html')

#to search an employee based on name
@app.route('/')
def search_view_name():
    if request.method == "POST":
        details = request.form
        user_name = details['name']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Employee WHERE name=%s", user_name)
        row = cur.fetchone()
        print('Total Row(s):', cur.rowcount)
        cur.close()
        for row in rows:
            print(row)
        if row:
            return render_template('users.html', row=row)
        else:
            return 'Error loading #{user_name}'.format(user_name=user_name)
    return render_template('index.html')

#to search an employee based on designation
@app.route('/')
def search_view_desi():
    if request.method == "POST":
        details = request.form
        user_designation = details['designation']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Employee WHERE designation=%s", user_designation)
        row = cur.fetchone()
        print('Total Row(s):', cur.rowcount)
        cur.close()
        for row in rows:
            print(row)
        if row:
            return render_template('users.html', row=row)
        else:
            return 'Error loading #{user_designation}'.format(user_designation=user_designation)
    return render_template('index.html')

#to search an employee based on phone
@app.route('/')
def search_view_phone():
    if request.method == "POST":
        details = request.form
        user_phone = details['phone']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Employee WHERE phone=%s", user_phone)
        row = cur.fetchone()
        print('Total Row(s):', cur.rowcount)
        cur.close()
        for row in rows:
            print(row)
        if row:
            return render_template('users.html', row=row)
        else:
            return 'Error loading #{user_phone}'.format(user_phone=user_phone)
    return render_template('index.html')

if __name__ == '__main__':  
    app.run()