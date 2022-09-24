import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle


# Title
st.title("Car Price Prediction")

# read Dataset
df = pd.read_csv("final_scout_not_dummy.csv")

#add image
img = Image.open("indir.png")
st.image(img,caption="Car Price Prediction",width = 500)

# features
st.markdown("## Car Features")
features = ["make_model", "hp_kW", "km","age", "Gearing_Type", "Gears","price"]
df = df[features]



# Creating side bar 
st.sidebar.title("Select the features you want for price estimation")


def user_input_features() :
    make_model = st.sidebar.selectbox("make_model", ("Audi A3","Audi A1","Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"))
    Gearing_Type = st.sidebar.selectbox("Gearing_Type", ("Manual","Automatic", "Semi-automatic"))
    age = st.sidebar.selectbox("age", ("0","1", "2", "3"))
    hp_kW = st.sidebar.slider("hp_kW", 40.0, 239.0, 50.0)
    km = st.sidebar.slider("km", 0.0, 317000.0, 5000.0)
    Gears = st.sidebar.radio("Gears",("5","6","7","8"))
    
    data = {"make_model" : make_model,
            "hp_kW" : hp_kW,
            "km" : km,
            "age" : age,
            "Gearing_Type" : Gearing_Type,
            "Gears" : Gears
            }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()
st.success("Features of Selected Car")
st.table(input_df)


#Read in saved model
samet_model = pickle.load(open("final_scout_not_dummy", "rb"))

#Apply model to make predictions
if st.button('predict'):
    st.success(f'Analyze Predict:{samet_model.predict(d)[0].round(2)}')
