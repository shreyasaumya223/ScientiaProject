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

if __name__ == '__main__':  
    app.run()