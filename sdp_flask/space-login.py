import flask
from pymongo import MongoClient


dum = flask.Flask(__name__)


@dum.route("/")
def login_page():
    return flask.render_template("space_mngmnt_login.html")


@dum.route("/n", methods=['POST'])
def verify():
    u_id = flask.request.form['userid']
    passw = flask.request.form['password']
    if u_id == 'harsha_007' and passw == 'saiharsha@19':
        return "<h1><center>Welcome %s </center><h1>" % u_id
    else:
        return "wrong credentials"


@dum.route("/r")
def new_user():
    return flask.render_template("register_now.html")


@dum.route("/nweuser", methods=['POST'])
def register():
    new_client = MongoClient('mongodb://localhost:27017/')
    print(new_client)

    entered_fname = flask.request.form.get("fname")
    entered_pass = flask.request.form.get("password")
    entered_lname = flask.request.form.get("lname")
    entered_mobile = flask.request.form.get("mobile")
    entered_email = flask.request.form.get("email-id")
    db = new_client['SpaceManagement']
    info = db.flask
    user = {"first_name": entered_fname, "last_name": entered_lname}
    userdata = db.flask
    userdata.insert_one(user)
    return "User Registered Successfully"


# Creating database


# Creating document

# Inserting data

if __name__ == '__main__':
    dum.run(debug=True)