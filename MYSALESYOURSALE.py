import streamlit as st
import pandas as pd
import seaborn as sns
import pickle

st.write("# Simple Sales Prediction App")
st.write("This app predicts the **Sales Price** type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    #('X',min,max,default)
    TV = st.sidebar.slider('TV', 00, 300, 150)
    Radio = st.sidebar.slider('Radio', 00, 50, 35)
    Newspaper = st.sidebar.slider('Newspaper', 00, 115, 60)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_modelSVR = pickle.load(open("SalesNew.h5", "rb"))
pred = loaded_modelSVR.predict(df)

st.subheader('Sales Price Prediction')
st.write(pred)
