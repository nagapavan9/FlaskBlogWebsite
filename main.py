from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#protect cross browser attacks
#  import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = '667c3b63ea9f67b79ce202777d22a1f7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #Post will link to Post(), backref will fetch the author, lazy=True will let us push data at one go
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    #db.ForeignKey('user.id') will use user table, id column as the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"



posts = [
    {
        'author': 'Naga Pavan',
        'title': 'Blog Past 1',
        'content': 'first post content',
        'date_posted': 'April 03, 2023'
    },
    {
        'author': 'KTS Srinivas',
        'title': 'Blog Past 2',
        'content': 'second post content',
        'date_posted': 'April 04, 2023'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html', posts=posts)

#This will route the About page
@app.route("/about")
def about():
    return render_template('About.html',title = 'About')

#This will route the Registration page
@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#This will route the Login page
@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You Have Been Logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please Check Username And Password', 'danger')
    return render_template('login.html', title='Login', form=form)

#To run the application in debug mode
if __name__=='__main__':
    app.run(debug=True)
