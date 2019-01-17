import csv
import numpy as np

def GetRatingsFeatures(movies):


    #vind directors
    Directors = [];
    Directors2 = []
    for director in [di[12] for di in movies[0:]]:
        for director2 in director.split(', '):
            if director2 not in Directors:
                Directors.append(director2)
            elif director2 not in Directors2:
                Directors2.append(director2)
    #directors naar array
    NewDirector = np.zeros(len(Directors), dtype='datetime64[s]')
    MovieDirector = np.zeros((len(movies),len(Directors2)));
    i=0
    for di in movies[0:]:
        director = di[12]
        daterated = np.datetime64(di[2])
        k=0
        for director2 in director.split(', '):
            if director2 in Directors2:
                k+=1
        for director2 in director.split(', '):
            if director2 in Directors2:
                MovieDirector[i,Directors2.index(director2)] = 1/k
            if daterated > NewDirector[Directors.index(director2)]:
                NewDirector[Directors.index(director2)] = daterated

        i+=1

    #vind genres
    Genres = [];
    for genre in [di[9] for di in movies[0:]]:
        for genre2 in genre.split(', '):
            if genre2 not in Genres:
                Genres.append(genre2)
    #genres naar array
    i=0
    MovieGenre = np.zeros((len(movies),len(Genres)));

    for genre in [di[9] for di in movies[0:]]:
        for genre2 in genre.split(', '):
            MovieGenre[i,Genres.index(genre2)] = 1/len(genre.split(', '))
        i+=1
    #y
    Ratings = np.asarray([di[1] for di in movies[0:]],dtype=float)/10.0
    maxreviews = (np.max(np.asarray([v[10] for v in movies[0:]],dtype=float)))
    #x
    X1 = np.concatenate((np.asarray([r[6] for r in movies[0:]],dtype=float)/10,(np.asarray([y[8] for y in movies[0:]],dtype=float)-1920)/100,np.asarray([v[10] for v in movies[0:]],dtype=float)/maxreviews))
    X =  np.concatenate((MovieDirector,MovieGenre,X1.reshape(3,len(movies)).T), axis=1)
    Features = Directors2 + Genres + ['ratings','year','views']
    return X,Ratings,maxreviews,Directors2,Genres,Features,NewDirector,Directors
