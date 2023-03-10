import joblib
import pandas as pd
import streamlit as st
from utils import *

class Prediction:
    def __init__(self, path, user_input_variables):
        self.path = path
        
        self.predict_result(user_input_variables)

    def predict_result(self, user_input_variables):
        
        model = joblib.load(self.path)
        response = model.predict(user_input_variables.values)


        if response == 0:
            st.info(f"Chances de ter euthyroid: BAIXA")
        if response == 1:
            st.warning(f"Chances de ter euthyroid: MÉDIA")

            
        st.markdown('---')