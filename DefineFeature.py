import numpy as np
from collections import Counter

def DefineFeatureRating(FeaturesColumn,minimumOccurence):


    #get a list of all features
    Features= [];
    for Row in FeaturesColumn:
        for feature in Row.split(', '):
            Features.append(feature)
    #occurence of each feature
    FeaturesOcc = Counter(Features)

    #filter list, only items that appear more than minimumoccurencee
    ClippedFeatures = []
    for key, value in FeaturesOcc.items():
        if value >= minimumOccurence:
                ClippedFeatures.append(key)



    MovieFeature = np.zeros((len(FeaturesColumn),len(ClippedFeatures)));
    i=0
    for row in FeaturesColumn:
        k=0
        for feature in row.split(', '):
            if feature in ClippedFeatures:
                k+=1
        for feature in row.split(', '):
            if feature in ClippedFeatures:
                MovieFeature[i,ClippedFeatures.index(feature)] = 1/k


        i+=1

    return MovieFeature,ClippedFeatures


def DefineFeatureWatchlist(FeaturesColumn,FeaturesReference,nmovies):

    MovieDirector = np.zeros((nmovies,len(FeaturesReference)))
    i=0
    for director in FeaturesColumn:
        k=0
        for director2 in director.split(', '):
            if director2 in FeaturesReference:
                k+=1
        for director2 in director.split(', '):
            if director2 in FeaturesReference:
                MovieDirector[i,FeaturesReference.index(director2)] = 1/k
        i+=1
    return MovieDirector

