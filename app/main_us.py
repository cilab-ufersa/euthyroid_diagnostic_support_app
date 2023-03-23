import streamlit as st
from PIL import Image
from utils import *
from prediction import *


class Main():
    """ Main class of the app """
    def __init__(self):
        image = Image.open('icon/cilab.png')
        st.set_page_config(
            page_title="DSS - Diagnostic Support System",
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
        st.title("Diagnostic support system: Euthyroid Sick Syndrome")
       
        st.markdown('---')
        # set the subtitle 
        st.markdown('<style>h2{font-size: 20px;}</style>', unsafe_allow_html=True)
        st.header("Do you know what the sick euthyroid syndrome is?")

        col1, col2 = st.columns(2)
        with col2:
            st.markdown('<style>p{text-align: justify;}</style>', unsafe_allow_html=True)
            st.markdown("""
           Euthyroid sick syndrome is a medical condition that
             affects the thyroid gland and can be detected through
             interpretation of test results such as T4, TSH and T3. However, the
             Subjective interpretation of these results can make diagnosis difficult.
             for the healthcare professional. To help with this task, a model of
             artificial intelligence was developed to predict whether the patient has
             or not the syndrome based on your examination data. However, it is important
             remember that artificial intelligence can present false positives and
             false negatives, therefore, your result should not be considered as
             absolute and should not replace the clinical judgment of the healthcare professional.
             It is recommended that the result of artificial intelligence be interpreted
             with caution and that the diagnosis is confirmed by the health professional.
            """)
        with col1:
            image = Image.open('icon/icon.png')
            st.image(image, caption='Euthyroid Sick Syndrome', width=450)
        st.markdown('---')


        st.header("Perform diagnosis using the artificial intelligence model") 
        st.markdown('<style>div.row-widget.stButton > button {margin-left: 45%;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.button("Perform Diagnosis",on_click=lambda:self.set_page(1))  

        st.markdown('---')
        st.markdown('<style>h2{color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.header("About the project")
        st.markdown('<style>p{text-align: justify;}</style>', unsafe_allow_html=True)
        st.markdown("""
        This is a project of the Federal Rural University of the Semi-Arid (UFERSA) that aims to
         to develop a diagnostic support system for the euthyroid sick syndrome. The project
         It is coordinated by Professor Dr. Rosana Rego and has the participation of
         scientific developers: Vinicius Anacleto, Caio Moisés, Macors.""")

        st.markdown('---')
        st.markdown('<style>h3{color: #1E90FF;}</style>', unsafe_allow_html=True)
        # centralize the subheader
        #st.markdown('<style>h3{text-align: center;}</style>', unsafe_allow_html=True)
        # set the subheader size
        st.markdown('<style>h3{font-size: 15px;}</style>', unsafe_allow_html=True)
        st.subheader("Support by:")
        image = Image.open('icon/Ufersa.png')
        st.image(image, caption='UFERSA', width=70)


    

            
if __name__ == '__main__':
    main = Main()