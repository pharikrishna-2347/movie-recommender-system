import pandas as pd
import pickle
import requests
import time

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

api_key = "YOUR_API_KEY"

posters = []

for movie_id in movies['movie_id']:

    try:

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

        response = requests.get(url, timeout=5)

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            full_path = "https://via.placeholder.com/500x750?text=No+Poster"

    except:
        full_path = "https://via.placeholder.com/500x750?text=Error"

    posters.append(full_path)

    print(full_path)

    time.sleep(0.2)

movies['poster'] = posters

movies.to_pickle('movies_with_posters.pkl')

print("DONE")