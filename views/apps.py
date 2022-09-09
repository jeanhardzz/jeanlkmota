from email.mime import application
import streamlit as st
from PIL import Image
from views.applications import indicadores_trader

def apps():
    #APPS                                          
        
    painel = st.empty()

    with painel.container():
        st.title("APPS")
        with st.expander("📈Indicadores para Investimentos"):
            text_app = """<div class="textapp">
            <p>Usando pandas para fazer o Cálculo de Médias Móveis, Médias Móveis Exponenciais e Índices de Força Relativa no Dataset Bitcoin Historical Data.</p>            
            </div>"""
            st.markdown(text_app,unsafe_allow_html= True) 
            image = Image.open('./images/bitcoin.png')
            st.image(image,width=200)            
            if st.button("Veja"):                
                with painel.empty():                    
                    indicadores_trader.indicadores()                                     
                 
    
        
   

        