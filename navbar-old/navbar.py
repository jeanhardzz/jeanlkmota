import streamlit as st

def navbar():

    with st.container():                       
        navbar = """        
        <div class="head">                                           
            <div class="htexto">
                <a href="https://gomesfellipe.github.io/">CV</a>
                <a href="https://gomesfellipe.github.io/">APPS</a>
                <a href="https://gomesfellipe.github.io/">EXTRAS</a>                             
        </div>
        <div style="clear: both;"></div>
        """
        st.markdown(navbar,unsafe_allow_html= True)