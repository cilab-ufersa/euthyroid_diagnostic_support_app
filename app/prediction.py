import joblib
import streamlit as st
from utils import *

class Prediction:
    def __init__(self, path, user_input_variables):
        """
        Class to predict the result of the user input variables

        Args:
            path (str): path to the model
            user_input_variables (pd.DataFrame): user data
        """

        self.path = path
        
        self.predict_result(user_input_variables)

    def predict_result(self, user_input_variables):
        """
        Predict the result of the user input variables

        Args:
            user_input_variables (pd.DataFrame): user data
        
        """
        try:
            model = joblib.load(self.path)
            response = model.predict(user_input_variables)
            if response == 0:
                st.info(f"Chances de ter euthyroid: BAIXA")
            if response == 1:
                st.warning(f"Chances de ter euthyroid: MÉDIA")
        except:
            st.error("Erro ao carregar o modelo")            
        st.markdown('---')