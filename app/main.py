import streamlit as st
from PIL import Image

class Main():
    """ Main class of the app """
    def __init__(self):
        image = Image.open('/home/rosana/Documentos/projects/euthyroid_diagnostic_support_app/app/icon/cilab.png')
        st.set_page_config(
            page_title="Predição",
            page_icon=image
        )
        
        self.placeholder = st.empty()
        self.home()
            
       
    def set_page(self,num):
        st.session_state.page=num
        
    def home(self):
        
        col1, col3, col5 = st.columns(3)

        with col1:
            st.text("Realizar a predição\nda possibilidade\nde sindrome na tireoide")
            
        
        with col3:
            st.header("O que você deseja fazer?")
        
        with col5:
            st.text("Realizar a analise das\nfeatures utilizadas\nno modelo")
    
        st.markdown("""
                        <br/>
                        <br/>
                        <center>
                                <a href="https://github.com/cilab-ufersa/euthyroid_diagnostic_support_app">
                                    <div class="row-widget stButton" style="width: 600px;">
                                        <button kind="secondary" class="css-5uatcg edgvbvh10">
                                            <div data-testid="stMarkdownContainer" class="css-1fv8s86 e16nr0p34">
                                                <p>Github</p>
                                            </div>
                                        </button>
                                    </div>
                                </a>
                        </center>
                        """,unsafe_allow_html=True)
     
        

            
if __name__ == '__main__':
    main = Main()