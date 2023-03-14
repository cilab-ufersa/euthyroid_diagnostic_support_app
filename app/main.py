import streamlit as st
from PIL import Image
from utils import *
from prediction import *


class Main():
    """ Main class of the app """
    def __init__(self):
        image = Image.open('app/icon/cilab.png')
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
            Prediction(path="models/RandomForestClassifier.sav")
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
       

        # set the subtitle 
        st.markdown('<style>h2{font-size: 20px;}</style>', unsafe_allow_html=True)
        st.header("Você sabe o que é a sindrome do Eutireoideo doente?")

        # add a image
        image = Image.open('icon/icon.png')
        st.image(image, caption='Síndrome do Eutireoideo doente', use_column_width=True)

        # TODO(Vinicius) escrever sobre a sindrome 
        st.markdown("""<div><p align="justify">A síndrome do doente Eutireoideo é uma condição em que ocorre um distúrbio na regulação hormonal das glândulas tireóideas em pacientes que apresentam alguma outra doença ou infecção (Geomann e Wajner, 2009). Embora a tireoide esteja funcionando normalmente, a sua produção de hormônios tireoidianos é afetada pela inflamação, infecção ou outra condição.</p></div>""", unsafe_allow_html=True) 
        # change button color 
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.button("Realizar Diagnóstico",on_click=lambda:self.set_page(1))  
        

            
if __name__ == '__main__':
    main = Main()