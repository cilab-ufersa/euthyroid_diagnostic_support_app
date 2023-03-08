import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

model = joblib.load('/home/vinicius/UFERSA/cilab/euthyroid_diagnostic_support_app/models/RandomForestClassifier.sav')

def get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti):
    user_data = {"age": age,
                "sex": sex,
                "sick": sick,
                "TSH": tsh,
                "T3": t3,
                "TT4": tt4,
                "T4U": t4u,
                "FTI": fti
                }
    features = pd.DataFrame(user_data, index = [0])
    return features

def prediction(user_input_variables):
    prediction = model.predict(user_input_variables)
    return prediction
    st.write("predição: ")
    st.write(prediction)