#IMPORTACOES

from select import select
import streamlit as st
import time 
from PIL import Image
from streamlit_option_menu import option_menu
import cv

#CONFIGURACOES BASICAS DA PAGINA
st.set_page_config(
    page_title="Jean Mota",
    page_icon="🍌",
    layout="centered",    
)

#CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)
               
select = option_menu(
    menu_title="",
    options=["CV","APPS","EXTRAS"],
    default_index=0,    
    orientation="horizontal",
    styles={
        "container": {"color": "#333333","padding": "0!important", "background-color": "#f4f4f4"},
        "icon": {"font-size": "0px"}, 
        "nav-link": {"color": "#333333","font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"color": "#ffffff"},

                
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

#NAVBAR
#navbar.navbar()

#CV
#CURRICULUM VITAE
with st.container():
    st.title("Curriculum Vitae")
    curriculo = """    
        * * *
        
        ## ![pdf](https://img.icons8.com/ios/30/000000/pdf--v1.png) Jean Lucas Almeida Mota

        ![Download](https://img.icons8.com/material-outlined/20/000000/downloading-updates.png) Download da versão em pdf [aqui](https://drive.google.com/file/d/15h2VtB7J8FaxceLiHX4x3pFUCY3K1zth/view?usp=sharing)
        * ![Data Nascimento](https://img.icons8.com/ios-filled/18/000000/birthday.png) 12/06/1997
        * ![Whatsapp](https://img.icons8.com/material-outlined/20/000000/whatsapp--v1.png) (31) 99468-8276
        * ![Linkedin](https://img.icons8.com/ios-glyphs/20/000000/linkedin-2--v1.png) [linkedin.com/in/jeanlkmota](https://www.linkedin.com/in/jeanlkmota/)
        * ![Github](https://img.icons8.com/ios-glyphs/20/000000/github.png) [github.com/jeanhardzz](https://github.com/jeanhardzz)                   
        * ![Email](https://img.icons8.com/ios-filled/20/000000/gmail.png) [jeanlkmota@gmail.com](mailto:jeanlkmota@gmail.com)               
        * ![Instagram](https://img.icons8.com/ios-glyphs/20/000000/instagram-new.png) [instagram.com/jean.lk/](https://www.instagram.com/jean.lk/)               
        * ![Codeforces](https://img.icons8.com/external-tal-revivo-bold-tal-revivo/20/000000/external-codeforces-programming-competitions-and-contests-programming-community-logo-bold-tal-revivo.png) [codeforces.com/profile/jeanhardzz](https://codeforces.com/profile/jeanhardzz)              
        * ![Twitter](https://img.icons8.com/ios-glyphs/20/000000/twitter--v1.png) [twitter.com/Jean_lucks](https://twitter.com/Jean_lucks)              
        
        * * *

        ## ![pdf](https://img.icons8.com/ios/25/000000/info--v1.png) Sobre mim

        Sou apaixonado por problemas difíceis e nada me motiva mais do que resolver problemas do mundo real com tecnologia e trabalho em equipe. Graduando em Matemática Computacional pela UFMG. Técnico em tecnologia da informação pelo Sistema FIEMG. Possuo fortes conhecimentos em matemática e em programação com foco em C,C++ e Python. E tenho muito interesse em trabalhar com empresas que usam seu know-how em projetos de software e iniciativas envolvendo Machine Learning, Blockchain e Data Science para solução de problemas.

        Recentemente tenho me focado em Machine Learning. Acredito que existem inúmeras oportunidades para usar algoritmos e tecnologia para otimizar negócios e criar valor.

        * * *

        ## ![pdf](https://img.icons8.com/ios/25/000000/rocket--v1.png) Habilidades 
          

        <div class="skills">
            <p class="alignleft">python</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot grey"></span> 
            </p>
            <div style="clear: both;"></div>            
            <p class="alignleft">C</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
            </p>
            <div style="clear: both;"></div>
            <p class="alignleft">C++</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
            </p>
            <div style="clear: both;"></div>
            <p class="alignleft">Álgebra</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
            </p>
            <div style="clear: both;"></div>
            <p class="alignleft">Modelagem Matemática</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot grey"></span>
                <span class="dot grey"></span>
            </p>
            <div style="clear: both;"></div>
            <p class="alignleft">Cálculo</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot grey"></span>
            </p>
            <div style="clear: both;"></div>            
            <p class="alignleft">HTML / CSS</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot grey"></span>
                <span class="dot grey"></span>
            </p>
            <div style="clear: both;"></div>
            <p class="alignleft">LaTeX / Markdown</p>
            <p class="alignright">
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
                <span class="dot black"></span>
            </p>
            <div style="clear: both;"></div>
        </div>
        <div style="clear: both;"></div>   

        * * *        

        ## ![pdf](https://img.icons8.com/ios/25/000000/project-management.png) Projetos/Planos
        
        Graduando em Matemática Computacional pela UFMG e fazendo Iniciação Científica em Problemas Difíceis em Grafos com Vinicius Fernandes do Santos do Departamento da Computação (DCC). Tenho me dedicado de forma ativa em projetos pessoais, a fim de colocar em prática todo o meu conhecimento teórico. E faço cursos online, como também leio, constantemente, tanto sobre minha área de atuação, quanto sobre assuntos diversos como psicologia, oratória, filosofia, empreendedorismo e inovação. Meu lema é Stay Hungry Stay Foolish, inspirado pelo Steve Jobs.

        Minha intenção com esta página é poder visualizar minha evolução, manter um portfólio dos meus projetos e quem sabe interagir com pessoas que se interessam por inovações tecnológicas e científicas.

        
        * * *

        ## ![pdf](https://img.icons8.com/glyph-neue/30/000000/university.png) Formação Acadêmica    

        - Curso de graduação em Matemática Computacional - conclusão em 2023/2 - UFMG - Universidade Federal de Minas Gerais
        - Técnico em tecnologia da informação - concluído em 2014 - Sistema FIEMG - Federação das Indústrias do Estado de Minas Gerais
      
        * * *

        ## ![pdf](https://img.icons8.com/ios/25/000000/new-job.png) Certificados

        Alura:

        - [Git e Github: Controle e Compartilhe seu Código](https://drive.google.com/file/d/1mBd0o4ZXunB7zTOZWPIRC2KTn5b7JPPm/view?usp=sharing)
        - [Python: Começando com a Linguagem](https://drive.google.com/file/d/1a1zffG3eT6_iN--iICzp6ERA9x8UUBtO/view?usp=sharing)
        - [Python: Avançando na Linguagem](https://drive.google.com/file/d/1W8yOsrrPnDBSqZ8ore_6qnPPdOSzU2kW/view?usp=sharing)
        - [Python: Entendendo a Orientação a Objetos](https://drive.google.com/file/d/1DN8M9qMRc-laWl8cMd-95oZTgnPoFsP5/view?usp=sharing)
        - [Python: Avançando na Orientação a Objetos](https://drive.google.com/file/d/1PbgM7h14JodOw65JVnd0PW61LCRhjNaJ/view?usp=sharing)
        - [Teste Automatizados: TDD com Python](https://drive.google.com/file/d/1gq4SNiOhwPJG1Wka9iZ2QR-3MgOWnNzX/view?usp=sharing)
        - [Data Science: Analise e Visualização de Dados](https://drive.google.com/file/d/1-yDS_F0N7MQ2bGRI72gP_HW2KZ-x7FtE/view?usp=sharing)
        * * *
        """
    st.markdown(curriculo,unsafe_allow_html= True) 
