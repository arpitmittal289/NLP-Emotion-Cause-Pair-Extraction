import json
import csv

data = None
with open('C:\\Users\\wyatt\\source\\repos\\emotioncausepair\\source\\data\\Electronics_split1.json') as json_file:
    data = json.load(json_file)

data_file = open('C:\\Users\\wyatt\\source\\repos\\emotioncausepair\\source\\data\\Electronics_split1.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)

for d in data:
    if 'reviewText' in d:
        csv_writer.writerow([d['overall'],d['reviewText']])

data_file.close()