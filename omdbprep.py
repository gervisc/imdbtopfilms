import json
import csv


from omdbget import omdbget

def omdbprep(movies,stora,positionkey):
    # lees csv in
    with open(stora, 'r') as f:
        omdbmovies = list(csv.reader(f, delimiter=','))







    i=0
    with open(stora, 'a')as f:
        writer = csv.writer(f, lineterminator='\n')
        for n, movie in enumerate(movies):
            k=0
            for om in omdbmovies:
                if om[positionkey] == movie[positionkey]:
                    movies[n] = om
                    k=1
            if k==1:
                continue
            resp = omdbget(movie[positionkey])
            item = resp.json()
            if item["Response"] == "True" :
                country = item["Country"]
                actors = item["Actors"]
                rated = item["Rated"]
                wins =0
                nominations =0
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
                movie.append(rated.lower())
                movie.append(wins)
                movie.append(nominations)
                movies[n]=movie
                writer.writerow(movie)
            else:
                movie.append("Unknown")
                movie.append("")
                movie.append("Not Rated".lower())
                movie.append(0)
                movie.append(0)
                movies[n] = movie
    return movies


