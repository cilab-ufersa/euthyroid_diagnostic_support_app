import streamlit as st
from PIL import Image
from utils import *
from prediction import *


class Main():
    """ Main class of the app """
    def __init__(self):
        image = Image.open('icon/cilab.png')
        st.set_page_config(
            page_title="ESS - Sistema de apoio ao diagnóstico",
            page_icon=image,
            layout="wide",
            initial_sidebar_state="expanded"
            )
        
        self.placeholder = st.empty()

        if "page" not in st.session_state:
            st.session_state.page = 0
            
        if st.session_state.page == 0:
            self.home()
            
        if st.session_state.page == 1:
            Prediction(path="../models/RandomForestClassifier.sav")
            st.button("Voltar",on_click=lambda:self.set_page(0))
            
 
    def set_page(self,num):
        st.session_state.page=num
        
    def home(self):
        """ Home page """

        # set the title 
        st.markdown('<style>h1{font-size: 30px;}</style>', unsafe_allow_html=True)
        # set title color 
        st.markdown('<style>h1{color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.title("Sistema de apoio ao diagnóstico: Síndrome do Eutireoideo doente")
       
        st.markdown('---')
        # set the subtitle 
        st.markdown('<style>h2{font-size: 20px;}</style>', unsafe_allow_html=True)
        st.header("Você sabe o que é a sindrome do Eutireoideo doente?")

        col1, col2 = st.columns(2)
        with col2:
            st.markdown('<style>p{text-align: justify;}</style>', unsafe_allow_html=True)
            st.markdown("""
            A síndrome do doente eutireoideo é uma condição médica que
            afeta a glândula tireoide e pode ser detectada por meio da
            interpretação de resultados de exames, como T4, TSH e T3. No entanto, a
            interpretação subjetiva desses resultados pode tornar o diagnóstico difícil
            para o profissional de saúde. Para ajudar nessa tarefa, um modelo de
            inteligência artificial foi desenvolvido para prever se o paciente tem
            ou não a síndrome com base em seus dados de exame. No entanto, é importante
            lembrar que a inteligência artificial pode apresentar falsos positivos e
            falsos negativos, portanto, seu resultado não deve ser considerado como
            absoluto e não deve substituir o julgamento clínico do profissional de saúde.
            É recomendado que o resultado da inteligência artificial seja interpretado
            com cautela e que o diagnóstico seja confirmado pelo profissional de saúde.
            """)
        with col1:
            image = Image.open('icon/icon.png')
            st.image(image, caption='Síndrome do Eutireoideo doente', width=450)
        st.markdown('---')


        st.header("Realize o diagnóstico utilizando o modelo de inteligência artificial") 
        st.markdown('<style>div.row-widget.stButton > button {margin-left: 45%;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.button("Realizar Diagnóstico",on_click=lambda:self.set_page(1))  

        st.markdown('---')
        st.markdown('<style>h2{color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.header("Sobre o projeto")
        st.markdown('<style>p{text-align: justify;}</style>', unsafe_allow_html=True)
        st.markdown("""
        Este é um projeto da Universidade Federal Rural do Semi-Árido (UFERSA) que tem como objetivo
        desenvolver um sistema de apoio ao diagnóstico para a síndrome do doente eutireoideo. O projeto 
        é coordenado pela professora Dra. Rosana Rego e conta com a participação dos 
        desenvolvedores científicos: Vinicius Anacleto, Caio Moisés, Macors.""")

        st.markdown('---')
        st.markdown('<style>h3{color: #1E90FF;}</style>', unsafe_allow_html=True)
        # centralize the subheader
        #st.markdown('<style>h3{text-align: center;}</style>', unsafe_allow_html=True)
        # set the subheader size
        st.markdown('<style>h3{font-size: 15px;}</style>', unsafe_allow_html=True)
        st.subheader("Apoio")
        image = Image.open('icon/Ufersa.png')
        st.image(image, caption='UFERSA', width=70)


    

            
if __name__ == '__main__':
    main = Main()