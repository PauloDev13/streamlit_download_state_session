import streamlit as st
import pandas as pd

st.set_page_config(page_title='Download and State Session', layout='centered')

with st.form('form_pessoa'):
    name = st.text_input('Nome')
    age = st.slider('Idade', 0, 120)
    ocupation = st.text_input('Cargo')

    if st.form_submit_button('Enviar dados'):
        if 'data' not in st.session_state:
            st.session_state['data'] = pd.DataFrame(columns=['nome', 'idade', 'cargo'])
        data = {'nome': name, 'idade': age, 'cargo': ocupation}
        df = pd.DataFrame(data, index=[0])
        st.session_state['data'] = pd.concat([st.session_state['data'], df], ignore_index=True)
        st.success('Dados cadastrado com sucesso!')

st.write('##### Lista de funcionários #####')
if 'data' in st.session_state:
    st.write(st.session_state['data'])
    st.session_state['data'] = {}

st.write('##### Download #####')
if 'data' in st.session_state:
    st.download_button(
        'Download',
        data=st.session_state.data.to_csv(),
        file_name='data.csv', mime='text/csv')