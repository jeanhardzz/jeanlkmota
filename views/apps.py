from email.mime import application
from queue import Empty
import streamlit as st
from PIL import Image
from views.applications import indicadores_trader,retas
# Pages logic 

if 'page_retas' not in st.session_state: st.session_state.page_retas = 0
if 'page_apps' not in st.session_state: st.session_state.page_apps = 0
def restart(): st.session_state.page_apps = 0
def page_ind(): st.session_state.page_apps = 1
def page_retas(): st.session_state.page_apps = 2    

def apps():    
    #APPS
                                          
        
    painel = st.empty()
    select = "APPS"
    if st.session_state.page_apps == 0:
        with painel.container():
            st.title("APPS")
            with st.expander("📈Indicadores para Investimentos"):
                text_app = """<div class="textapp">
                <p>Usando pandas para fazer o Cálculo de Médias Móveis, Médias Móveis Exponenciais e Índices de Força Relativa no Dataset Bitcoin Historical Data.</p>            
                </div>"""
                st.markdown(text_app,unsafe_allow_html= True) 
                image = Image.open('./images/bitcoin.png')
                st.image(image,width=200)            
                st.button("Veja", key=1,on_click=page_ind)                    

            with st.expander("📐Interceções com Algoritmos Geométricos"):
                text_app = """<div class="textapp">
                <p>A área de geometria computacional é um ramo da computação que estuda soluções algorítmicas para problemas geométricos. Aqui apresento um algoritmo ótimo em espaço e tempo para saber se há interceção em um determinado grupo de retas</p>            
                </div>"""
                st.markdown(text_app,unsafe_allow_html= True) 
                image = Image.open('./images/geo.png')
                st.image(image,width=200)            
                st.button("Veja", key=2,on_click=page_retas)                                    
                 
    elif st.session_state.page_apps == 1: #Indicadores                                              
        with painel.container():
            st.button("Voltar", key=1,on_click=restart)
            indicadores_trader.indicadores()
            st.button("Voltar", key=2,on_click=restart)

    elif st.session_state.page_apps == 2: #Interceções de retas                              
        with painel.container():                                
            st.button("Voltar", key=1,on_click=restart)
            retas.retas()              
            st.button("Voltar", key=2,on_click=restart)

        
   

        