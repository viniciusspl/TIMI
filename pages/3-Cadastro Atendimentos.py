import streamlit as st 
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, nome_pai, nome_mae, terapias):
    if nome and data_nasc <= date.today():
        st.session_state["sucesso"] = True
        with open("clientes.csv","a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{nome_pai},{nome_mae},{terapias}\n")
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📄"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

dt_nasc = st.date_input("Data nascimento", format="DD/MM/YYYY")

nome_pai = st.text_input("Digite o nome do Pai")

nome_mae = st.text_input("Digite o nome da Mãe")

terapias = st.multiselect("Digite quais as terapias fazem parte da rotina da criança",
                          ["Psicologia", "Psicopedagogia", "Terapia Ocupacional", "Fonoaudiologia", "Fisioterapia"])

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, nome_pai, nome_mae, terapias])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cadastro realizado com sucesso!",
                   icon="✔")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")
        
data = {
    'Nome': ["nome"],
    'Data de Nascimento': ["dt_nasc"],
    'Nome do Pai': ["nome_pai"],
    'Nome da Mãe': ["nome_mae"],
    'Contato': ["tel_resp"],
    'Terapias': ["terapias"],
}
