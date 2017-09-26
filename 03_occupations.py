import csv, random 

jobs = {}


with open('occupations.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        jobs[row[0]] = float(row[1])
     
#print(jobs)


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

print(randomJob(jobs))

#print(jobs)
