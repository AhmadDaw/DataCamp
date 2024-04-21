import pandas as pd
import random

# Create a list of movie names
movie_names = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Inception', 'Forrest Gump',
               'The Lord of the Rings: The Fellowship of the Ring', 'Pulp Fiction', 'The Matrix', 'Schindler\'s List',
               'The Silence of the Lambs', 'Goodfellas', 'The Departed', 'The Shining', 'Saving Private Ryan',
               'The Prestige']

# Generate random average ratings between 1 and 10
avg_ratings = [random.uniform(1, 10) for _ in range(len(movie_names))]

# Create the DataFrame
movies = pd.DataFrame({'movie_name': movie_names, 'avg_rating': avg_ratings})

movies_gt_five=movies[movies['avg_rating']>5]

movies.drop(movies[movies['avg_rating']<5].index,inplace=True)

print(movies)

assert movies['avg_rating'].max() > 5

