# This is the Login and Register page for Transport Management System "Transport4U"


from flask import Flask, request, json, session
from flask import render_template
from werkzeug.utils import redirect

app = Flask(__name__)
app.debug = True



@app.route("/")
def home():
    if not session.get("username"):
        return redirect("/signin")
    return render_template('index.html')

@app.route("/signin", methods=['GET','POST'])
def signin():
    #username = request.form['username']
    #password = request.form['password']
    #if username and password:
       # return json.dumps({'validation': validateUser(username, password)})
    #return json.dumps({'validation': False})
    return render_template('signin.html')

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template('register.html')


def validateUser(username, password, confirmPassword):
    return True


if __name__ == '__main__':
    app.run()