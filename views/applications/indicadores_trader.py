import streamlit as st
from PIL import Image
import pandas as pd

def indicadores():            
    texto = """
    #### Cálculo de indicadores 
    Este projeto possui o intuito de calcular as médias móveis, médias móveis exponenciais e índice de força relativa usando o histórico de preços do bitcoin. Bem como visualizar esses dados em um gráfico. 

    * * *

    **Dataset usado:** https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv        

    * * *

    ##### Importando Dataset
    
        import pandas as pd
        dados = pd.read_csv("coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv")
        dados.dropna(subset=dados.columns,inplace=True)
        dados.index = range(dados.shape[0])
        dados.info()
    
    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img1.png?raw=true)    
    
    * * *

    ##### Médias Móveis
    Média Móvel é uma media do preço dos ultimos N fechamentos de um ativo.
    <br /><br />
    Sendo que o N é chamado de periodo, e esta sendo utilizando um periodo de 20. Dependendo do dataset, 20 periodos podem ser 20 minutos, 20 horas, 20 dias ou 20 anos.
    <br /><br />
    No dataset utilizado 20 periodos representam 20 minutos.
    <br />
    <br />
        
        media=dados['Close'].rolling(window=20).mean()
        media
    
    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img2.png?raw=true)
    
    * * *

    ##### Médias Móveis Exponenciais

    Média Móvel Exponencial é uma media ponderada do preço dos ultimos N fechamentos de um ativo, dando mais peso para os fechamentos mais próximos.
    <br /><br />
    Sendo que o N é chamado de periodo, e esta sendo utilizando um periodo de 20. Dependendo do dataset, 20 periodos podem ser 20 minutos, 20 horas, 20 dias ou 20 anos.
    <br /><br />
    No dataset utilizado 20 periodos representam 20 minutos.
    <br />
    <br />
    
        media = dados['Close'].ewm(span=20, adjust=False).mean()
        media
    
    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img3.png?raw=true)
    
    * * *

    ##### Índices de Força Relativa
    O indice de força relativa (RSI em inglês) foi desenvolvido por J. Welles Wilder. É um indice com escala de variação fixa, ou seja, varia entre 0 e 100. É usado para identificar a subvalorização ou sobrevalorização de um ativo. 
    <br /><br />
    Exemplo: Quanto maior o indice (>70) mais sobrevalorizada o ativo esta, e quanto menor o indice (<30) mais subvalorizada o ativo esta.
    <br /><br />
    **$IFR = 100 – (100 ÷ (1+ (U/D))$**
    <br /><br />
    **IFR** = Índice de Força Relativa
    <br />
    **U** = Média das cotações dos últimos n dias em que a cotação da ação subiu. Trata-se da soma das cotações dos últimos n dias em que a cotação da ação subiu, dividido por n.
    <br />
    **D** = Média das cotações dos últimos n dias em que a cotação da ação caiu. Trata-se da soma das cotações dos últimos n dias em que a cotação da ação caiu, dividido por n.
    <br />
    **n** = O numero de dias mais utilizado pelo mercado é 14, e recomendado por Wilder quando da publicação de seu livro. Por isso, esse é o default da plataforma gráfica de análise técnica do Bússola do Investidor. Mas também é comum usar um IFR de 9 ou 25 dias, e você pode customizar o indicador para quantos períodos desejar.
    <br />
    <br />

        import numpy as np

        def calcula_indices_de_força_relativa(precos, n=14):                
                deltas = np.diff(precos)  # pegando a diferença preco[0]-preco[1] e guardando em deltas[0]
                primeiros = deltas[:n]  # pegando as diferença 14 primeiras diferenças
                        
                ganho = primeiros[primeiros >= 0].sum() / n  # media das diferenças positivas dentre as 14 iniciais
                perda = -primeiros[primeiros < 0].sum() / n  # media das diferenças negativas dentre as 14 iniciais

                forca_relativa = ganho / perda  # calculando a força relativa

                rsi = np.zeros_like(precos)  # criando uma copia de precos só com zeros

                rsi[:n] = 100. - 100. / (1. + forca_relativa)  # calculando rsi para os 14 primeiros precos, serao iguais
         
                
                for i in range(n, len(precos)):
                    delta = deltas[i - 1]

                    if (delta >= 0):
                        ganho_variacao = delta
                        perda_variacao = 0.
                    else:
                        ganho_variacao = 0.
                        perda_variacao = -delta
                    
                    ganho = (ganho * (n - 1) + ganho_variacao) / n
                    perda = (perda * (n - 1) + perda_variacao) / n

                    forca_relativa = ganho / perda

                    rsi[i] = 100. - 100. / (1. + forca_relativa)

                return rsi

        indice_rsi = calcula_indices_de_força_relativa(dados['Close'])
        indice_rsi = pd.DataFrame(data=indice_rsi)
        indice_rsi
    
    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img4.png?raw=true)

    * * *

    ##### Criando coluna DateTime
        from datetime import datetime
        import time

        def fun_date (x):
            dt = datetime.utcfromtimestamp(x)    
            return dt
        dados['Datetime'] = dados['Timestamp'].apply(fun_date)


        dados.index= range(dados.shape[0])

        dados.head(10)

    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img5.png?raw=true)
    <br />
    O periodo de minutos é muito ruim de trabalhar, vamo transformar isso em dias.

    * * *

    ##### Criando novo DataSet com periodo em DIAS

    Vou pegar a coluna Datetime e a coluna Close e passar para o novo dataset a media dos fechamentos dos candles no dia
    <br />
    <br />

        ultima_data = dados['Datetime'][-1:].values # 2019-01-07 22:06:00
        ultima_data = ultima_data[0]
        ultima_data = pd.to_datetime(ultima_data)
        ultima_data

        data_inicial =  pd.to_datetime('12-01-2014 00:00')
        dic_mes = {}
        while(data_inicial < ultima_data):    
            selecao = (dados['Datetime'] >= data_inicial) & (dados['Datetime'] < data_inicial + pd.DateOffset(1))
            aux = dados[selecao]

            dic_mes[data_inicial.date()] = aux['Close'].mean()    
            
            data_inicial = data_inicial + pd.DateOffset(1)

        dados_mes = pd.Series(dic_mes).to_frame('Close')
        dados_mes.dropna(subset=dados_mes.columns,inplace=True)
        dados_mes
    
    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img6.png?raw=true)

    * * *

    ##### Gráficos com DataSet em DIAS
        data_1 = pd.to_datetime('12-01-2014')
        data_2 = pd.to_datetime('12-01-2015')
        selecao = (dados_mes.index >= data_1  ) & (dados_mes.index <= data_2)
        df_mes = dados_mes[selecao]

        exp1=df_mes['Close'].ewm(span=5, adjust=False).mean()
        exp2=df_mes['Close'].ewm(span=20, adjust=False).mean()

        plt.plot(df_mes.index, df_mes['Close'], label='Fechamento')
        plt.plot(df_mes.index, exp1, label='exp 5')
        plt.plot(df_mes.index, exp2, label='exp 20')
        plt.legend(loc='upper left')
        plt.show()

    ![img](https://github.com/jeanhardzz/imagens_uteis/blob/main/img7.png?raw=true)        
    """        

    st.markdown(texto,unsafe_allow_html= True)   

       
    