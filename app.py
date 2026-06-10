import streamlit as st
import pickle
import pandas as pd

new_df = pd.read_csv("movie.csv")
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        # fetch poster from api
        recommended_movies.append(new_df.iloc[i[0]].title)
    return recommended_movies
        
movies_name=new_df['title'].values
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select your interested Movie.",movies_name
)
 
if  st.button("Recommend"):

    recommendation=recommend(selected_movie_name)
    for i in recommendation:
       st.write(i)

