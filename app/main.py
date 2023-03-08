import streamlit as st
from PIL import Image
from utils import *


class Main():
    """ Main class of the app """
    def __init__(self):
        image = Image.open('app/icon/cilab.png')
        st.set_page_config(
            page_title="ESS - Sistema de apoio ao diagnóstico",
            page_icon=image
        )
        
        self.placeholder = st.empty()
        self.home()
            
       
    def set_page(self,num):
        st.session_state.page=num
        
    def home(self):
        """ Home page """
   
        # set the page title 
        st.title("Sistema de apoio ao diagnóstico")
        st.header("Síndrome do Eutireoideo doente")
        col1, col2 = st.columns([1,3]) # duas colunas com tamanhos diferentes 1 e 3

 
        with col1:
            st.text("Insira os dados:")
            age = st.number_input("Idade",min_value=1, max_value=100, value=1)
            sex = st.selectbox("Sexo",("F","M"))
            sick = st.selectbox("Possui a doença?", ("Sim", "Não"))
            tsh = st.number_input("TSH",min_value=0.0, max_value=10.0, value=0.0)
            t3 = st.number_input("T3",min_value=0.0, max_value=10.0, value=0.0)
            tt4 = st.number_input("TT4",min_value=0.0, max_value=10.0, value=0.0)
            t4u = st.number_input("T4U",min_value=0.0, max_value=10.0, value=0.0)
            fti = st.number_input("FTI",min_value=0.0, max_value=10.0, value=0.0)
            #st.button("Realizar predição",on_click=lambda:self.set_page(1))
            #sex = sex.astype(str).astype(int)
            user_input_variables = st.button("Realizar predição",on_click = get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti))
            #prediction(user_input_variables)


        with col2:
            st.header("Você sabe o que é a sindrome do Eutireoideo doente?")

            # escrever sobre a sindrome 
            st.markdown("""<div><p align="justify">A síndrome do doente Eutireoideo é uma condição em que ocorre um distúrbio na regulação hormonal das glândulas tireóideas em pacientes que apresentam alguma outra doença ou infecção (Geomann e Wajner, 2009). Embora a tireoide esteja funcionando normalmente, a sua produção de hormônios tireoidianos é afetada pela inflamação, infecção ou outra condição.</p></div>""", unsafe_allow_html=True) 

        # set a icon image in footer in the center
        st.text("Realização")
        st.markdown("<center><img src='https://raw.githubusercontent.com/cilab-ufersa/euthyroid_diagnostic_support_app/main/app/icon/cilab.png' width='200'></center>", unsafe_allow_html=True) 
        st.markdown("<center><img src='https://raw.githubusercontent.com/cilab-ufersa/euthyroid_diagnostic_support_app/main/app/icon/Ufersa.png' width='70'></center>", unsafe_allow_html=True)

    
        st.markdown("""
                        <br/>
                        <br/>
                        <center>
                                <a href="https://github.com/cilab-ufersa/euthyroid_diagnostic_support_app">
                                    <div class="row-widget stButton" style="width: 600px;">
                                        <button kind="secondary" class="css-5uatcg edgvbvh10">
                                            <div data-testid="stMarkdownContainer" class="css-1fv8s86 e16nr0p34">
                                                <p>Source</p>
                                            </div>
                                        </button>
                                    </div>
                                </a>
                        </center>
                        """,unsafe_allow_html=True)
     
        

            
if __name__ == '__main__':
    main = Main()