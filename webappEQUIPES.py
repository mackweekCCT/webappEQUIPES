# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import plotly.graph_objects as go

import altair as alt
from urllib.error import URLError

#DÚVIDAS
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRtt6VlUfp77JA2ok1dUAN5WMj3NNKCliMyG6Tb7Yu8MzUzQ5lZXjcNOWMgit6VaJw8W8lPIzjjnWVn/pub?gid=51090662&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
NregD = len(dfD)
dfD.columns = ['email', 'equipe', 'nome', 'duvida', 'obs']
selecao01D = dfD['equipe']=='Equipe 01'
df01D = dfD[selecao01D]
selecao02D = dfD['equipe']=='Equipe 02'
df02D = dfD[selecao02D]
selecao03D = dfD['equipe']=='Equipe 03'
df03D = dfD[selecao03D]
selecao04D = dfD['equipe']=='Equipe 04'
df04D = dfD[selecao04D]
selecao05D = dfD['equipe']=='Equipe 05'
df05D = dfD[selecao05D]
selecao06D = dfD['equipe']=='Equipe 06'
df06D = dfD[selecao06D]
selecao07D = dfD['equipe']=='Equipe 07'
df07D = dfD[selecao07D]
selecao08D = dfD['equipe']=='Equipe 08'
df08D = dfD[selecao08D]
selecao09D = dfD['equipe']=='Equipe 09'
df09D = dfD[selecao09D]
selecao10D = dfD['equipe']=='Equipe 10'
df10D = dfD[selecao10D]
selecao11D = dfD['equipe']=='Equipe 11'
df11D = dfD[selecao11D]

#RESPOSTAS
rR = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQw6XD9vI_C4zvZ6W51vut_Ze_D_OSESuXiHh1IAXeBFXRRvyQ7kyFTLbGip1obadjbZHUmaAxvXmnz/pub?gid=1789345467&single=true&output=csv')
dataR = rR.content
dfR = pd.read_csv(BytesIO(dataR), index_col=0)
NregR = len(dfR)
dfR.columns = ['email', 'equipe', 'nome', 'resposta', 'sugestao']
selecao01R = dfR['equipe']=='Equipe 01'
df01R = dfR[selecao01R]
selecao02R = dfR['equipe']=='Equipe 02'
df02R = dfR[selecao02R]
selecao03R = dfR['equipe']=='Equipe 03'
df03R = dfR[selecao03R]
selecao04R = dfR['equipe']=='Equipe 04'
df04R = dfR[selecao04R]
selecao05R = dfR['equipe']=='Equipe 05'
df05R = dfR[selecao05R]
selecao06R = dfR['equipe']=='Equipe 06'
df06R = dfR[selecao06R]
selecao07R = dfR['equipe']=='Equipe 07'
df07R = dfR[selecao07R]
selecao08R = dfR['equipe']=='Equipe 08'
df08R = dfR[selecao08R]
selecao09R = dfR['equipe']=='Equipe 09'
df09R = dfR[selecao09R]
selecao10R = dfR['equipe']=='Equipe 10'
df10R = dfR[selecao10R]
selecao11R = dfR['equipe']=='Equipe 11'
df11R = dfR[selecao11R]

image01 = Image.open('ImagemLateral.jpg')
st.sidebar.image(image01, width=300, caption='Mack Week CCT 2022') 
st.title("DASHBOARD - EQUIPES")
# st.header("Cabeçalho")
#st.subheader("Sub Cabeçalho")
#st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
menu = ["Dúvidas",
        "Respostas",
        "Dúvidas e Respostas",
        "EQUIPE 01"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.info("By: Prof. Massaki de O. Igarashi")

if choice == "Dúvidas": 
    st.header("Painel Analítico: DÚVIDAS")   
    st.write('EQUIPE 01:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df01D['duvida']) 
    st.write('EQUIPE 02:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df02D['duvida']) 
    st.write('EQUIPE 03:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df03D['duvida']) 
    st.write('EQUIPE 04:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df04D['duvida']) 
    st.write('EQUIPE 05:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df05D['duvida']) 
    st.write('EQUIPE 06:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df06D['duvida'])
    st.write('EQUIPE 07:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df07D['duvida']) 
    st.write('EQUIPE 08:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df08D['duvida']) 
    st.write('EQUIPE 09:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df09D['duvida']) 
    st.write('EQUIPE 10:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
    st.write('EQUIPE 11:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df11D['duvida']) 
        
elif choice == "Respostas":       
    st.header("Painel Analítico: RESPOSTAS")    
    st.write('EQUIPE 01:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df01R['resposta'])  
    st.write('EQUIPE 02:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df02R['resposta'])  
    st.write('EQUIPE 03:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df03R['resposta'])  
    st.write('EQUIPE 04:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df04R['resposta'])      
    st.write('EQUIPE 05:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df05R['resposta'])  
    st.write('EQUIPE 06:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df06R['resposta'])  
    st.write('EQUIPE 07:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df07R['resposta'])  
    st.write('EQUIPE 08:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df08R['resposta'])  
    st.write('EQUIPE 09:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df09R['resposta'])  
    st.write('EQUIPE 10:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta'])  
    st.write('EQUIPE 11:')    
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df11R['resposta'])  
               
elif choice == "Dúvidas e Respostas":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    #EQUIPE 01
    st.write('EQUIPE 01:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df01D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df01R['resposta'])  
    #EQUIPE 02
    st.write('EQUIPE 02:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df02D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df02R['resposta'])     
    #EQUIPE 03
    st.write('EQUIPE 03:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df03D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df03R['resposta']) 
    #EQUIPE 04
    st.write('EQUIPE 04:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df04D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df04R['resposta']) 
    #EQUIPE 05
    st.write('EQUIPE 05:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df05D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df05R['resposta'])    
    #EQUIPE 06
    st.write('EQUIPE 06:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df06D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df06R['resposta'])  
    #EQUIPE 07
    st.write('EQUIPE 07:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df07D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df07R['resposta'])     
    #EQUIPE 08
    st.write('EQUIPE 08:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df08D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df08R['resposta']) 
    #EQUIPE 09
    st.write('EQUIPE 09:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df09D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df09R['resposta']) 
    #EQUIPE 10
    st.write('EQUIPE 10:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta']) 
    #EQUIPE 11
    st.write('EQUIPE 11:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df11D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df11R['resposta']) 

elif choice == "EQUIPE 01":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    col1, col2 = st.columns((1,1))
    with col1:
        st.write("Nº de Dúvidas:")
        st.warning(NregD)
    with col2:
        st.write("Nº de dúvidas RESPONDIDAS:")
        st.info(NregR)
    st.write('EQUIPE 01:')
    st.info('Dúvida(s) Enviada(s)')
    st.code(df01D['duvida']) 
    st.warning('Resposta do(a) TUTOR(A):')
    st.code(df01R['resposta']) 

elif choice == "Texto_Markdown":
    st.subheader("Texto Markdown")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )

#st.image(image01, width=800, caption='Rótulo da Imagem 01') 
#st.subheader("**Desenvolvido pelo Professor Massaki de O. Igarashi** ")
