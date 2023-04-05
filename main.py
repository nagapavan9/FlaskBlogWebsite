from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#protect cross browser attacks
#  import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = '667c3b63ea9f67b79ce202777d22a1f7'

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
