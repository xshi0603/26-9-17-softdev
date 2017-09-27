from flask import Flask, render_template
import csv, random 

#old code

jobs = {}

with open('occupations.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        jobs[row[0]] = float(row[1])

def randomJob (diction):
    first = 0
    second = 0
    counter = 0
    targetnum = random.uniform(0, 99.8)
    print(targetnum)
    for item in diction:
        if counter % 2 == 0:
            second = first + diction[item]
            if (targetnum > first and targetnum < second) :
                return item
        else:
            first = second + diction[item]
            if (targetnum < first and targetnum > second) :
                return item
        counter += 1
#new code

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('template.html', title = "root", i = "This is the root page. Other pages include occupations.")

@my_app.route('/occupations')
def occupations():
    return render_template('template.html', title = "Occupations", d = jobs, random_occ = randomJob(jobs))

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
