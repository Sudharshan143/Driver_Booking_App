from flask import Flask, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy users
users = {
    '9876543210': {'password': 'driver123', 'role': 'driver'},
    'user@example.com': {'password': 'cust123', 'role': 'customer'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']
        user = users.get(identifier)
        if user and user['password'] == password:
            session['user'] = identifier
            return f"Welcome, {user['role'].capitalize()}!"
        else:
            flash("Invalid credentials")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

