import pandas as pd
import streamlit as st
import joblib

model = joblib.load('/home/vinicius/UFERSA/cilab/euthyroid_diagnostic_support_app/models/RandomForestClassifier.sav')

def get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti):
    """
    Get user data from the form

    Args:
        age (int): age of the patient
        sex (int): sex of the patient 0 for F and 1 for M
        sick (int): sick of the patient 
        tsh (float): TSH of the patient
        t3 (float): T3 of the patient
        tt4 (float): TT4 of the patient
        t4u (float): T4U of the patient
        fti (float): FTI of the patient

    Returns:
        pd.DataFrame: user data
    
    """

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
    st.write("predição: ")
    st.write(prediction)