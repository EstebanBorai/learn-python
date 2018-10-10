# This is a Python List not an Array, "read-to-use"
movies = ["The Holy Grail", "The Life of Brian", "The Meaning Of Life"]
years = [1975, 1979, 1983]

fav_movies = []

for i in range(len(movies)):
	fav_movies.extend([movies[i], years[i]])
movies = fav_movies

print(movies)
