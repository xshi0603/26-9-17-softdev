from flask import Flask, render_template

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "This is the root page. Other pages include one and two."

@my_app.route('/occupations')
def occupations():
    return render_template('template.html', c = "hello")

if __name__ == '__main__':
    my_app.debug = true
    my_app.run()
