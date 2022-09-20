from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    message = TextAreaField('message', validators=[DataRequired()])
    send = SubmitField('send')















app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/signIn")
def signIn():
    return render_template("signIn.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")



if __name__ == "__main__":
    app.run(debug=True)
