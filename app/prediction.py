import joblib
import streamlit as st
from utils import *


class Prediction:
    def __init__(self, path):
        """
        Class to predict the result of the user input variables

        Args:
            path (str): path to the model
            user_input_variables (pd.DataFrame): user data
        """

        self.path = path

        self.page()

    def page(self):
        """
        Prediction page
        """
        col1, col2 = st.columns(2)

        with col1:
            self.data_values()

        # TODO(Vinicius) adicionar as métricas do modelo
        #with col2:
            # adicionar as métricas do modelo (acuracy, precision, recall)
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Acuracia", "0.9834")
            col2.metric("Precisão", "0.9838")
            col3.metric("Recall", "0.9821")
            col4.metric("F1 score", "0.9830")


        
        

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
                st.success(f"Chances de ter euthyroid: BAIXA", icon="✅")
            if response == 1:
                st.warning(f"Chances de ter euthyroid: ALTA")
        except:
            st.error("Erro ao carregar o modelo")            
        st.markdown('---')

    def data_values(self):
        """
        Get the data values from the user input variables

        Returns:
            pd.DataFrame: user data
        """
                 
        st.markdown('<style>h1{font-size: 30px;}</style>', unsafe_allow_html=True)
        st.header("Preencha os campos com os dados solicitados:")
        # change color of the number input when the user click on it
        st.markdown('<style>input[type=number] {color: #1E90FF;}</style>', unsafe_allow_html=True)
        
        age = st.number_input("Idade",min_value=0, max_value=100, value=0, key="age")
        sex = st.selectbox("Sexo",("F","M"), key="sex")
        sick = st.selectbox("Possui algum distúrbio da tireoide?", ("Não", "Sim"), key="sick")
        tsh = st.number_input("TSH",min_value=0.0, max_value=100.0, value=0.0, key="tsh")
        t3 = st.number_input("T3",min_value=0.0, max_value=100.0, value=0.0, key="t3")
        tt4 = st.number_input("TT4",min_value=0.0, max_value=100.0, value=0.0, key="tt4")
        t4u = st.number_input("T4U",min_value=0.0, max_value=100.0, value=0.0, key="t4u")
        fti = st.number_input("FTI",min_value=0.0, max_value=100.0, value=0.0, key="fti")

        sex = sex_string2int(sex)
        sick = sick_string2int(sick)

        self.user_input_variables = get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti)
        st.button("Realizar predição",on_click=lambda:self.predict_result(self.user_input_variables), key="prediction")
        
        # change the button color
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.button("Limpar", on_click=lambda: self.clear_values(), key="clear")

    def clear_values(self):
        """ Clear all values """
        st.session_state.age = 1
        st.session_state.tsh =0.0
        st.session_state.t3 =0.0
        st.session_state.tt4 =0.0
        st.session_state.t4u =0.0
        st.session_state.fti =0.0
