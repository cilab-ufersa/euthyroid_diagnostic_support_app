import joblib
import streamlit as st
from utils import *
import pandas as pd
import numpy as np

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
        col1, col2, col3 = st.columns([2, 0.5, 2])

        with col1:
            self.data_values()

        with col2: 
            pass 

        with col3:
       
            st.header("Métricas do modelo")
            df = pd.read_csv("models/models.csv")
            col_1, col_2, col_3 = st.columns(3)
            col_1.metric("Acurácia", value=str(int(100*df['acuracia']))+"%", help="Acurácia do modelo: indica o quão precisa é a previsão de um modelo")
            col_2.metric("Precisão", value=str(int(100*df['precisao']))+"%", help="Precisão do modelo: indica a capacidade do modelo de prever corretamente os casos em que o paciente tem a doença")
            col_3.metric("Recall", value=str(int(100*df['recall']))+"%", help="Recall do modelo: indica quantos casos em que o paciente tem a doença o modelo conseguiu identificar no conjunto de dados")

            st.markdown('---')
            st.markdown('<style>p{ text-align: justify;, font-weight: bold;}</style>', unsafe_allow_html=True)
            st.warning("**ATENÇÃO**: Embora os resultados de testes e modelos sejam importantes, é fundamental lembrar que eles não devem ser usados como uma única fonte de informação ou como uma decisão definitiva. É essencial que um profissional de saúde utilize seu conhecimento clínico e julgamento para interpretar e avaliar adequadamente esses resultados, garantindo que os pacientes recebam o tratamento mais adequado e seguro.")
            
        

        
        

    def predict_result(self, user_input_variables):
        """
        Predict the result of the user input variables

        Args:
            user_input_variables (pd.DataFrame): user data
        
        """
        #try:
        model = joblib.load(self.path)
        response = model.predict(user_input_variables)
        print(response)
        if response == 0:
            st.success(f"Chances de ter euthyroid: BAIXA", icon="✅")
        if response == 1:
            st.warning(f"Chances de ter euthyroid: ALTA")

        '''except:
            st.error("Erro ao carregar o modelo")            
        st.markdown('---')
        '''
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
        
        age = st.number_input("Idade",min_value=1, max_value=100, value=1, key="age", help="Idade do paciente")
        sex = st.selectbox("Sexo",("F","M"), key="sex")
        sick = st.selectbox("Possui algum distúrbio da tireoide?", ("Não", "Sim"), key="sick", help="Se o paciente possui algum distúrbio da tireoide já conhecido")
        tsh = st.number_input("TSH",min_value=0.0, max_value=100.0, value=0.0, key="tsh", help="TSH é a sigla para hormônio estimulante da tireoide, que é produzido pela glândula pituitária")
        t3 = st.number_input("T3",min_value=0.0, max_value=100.0, value=0.0, key="t3", help="T3 é a sigla para triiodotironina, que é um hormônio produzido pela glândula tireoide")
        tt4 = st.number_input("TT4",min_value=0.0, max_value=100.0, value=0.0, key="tt4", help="TT4 é a sigla para tiroxina total, que é um hormônio produzido pela glândula tireoide")
        t4u = st.number_input("T4 Livre",min_value=0.0, max_value=100.0, value=0.0, key="t4u", help="Tiroxina livre, que é um hormônio produzido pela glândula tireoide")
        fti = st.number_input("FTI",min_value=0.0, max_value=200.0, value=0.0, key="fti", help="FTI é a sigla para índice de tiroxina livre, que é um hormônio produzido pela glândula tireoide")

        sex = sex_string2int(sex)
        sick = sick_string2int(sick)
        scaler = StandardScaler()
        
        user_data = get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti)
        data_scaled = scaler.fit_transform(user_data.reshape(8, -1))
        self.user_input_variables = data_scaled.reshape(-1, 8)
        #print(self.user_input_variables)

        st.markdown('---')
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
 
        but1, but2, but3 = st.columns(3)
        with but1:
            st.button("Realizar predição",on_click=lambda:self.predict_result(self.user_input_variables), key="prediction")
        with but2:
            st.button("Limpar", on_click=lambda: self.clear_values(), key="clear")
        with but3:
            pass

        


    def clear_values(self):
        """ Clear all values """
        st.session_state.age = 1
        st.session_state.tsh =0.0
        st.session_state.t3 =0.0
        st.session_state.tt4 =0.0
        st.session_state.t4u =0.0
        st.session_state.fti =0.0
