import streamlit as st
import requests
import pandas as pd
import json

def predict_emprestimo(data):
    url = 'https://cute-marjorie-thalesh-20cc4b2da.koyeb.app/empresa/predict'
    header = {'Content-type': 'application/json'}
    data = json.dumps(data, to_dict(orient='records'))
    r = requests.post(url, data=data, headers=header)
    prediction = r.json()[0]['prediction']
    return prediction

st.set_page_config(
    layout='wide',
    page_title='Previsão de Inadimplência'
)

st.title('Previsão de Inadimplência')

col1, col2, col3, col4 = st.columns(4)

with col1:
    idade = st.number_input('Insira a Idade do Cliente')

with col2:
   renda = st.number_input('Insira a renda do Cliente')

with col3:
    tempo_emprego = st.number_input('Insira o tempo de emprego do Cliente')

with col4:
    valor_emprestimo = st.number_input('Insira o valor do empréstimo')   

col5, col6, col7, col8 = st.columns(4)   

with col5:
    taxa_juros_emprestimo = st.number_input('Insira a Taxa de Juros')

with col6:
    relacao_emprestimo_renda = st.number_input('Insira a relação empréstimo renda')

with col7:
     historico_credito = st.number_input('Insira o histórico de Crédito') 

with col8:
    posse_casa = st.selectbox('Insira o a posse da casa',(['RENT','OWR','MORTGAGE','OTHER']))

col9, col10, col11 = st.columns(3)

with col9:
    finalidade_emprestimo = st.selectbox('Insira a Finalidade do Empréstimo', (['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION']))

with col10:
    grau_risco_emprestimo = st.selectbox('Insira o Grau do Risco do Empréstimo', (['D', 'B', 'C', 'A', 'E', 'F', 'G']))

with col11:
    registro_inadimplencia = st.selectbox('Insira o registro de inadimplência',(['Y', 'N']))


dict_data = {
    'idade': int(idade),
    'renda': int(renda),
    'tempo_emprego': int(tempo_emprego),
    'valor_emprestimo': int(valor_emprestimo),
    'taxa_juros_emprestimo': float(taxa_juros_emprestimo),
    'relacao_emprestimo_renda': float(relacao_emprestimo_renda),
    'historico_credito': int(historico_credito),
    'posse_casa': posse_casa,
    'finalidade_emprestimo': finalidade_emprestimo,
    'registro_inadimplencia': registro_inadimplencia,
    'grau_risco_emprestimo': grau_risco_emprestimo
}

df = pd.DataFrame([dict_data])
data = json.dumps(df.to_dict(orient='records'))  

if st.button('Fazer Previsão'):
    with st.spinner('Nosso Modelo de Inteligencia Artificial esta analisando os dados....'):
        previsao = predict_emprestimo(data)
        if previsao !=0:
            st.markdown("<h4 style='color:red;'> Nosso modelo de Inteligencia Artificial recomenda nao disponibilizar credito para esse Cliente, pois ele possue uma alta problabilidade de nao pagar. </h4>",unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color:green;'> Nosso modelo de Inteligencia Artificial recomenda  disponibilizar credito para esse Cliente. </h4>",unsafe_allow_html=True)
    
