import streamlit as st
import pandas as pd
import seaborn as sns


st.write("# Simple Sales Prediction App")
st.write("This app predicts the **Sales Price** type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    *('X',min,max,default)
    TV = st.sidebar.slider('TV', 0.00, 300, 150)
    Radio = st.sidebar.slider('Radio', 0.00, 50, 35)
    Newspaper = st.sidebar.slider('Newspaper', 0.00, 115, 60)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

loaded_modelSVR = pickle.load(open("SalesNew.h5", "rb"))
TV=loaded_modelSVR.predict(df)
st.write(prediction_proba)
