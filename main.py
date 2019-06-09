import csv
from keras.models import Sequential
from keras.layers import Dense
from ratings import GetRatingsFeatures
from WatchList import GetWatchListFeatures
from omdbprep import omdbprep
from keras import initializers
import numpy as np
from utils import GetColumn


#lees csv in
with open('storage/ratings.csv','r') as f:
    moviesandtv = list(csv.reader(f,delimiter= ','))

#filter op movies
movies = [];
for movie in moviesandtv:
   if movie[5] == 'movie':
       movies.append(movie)

#test data#

movies = omdbprep(movies,'storage/omdb.csv',0)



X,Ratings,maxreviews,Directors,Genres,Countrys,Actors,ParentRatings,Features,DiDates = GetRatingsFeatures(movies)

Xw,NewDirector,movies = GetWatchListFeatures(maxreviews,Directors,Genres,Countrys,Actors,ParentRatings,DiDates)




#create model
model = Sequential()
model.add(Dense(1,kernel_initializer=initializers.RandomUniform(minval=-0.01, maxval=1, seed=None), activation='relu', input_dim=X.shape[1]))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



# Fit the model

model.fit(X, Ratings, epochs=50, batch_size=1)



#model.fit(X, Ratings, validation_split=0.33, epochs=50, batch_size=1)
predictions = model.predict(Xw)

countrys=GetColumn(movies, 17)
actors=GetColumn(movies, 18)
parentratings=GetColumn(movies, 19)
wins =GetColumn(movies, 20)
nominations = GetColumn(movies, 21)

with open('storage/watchlist.csv','r') as fin ,open('watchlistratings.csv','w') as fout:
    writer = csv.writer(fout, lineterminator='\n')
    reader = csv.reader(fin)
    all=[]
    row = next(reader)
    row.append('recommendation')
    row.append('newdirector')
    row.append('Country')
    row.append('actor')
    row.append('rated')
    row.append('wins')
    row.append('nominations')
    all.append(row)
    k=0
    for row in reader:
        if row[7] == 'movie':
            row.append('{:.2f}'.format(float(predictions[k]*10)))
            row.append(NewDirector[k])
            row.append(countrys[k])
            row.append(actors[k])
            row.append(parentratings[k])
            row.append(wins[k])
            row.append(nominations[k])
            all.append(row)
            k+=1
    writer.writerows(all)

