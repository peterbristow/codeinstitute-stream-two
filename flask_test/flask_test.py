from flask import Flask
from flask import render_template # Add this as the last import at the beginning of the file
app = Flask(__name__)


ages = {
    'bob': '43',
    'alice': '29'
}


@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    return render_template('users.html', user=user, age=age)


@app.route('/')
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
