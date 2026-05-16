import pandas as pd
import streamlit as st
import pickle
import requests
import time

from streamlit.elements.lib.image_utils import PILImage

st.title('Movie Recommender System')

#import streamlit as st
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

option = st.selectbox(
    "Select the movie for recommending similar movies!",
    movies['title'].values,
)

#API fetching
def fetch(movie_id):

    api_key = "83f37ed3a39a255723999dd5186ff30a"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )
        while response.status_code != 200:
            response = requests.get(
                url,
                headers=headers,
                timeout=5
            )
            time.sleep(0.5)

        if response.status_code != 200:
            return "https://via.placeholder.com/300x450?text=API+Error"

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path is None:
            return "https://via.placeholder.com/300x450?text=No+Poster"

        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

        return full_path

    except Exception as e:
        print("ERROR:", e)

        return "https://via.placeholder.com/300x450?text=Connection+Failed"



# we will make a recommend function whose parameter will be the name of the movie selected
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]
    recommended=[]
    posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        link=fetch(movie_id)
        posters.append(link)
        recommended.append(movies.iloc[i[0]].title)
        time.sleep(0.5)
    return recommended,posters


if st.button('Recommend'):
    recommendations,posters = recommend(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])
# Up to here, we will get only movie names as recommendations, now we should also fetch movie poster using its id

