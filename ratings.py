import csv
import numpy as np
from DefineFeature import DefineFeatureRating
from utils import GetColumn

def GetRatingsFeatures(movies):

    FeaturesColumnDirector = GetColumn(movies,12)

    MovieFeatureDirectors, ClippedFeaturesDirector=DefineFeatureRating(FeaturesColumnDirector, 5)
    print(ClippedFeaturesDirector)
    #latest rated date  of director
    NewDirector = {}

    for di in movies[0:]:
        director = di[12]
        daterated = np.datetime64(di[2])
        for director2 in director.split(', '):
            if director2 not in NewDirector or daterated > NewDirector[director2]:
                NewDirector[director2] = daterated

    FeaturesColumnGenre = GetColumn(movies, 9)

    MovieFeatureGenre, ClippedFeaturesGenre = DefineFeatureRating(FeaturesColumnGenre, 10)
    print(ClippedFeaturesGenre)
    FeaturesColumnCountry = GetColumn(movies, 13)

    MovieFeatureCountry, ClippedFeaturesCountry = DefineFeatureRating(FeaturesColumnCountry, 15)
    print(ClippedFeaturesCountry)

    FeaturesColumnActors = GetColumn(movies, 14)
    MovieFeatureActors, ClippedFeaturesActors = DefineFeatureRating(FeaturesColumnActors, 8)
    print(ClippedFeaturesActors)

    FeaturesColumnParentRating = GetColumn(movies, 15)
    MovieFeatureParentRating, ClippedFeaturesParentRating = DefineFeatureRating(FeaturesColumnParentRating, 8)
    print(ClippedFeaturesParentRating)

    #y
    Ratings = np.asarray([di[1] for di in movies[0:]],dtype=float)/10.0
    maxreviews = (np.max(np.asarray([v[10] for v in movies[0:]],dtype=float)))
    #x
    X1 = np.concatenate((np.asarray([r[16] for r in movies[0:]],dtype=float)/20-0.5,np.asarray([r[17] for r in movies[0:]],dtype=float)/100-0.5,np.asarray([r[6] for r in movies[0:]],dtype=float)/10-0.5,(np.asarray([y[8] for y in movies[0:]],dtype=float)-1920)/100-0.5,np.asarray([v[10] for v in movies[0:]],dtype=float)/maxreviews-0.5))
    X =  np.concatenate((MovieFeatureDirectors,MovieFeatureGenre,MovieFeatureCountry,MovieFeatureActors,MovieFeatureParentRating,X1.reshape(5,len(movies)).T), axis=1)
    #print(Countrys)
    Features = ClippedFeaturesDirector + ClippedFeaturesGenre + ClippedFeaturesCountry +ClippedFeaturesActors+ClippedFeaturesParentRating+ ['wins','nominations','ratings','year','views']
    return X,Ratings,maxreviews,ClippedFeaturesDirector,ClippedFeaturesGenre,ClippedFeaturesCountry,ClippedFeaturesActors,ClippedFeaturesParentRating,Features,NewDirector
