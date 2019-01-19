import json
import csv


from omdbget import omdbget

def omdbprep(movies):
    i=0
    for movie in movies:
        i+=1
        if i== 10:
            break
        resp = omdbget(movie[0])
        item = resp.json()
        country = item["Country"]
        print(country)
        awards = item["Awards"]
        oscarindex = awards.find("Oscar")
        if(oscarindex>0):
            oscar = int(awards[max(oscarindex-3,0):oscarindex])
            print(oscar)
        winindex = awards.find("win")
        if(winindex>0):
            if(awards[max(winindex-5,0)] == " "):
                wins = int(awards[max(winindex - 4, 0):winindex])
            else:
                wins = int(awards[max(winindex-3,0):winindex])
            print(wins)
        nominationindex = awards.find("nomination")
        if(nominationindex>0):
            if (awards[max(nominationindex - 5, 0)] == " "):
                nominations = int(awards[max(nominationindex - 4, 0):nominationindex])
            else:
                nominations = int(awards[max(nominationindex - 3, 0):nominationindex])
            print(nominations)
        print(awards)
        actors = item["Actors"]
        print(actors)
        rated = item["Rated"]
        print(rated)



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