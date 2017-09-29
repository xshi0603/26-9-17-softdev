from flask import Flask, render_template #importing stuff
import csv, random
from utils import occs 

jobs = occs.createDict() 

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('template.html', title = "root", i = "This is the root page. Other pages include occupations.")

@my_app.route('/occupations')
def occupations():
    return render_template('template.html', title = "Occupations", d = jobs, random_occ = occs.randomJob(jobs))

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
