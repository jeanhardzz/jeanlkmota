#IMPORTACOES
import streamlit as st
from PIL import Image


#CONFIGURACOES BASICAS DA PAGINA
st.set_page_config(
    page_title="Jean Mota",
    page_icon="🍌",
    layout="centered",    
)

#CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

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

#NAVBAR
#navbar.navbar()

#CV
#APPs
with st.container():
    st.title("APPS")
    curriculo = """                    
        * * *
        """
    st.markdown(curriculo,unsafe_allow_html= True) 
