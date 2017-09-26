from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "This is the root page. Other pages include one and two."

@my_app.route('/one')
def one():
    return "This is page one. Other pages include root and two."

@my_app.route('/two')
def two():
    return "This is page two. Other pages include root and one."

if __name__ == '__main__':
    #my_app.debug = true
my_app.run()
