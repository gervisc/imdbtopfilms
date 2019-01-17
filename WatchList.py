import csv
import numpy as np

def GetWatchListFeatures(maxreviews,Directors,Genres,DirectorDates,AllDi):
    #lees csv in
    with open('watchlist.csv','r') as f:
        moviesandtv = list(csv.reader(f,delimiter= ','))
    #filter op movies
    movies = [];
    for movie in moviesandtv:
        if movie[7] == 'movie':
            movies.append(movie)
    #vind directors

    #directors naar array
    NewDirector = np.ones(len(movies), dtype='datetime64[s]')
    MovieDirector = np.zeros((len(movies),len(Directors)));
    i=0
    for director in [di[14] for di in movies[0:]]:
        k=0
        for director2 in director.split(', '):
            if director2 in Directors:
                k+=1
        for director2 in director.split(', '):
            if director2 in Directors:
                MovieDirector[i,Directors.index(director2)] = 1/k

            if director2 in AllDi:
                NewDirector[i] = DirectorDates[AllDi.index(director2)]
        i+=1

    #genres naar array
    i=0
    MovieGenre = np.zeros((len(movies),len(Genres)));

    for genre in [di[11] for di in movies[0:]]:
        for genre2 in genre.split(', '):
            if genre2 in Genres:
                MovieGenre[i,Genres.index(genre2)] = 1/len(genre.split(', '))
        i+=1
    #x
    ratings=np.zeros(len(movies),dtype=float)
    i=0
    for r in [r[8] for r in movies[0:]]:
        if r == '':
            ratings[i] = 7.8
        else :
            ratings[i]= r
        i+=1
    #votes
    votes   =np.zeros(len(movies), dtype=float)
    i = 0
    for v in [v[12] for v in movies[0:]]:
        if v == '':
            votes[i] = 0
        else:
            votes[i] = v
        i += 1


    X1 = np.concatenate((ratings/10,(np.asarray([y[10] for y in movies[0:]],dtype=float)-1920)/100,votes/maxreviews))
    X =  np.concatenate((MovieDirector,MovieGenre,X1.reshape(3,len(movies)).T), axis=1)
    return X,NewDirector
