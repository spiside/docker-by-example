from flask import Flask
import psycopg2


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/users')
def users():
    conn = psycopg2.connect('postgres://postgres:postgres@db:5432')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    return "\n".join("<p><b>Email</b>: {}\t<b>Name</b>: {}</p>".format(user[0], user[1]) for user in users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
