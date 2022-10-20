import pandas as pd
watched_films = pd.read_csv('2 laba\\watchedFilms.csv')
genre_values = dict(watched_films.Genre.value_counts())
recommend_films = pd.read_csv('2 laba\\films.csv')  
genre_weight, views_weight, ratings_weight = input("Введите вес Жанра: "), input("Введите вес Просмотров: "), input("Введите вес Рейтинга: ") 
for genre in genre_values: 
    recommend_films.loc[(recommend_films.Genre == genre), 'Genre'] = genre_values[genre]
recommend_films.Genre *= float(genre_weight)
recommend_films.Views *= float(views_weight)
recommend_films.Ratings *= float(ratings_weight)
recommend_films['Weight'] = recommend_films.Genre+recommend_films.Views+recommend_films.Ratings 
result = recommend_films.sort_values('Weight', ascending=False).head(3) 
print(result.Name)