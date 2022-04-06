from flask import Flask, render_template, request
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("Employee.db", check_same_thread=False)

listoftables = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'MYEMPLOYEE'").fetchall()

if listoftables != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE MYEMPLOYEE(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODE TEXT,
    NAME TEXT,
    AGE INTEGER,
    ADDRESS TEXT,
    EMAIL TEXT,
    DESIG TEXT,
    SALARY TEXT,
    COM_NAME TEXT
    
    )''')
    print("Table Created Successfully")

App = Flask(__name__)


@App.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        getCode = request.form["code"]
        getName = request.form["name"]
        getAge = request.form["age"]
        getAddress = request.form["add"]
        getEmail = request.form["email"]
        getDesig = request.form["desig"]
        getSalary = request.form["sal"]
        getCname = request.form["cname"]
        print(getCode)
        print(getName)
        print(getAge)
        print(getAddress)
        print(getEmail)
        print(getDesig)
        print(getSalary)
        print(getCname)

        connection.execute("INSERT INTO MYEMPLOYEE(CODE, NAME, AGE, ADDRESS, EMAIL, DESIG, SALARY, COM_NAME) \
        VALUES('"+getCode+"', '"+getName+"', "+getAge+", '"+getAddress+"', '"+getEmail+"', '"+getDesig+"', \
        '"+getSalary+"', '"+getCname+"')")
        connection.commit()
        print("Inserted Successfully")

        return redirect('/viewemp')

    return render_template("home.html")

@App.route("/search", methods=['GET', 'POST'])
def search():
    cursor = connection.cursor()
    if request.method == "POST":
        getCode1 = request.form["code"]

        count = cursor.execute("SELECT * FROM MYEMPLOYEE WHERE CODE ="+request.form["code"])
    result1 = cursor.fetchall()
    return render_template("search.html", employee=result1)

@App.route("/update", methods=['GET', 'POST'])
def update():
    global getCode1
    if request.method == "POST":
        getCode1 = request.form["code"]

        return redirect('/upd')


    return render_template("update.html")


@App.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        getCode = request.form["code"]
        connection.execute("DELETE FROM MYEMPLOYEE WHERE CODE=" + getCode)
        connection.commit()
        return redirect('/viewemp')
    print("Deleted Successfully")
    return render_template("delete.html")


@App.route("/viewemp")
def viewAll():
    cursor = connection.cursor()
    count = cursor.execute("SELECT * FROM MYEMPLOYEE")

    result = cursor.fetchall()
    return render_template("viewall.html", employee=result)


@App.route("/upd", methods=['GET', 'POST'])
def updation():
    if request.method == "POST":
        getNCode = request.form["code"]
        getNName = request.form["name"]
        getNAge = request.form["age"]
        getNAddress = request.form["add"]
        getNEmail = request.form["email"]
        getNDesig = request.form["desig"]
        getNSalary = request.form["sal"]
        getNCname = request.form["cname"]

        print(getNCode)
        print(getNName)
        print(getNAge)
        print(getNAddress)
        print(getNEmail)
        print(getNDesig)
        print(getNSalary)
        print(getNCname)
        connection.execute("UPDATE MYEMPLOYEE SET CODE='" +getNCode+"', NAME='" +getNName+"', \
        AGE=" +getNAge+", ADDRESS='" +getNAddress+"', EMAIL='" +getNEmail+"', DESIG='" +getNDesig+"', \
        SALARY='" +getNSalary+"', COM_NAME='" +getNCname+"' WHERE CODE='"+getCode1+"'")
        connection.commit()
        print("Updated Successfully")

        return redirect('/viewemp')

    return render_template("updation.html")

if __name__ == "__main__":
    App.run()