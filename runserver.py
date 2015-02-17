# coding=utf8



from flask import Flask, g
from views import index_page

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

app.register_blueprint(index_page)

if __name__ == '__main__':
    app.run(debug=True)
