
import csv

with open('omdb.csv','r')as f:
    omdbmovies = list(csv.reader(f, delimiter=','))


with open('watchlist.csv','r') as fin , open('omdb.csv','w') as omdb:

    reader = csv.reader(fin)
    all=[]
    row = next(reader)
    row.append('recommendation')
    row.append('newdirector')
    all.append(row)
    k=0
    for row in reader:
        if row[7] == 'movie':
            row.append('{:.2f}'.format(float(predictions[k]*10)))
            row.append(NewDirector[k])
            all.append(row)
            k+=1

with open('watchlistomdb.csv','w') as watchlistextended
    writer = csv.writer(watchlistextended, lineterminator='\n')
    writer.writerows(all)