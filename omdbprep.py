import json
import csv


from omdbget import omdbget

def omdbprep(movies):
    # lees csv in
    with open('omdb.csv', 'r') as f:
        omdbmovies = list(csv.reader(f, delimiter=','))







    i=0
    with open('omdb.csv', 'a')as f:
        writer = csv.writer(f, lineterminator='\n')
        for n, movie in enumerate(movies):
            i+=1
            if i== 999:
                break
            for om in omdbmovies:
                if om[0] == movie[0]:
                    continue
            resp = omdbget(movie[0])
            item = resp.json()
            country = item["Country"]
            actors = item["Actors"]
            rated = item["Rated"]

            #awards
            awards = item["Awards"]
            winindex = awards.find("win")
            if(winindex>0):
                if(awards[max(winindex-5,0)] == " "):
                    wins = int(awards[max(winindex - 4, 0):winindex])
                else:
                    wins = int(awards[max(winindex-3,0):winindex])
            nominationindex = awards.find("nomination")
            if(nominationindex>0):
                if (awards[max(nominationindex - 5, 0)] == " ") and (awards[max(nominationindex - 3, 0)] != " "):
                    nominations = int(awards[max(nominationindex - 4, 0):nominationindex])
                else:
                    nominations = int(awards[max(nominationindex - 3, 0):nominationindex])

            movie.append(country)
            movie.append(actors)
            movie.append(rated)
            movie.append(wins)
            movie.append(nominations)
            movies[n]=movie
            writer.writerow(movie)
    return movies


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