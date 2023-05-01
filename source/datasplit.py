import os
import json

#you need to add you path here
with open(os.path.join('C:\\Users\\wyatt\\source\\repos\\emotioncausepair\\source\\data', 'Electronics.json'), 'r',
          encoding='utf-8') as f1:
    ll = []
    for i in range(100000):
        line = f1.readline()
        ll.append(json.loads(line.strip()))

    #ll = [json.loads(line.strip()) for line in f1.readlines()]


    size_of_the_split=100000
    total = len(ll) // size_of_the_split

    #in here you will get the Number of splits
    print(total+1)

    for i in range(total+1):
        json.dump(ll[i * size_of_the_split:(i + 1) * size_of_the_split], open(
            "C:\\Users\\wyatt\\source\\repos\\emotioncausepair\\source\\data\\Electronics_split" + str(i+1) + ".json", 'w',
            encoding='utf8'), ensure_ascii=False, indent=True)