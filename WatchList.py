import csv
import numpy as np
from omdbprep import omdbprep
from DefineFeature import DefineFeatureWatchlist
from utils import GetColumn

def GetWatchListFeatures(maxreviews,Directors,Genres,Countrys,Actors,ParentRatings,DirectorDates):
    #lees csv in
    with open('storage/watchlist.csv','r') as f:
        moviesandtv = list(csv.reader(f,delimiter= ','))
    #filter op movies
    movies = [];
    for movie in moviesandtv:
        if movie[7] == 'movie':
            movies.append(movie)
    #vind directors

    movies = omdbprep(movies, 'storage/omdbwatch.csv',1)

    FeaturesColumnDirector = GetColumn(movies, 14)
    MovieDirector=DefineFeatureWatchlist(FeaturesColumnDirector, Directors, len(movies))

    #directors naar array
    NewDirector = np.ones(len(movies), dtype='datetime64[s]')
    i=0
    for director in FeaturesColumnDirector:
        for director2 in director.split(', '):
           if director2 in DirectorDates:
                NewDirector[i] = DirectorDates[director2]
        i+=1

    #genres naar array
    MovieGenre = DefineFeatureWatchlist(GetColumn(movies, 11), Genres, len(movies))

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

    # directors naar array
    MovieCountry = DefineFeatureWatchlist(GetColumn(movies, 17), Countrys, len(movies))


    MovieActor = DefineFeatureWatchlist(GetColumn(movies, 18), Actors, len(movies))


    MovieParentRating = DefineFeatureWatchlist(GetColumn(movies, 19), ParentRatings, len(movies))



    X1 = np.concatenate((np.asarray([r[20] for r in movies[0:]],dtype=float)/20,np.asarray([r[21] for r in movies[0:]],dtype=float)/100,ratings/10,(np.asarray([y[10] for y in movies[0:]],dtype=float)-1920)/100,votes/maxreviews))
    X =  np.concatenate((MovieDirector,MovieGenre,MovieCountry,MovieActor,MovieParentRating,X1.reshape(5,len(movies)).T), axis=1)
    #print(MovieCountry)
    return X,NewDirector,movies
