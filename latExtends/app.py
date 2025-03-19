from flask import Flask, flash, session, render_template, redirect, url_for, request

app=Flask(__name__) #membuat class atau object
app.secret_key='any random string'

@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        return render_template('index.html', username=username)

    return 'You are not logged in <br> <a href="/login">Click here to log in</a>'
    #return render_template('index.html', username=None)

@app.route('/utama')
def utama():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/respon')
def respon():
    return render_template('respon.html')

@app.route('/success/<name>')
def success(name):
    return "Welcome {}" .format(name)

@app.route('/input', methods=["POST","GET"])
def input():
    if request.method == "POST":
        user = request.form["uname"]
        return redirect(url_for("success", name=user))
    else:
        user=request.args.get("uname")
        return render_template('input.html')

@app.route('/result', methods=["POST","GET"])
def result():
    if request.method=="POST":
        result=request.form
        return render_template('result.html', result=result)

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        session['username'] = request.form["uname"]
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Anda telah logout.", "info")
    return redirect(url_for('index'))

if __name__=='__main__':#menjalankan program
    app.run(debug=True)