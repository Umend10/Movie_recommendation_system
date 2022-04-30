import streamlit as st
import pickle
import pandas as pd
import requests
distance=pickle.load(open('distance.pkl','rb'))

# for online poster getting
def fetch_poster(movie_id):
    b=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a7138fc03ea063cfcf25f8458c74a510&language=en-US")
    c=b.json()
    return 'https://image.tmdb.org/t/p/w500/'+c['poster_path']


def recomend(name):
    index=movies_name[movies_name.original_title==name].index[0]
    d=enumerate(distance.iloc[index].values)
    e=sorted(d,reverse=True,key=lambda x:x[1])[1:7]
    recomende=[]
    

    p=[]
    for i in e:
        p.append(i[0])
        k=i[0]
        recomende.append(fetch_poster(movies_name.iloc[k].movie_id))
    return  movies_name.original_title[p],recomende
    


movies_name=pickle.load(open("movies_name.pkl",'rb'))



st.title("Movie Recomender System")


option = st.selectbox(
     'How would you like to be contacted?',
     movies_name.original_title)

if st.button('Click'):

    try:   
        re,p=recomend(option)
        col1,col2,col3=st.columns(3)

        with col1:

            st.write(re.iloc[0])
            st.image(p[0])
    
        
        with col2:
            st.write(re.iloc[1])

            st.image(p[1])
        with col3:
            st.write(re.iloc[2])
            st.image(p[2])
        
        col4,col5,col6=st.columns(3)
        with col4:
            st.write(re.iloc[3])
            st.image(p[3])
        with col5:
            st.write(re.iloc[4])
            st.image(p[4])
        with col6:
            st.write(re.iloc[5])
            st.image(p[5])
    
    except :
        st.header('sorry problem arrived in image because of API')







    






