import csv
import numpy as np

def GetTestFeatures(movies,maxreviews,Directors,Genres):



    #directors naar array
    MovieDirector = np.zeros((len(movies),len(Directors)));
    i=0
    for director in [di[12] for di in movies[0:]]:
        for director2 in director.split(', '):
            k=0
            if director2 in Directors:
                k+=1
            if director2 in Directors:
                MovieDirector[i,Directors.index(director2)] = 1/k
        i+=1

    #genres naar array
    i=0
    MovieGenre = np.zeros((len(movies),len(Genres)));

    for genre in [di[9] for di in movies[0:]]:
        for genre2 in genre.split(', '):
            if genre2 in Genres:
                MovieGenre[i,Genres.index(genre2)] = 1/len(genre.split(', '))
        i+=1
    #x
    ratings=np.zeros(len(movies),dtype=float)
    i=0
    for r in [r[1] for r in movies[0:]]:
        if r == '':
            ratings[i] = 7.8
        else :
            ratings[i]= r
        i+=1
    #votes
    votes   =np.zeros(len(movies), dtype=float)
    i = 0
    for v in [v[10] for v in movies[0:]]:
        if v == '':
            votes[i] = 0
        else:
            votes[i] = v
        i += 1

    X1 = np.concatenate((ratings/10,(np.asarray([y[8] for y in movies[0:]],dtype=float)-1920)/100,votes/maxreviews))
    X =  np.concatenate((MovieDirector,MovieGenre,X1.reshape(3,len(movies)).T), axis=1)
    return X
