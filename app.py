from flask import Flask, render_template #importing stuff
import csv, random 

#old code

jobs = {}

with open('occupations.csv', 'rb') as csvfile: #get file and make a dictionary
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        jobs[row[0]] = float(row[1])

def randomJob (diction): #get a random job
    first = 0 #range bottom
    second = 0 #range top
    counter = 0 #how many are u at
    targetnum = random.uniform(0, 99.8) #float between 0 and 99.8
    #print(targetnum)
    for item in diction:
        if counter % 2 == 0: #alternates w/ the other one
            second = first + diction[item]
            if (targetnum > first and targetnum < second) :
                return item #return if inbetween the ranges
        else:
            first = second + diction[item]
            if (targetnum < first and targetnum > second) :
                return item #return if inbetween the ranges
        counter += 1 #swap between the two
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
