#IMPORTACOES

import streamlit as st
import time 
from PIL import Image
from streamlit_option_menu import option_menu
from views import cv

#CONFIGURACOES BASICAS DA PAGINA
st.set_page_config(
    page_title="Jean Mota",
    page_icon="🍌",
    layout="centered",    
)

#CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


#NAVBAR
#usar no futuro "border": "solid 1px rgba(160, 160, 160, 0.3)","         
        
        
select = option_menu(
    menu_title="",
    options=["CV","APPS","EXTRAS"],
    default_index=0,    
    orientation="horizontal",
    styles={
        "container": {"border": "solid 1px rgba(160, 160, 160, 0.3)","padding": "5!important", "background-color": "#f4f4f4"},
        "icon": {"font-size": "0px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {},
                
    }
)


#MENU LATERAL
with st.sidebar:
    """    
    """    
    image = Image.open('./images/perfil.png')

    st.image(image,  width=200)
    
    """
    ## Jean Mota
    Stay Hungry Stay Foolish

    [![Github](https://img.icons8.com/ios-glyphs/20/000000/github.png)](https://github.com/jeanhardzz) [![Linkedin](https://img.icons8.com/ios-glyphs/20/000000/linkedin-2--v1.png)](https://www.linkedin.com/in/jeanlkmota/) [![Email](https://img.icons8.com/ios-filled/20/000000/gmail.png)](mailto:jeanlkmota@gmail.com) [![Instagram](https://img.icons8.com/ios-glyphs/20/000000/instagram-new.png)](https://www.instagram.com/jean.lk/) [![Codeforces](https://img.icons8.com/external-tal-revivo-bold-tal-revivo/20/000000/external-codeforces-programming-competitions-and-contests-programming-community-logo-bold-tal-revivo.png)](https://codeforces.com/profile/jeanhardzz) [![Twitter](https://img.icons8.com/ios-glyphs/20/000000/twitter--v1.png)](https://twitter.com/Jean_lucks)                        

    """

    #html = "<h1>Meu Perfil</h1>"
    #st.markdown(html,unsafe_allow_html=True)
    
if(select == "CV"):
    cv.cv()

elif(select == "APPS"):
    st.title("APPS")

elif(select == "EXTRAS"):
    st.title("EXTRAS")    
