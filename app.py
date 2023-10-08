from flask import Flask

RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


if __name__ == '__main__':
    app.debug = True
    app.run()
