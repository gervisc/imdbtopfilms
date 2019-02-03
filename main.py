import csv
from keras.models import Sequential
from keras.layers import Dense
from ratings import GetRatingsFeatures
from WatchList import GetWatchListFeatures
from testfeatures import GetTestFeatures
from omdbprep import omdbprep
import numpy as np




#lees csv in
with open('ratings.csv','r') as f:
    moviesandtv = list(csv.reader(f,delimiter= ','))
#filter op movies
movies = [];
for movie in moviesandtv:
   if movie[5] == 'movie':
       movies.append(movie)

movies = omdbprep(movies)

#np.random.seed(0)
#np.random.shuffle(movies)
#training, test = moviesX[:np.ceil(len(movies)*2/3)], moviesX[np.ceil(len(movies)*2/3)+1:]

X,Ratings,maxreviews,Directors,Genres,Features,DiDates,AllDi = GetRatingsFeatures(movies)
#X,Ratings,maxreviews,Directors,Genres = GetRatingsFeatures(training)
#TestX,TestRatings = GetTestFeatures(test,maxreviews,Directors,Genres)

#print(np.shape(np.concatenate((X,Ratings.T), axis=0)))

Xw,NewDirector = GetWatchListFeatures(maxreviews,Directors,Genres,DiDates,AllDi)


#create model
model = Sequential()
model.add(Dense(1,kernel_initializer='glorot_normal', activation='relu', input_dim=X.shape[1]))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print(Xw)

# Fit the model
#model.fit(X, Ratings, epochs=1000, batch_size=5)
model.fit(X, Ratings, epochs=100, batch_size=1)


predictions = model.predict(Xw)

with open('watchlist.csv','r') as fin ,open('watchlistratings.csv','w') as fout:
    writer = csv.writer(fout, lineterminator='\n')
    reader = csv.reader(fin)
    all=[]
    row = next(reader)
    row.append('recommendation')
    row.append('newdirector')
    all.append(row)
    k=0
    for row in reader:
        if row[7] == 'movie':
            row.append('{:.2f}'.format(float(predictions[k]*10)))
            row.append(NewDirector[k])
            all.append(row)
            k+=1
    writer.writerows(all)

#scores = model.evaluate(Xw, predictions)
#print(predictions)
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
