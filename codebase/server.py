
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm















app = Flask(__name__)

app.config['SECRET_KEY']  = 
# Route for handling the login page logic
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = "default.jpg")
    password = db.Column(db.String(60),  nullable = False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")



@app.route("/signIn", methods = ["GET", "POST"])
def signIn():
    form  = LoginForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("signIn.html", title= "Login", form = form)


@app.route("/signup", methods = ["GET", 'POST'])
def signup():
    form  = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("signup.html", title= "Register", form = form)







if __name__ == "__main__":
    app.run(debug=True)
