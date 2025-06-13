from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')

# Route for login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for profile page
@app.route('/profile')
def profile():
    return "profile.html"


if __name__ == '__main__':
    app.run(debug=True)