
import csv


from omdbget import omdbget

print(omdbget("tt3747978"))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))


#
#
#
# with open('omdb.csv','r')as f:
#     omdbmovies = list(csv.reader(f, delimiter=','))
#
#
# with open('watchlist.csv','r') as fin , open('omdb.csv','w') as omdb:
#
#     reader = csv.reader(fin)
#     all=[]
#     row = next(reader)
#     row.append('recommendation')
#     row.append('newdirector')
#     all.append(row)
#     k=0
#     for row in reader:
#         if row[7] == 'movie':
#             row.append('{:.2f}'.format(float(predictions[k]*10)))
#             row.append(NewDirector[k])
#             all.append(row)
#             k+=1
#
# return all