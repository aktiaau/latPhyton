from flask import Flask, render_template, request
import sqlite3 as sql

app=Flask(__name__) #membuat class atau object
con=sql.connect("database.db")
print("Opened database successfully")

con.execute('create table if not exists students (name TEXT, address TEXT, city TEXT, pin TEXT)')
print("Table created successfully")
con.close()

@app.route('/')
def home():
    return render_template('indexsql.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method=='POST':
        try:
            nm=request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect("database.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO students (name,address,city,pin) VALUES (?,?,?,?)", (nm,addr,city,pin))
                con.commit()
                msg="Record successfully added"
        except:
            con.rollback()
            msg="Error in insert operation"
        finally:
            return render_template("result.html", msg=msg)

@app.route('/list')
def list():
    try:
        con=sql.connect("database.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        con.close()
        return render_template("list.html", rows=rows)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__=='__main__':#menjalankan program
    app.run()