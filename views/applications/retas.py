from typing import Container
import streamlit as st
import mpld3
import streamlit.components.v1 as components
from views.applications import any_segments_intersect

if 'page_retas' not in st.session_state: st.session_state.page_retas = 0
def restart(): st.session_state.page_retas = 0
def new_retas(): st.session_state.page_retas = 1

def retas(): 
    
    texto = """
        #### Interceções com Algoritmos Geométricos 
        Este projeto possui o intuito de aprender um pouco mais sobre a geometria computacional. Aqui foi implementado o algoritmo visto em Algoritmos Teoria e Pratica - Thomas H. Cormen.

        * * * 
        #### Visualização 
        Primeiro é gerado um conjunto de retas aleatórias e então é calculado se há ou não interceções.
        """            
    st.markdown(texto,unsafe_allow_html= True)    
    n = st.number_input('',min_value=2, max_value=100,)
    n = int(n)
    st.button("Gerar Retas", key=3,on_click=new_retas)
    if st.session_state.page_retas == 1:        
        fig,msg = any_segments_intersect.AnySegmentsIntersect(n)


    fig,msg = any_segments_intersect.AnySegmentsIntersect(n)
    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=500)

    st.markdown("""
    <h3 style = "text-align: center;">""" + msg +
    """</h3>
    """
    ,unsafe_allow_html= True)

    st.markdown("* * *",unsafe_allow_html= True)       
      

       
    