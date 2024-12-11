import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import date

dados = pd.read_csv("clientes.csv")

st.title("Clientes cadastrados")
st.divider()

st.dataframe(dados)


# Exemplo de dados

data = {
    'Nome': ["nome"],
    'Data de Nascimento': ["dt_nasc"],
    'Nome do Pai': ["nome_pai"],
    'Nome da Mãe': ["nome_mae"],
    'Contato': ["tel_resp"],
    'Terapias': ["terapias"],
}

df = pd.DataFrame(dados)

# Função para converter DataFrame para um arquivo Excel formatado
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Formatação (opcional)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for column in worksheet.columns:
        for cell in column:
            cell.alignment = cell.alignment.copy(horizontal='center', vertical='center')
            cell.font = cell.font.copy(bold=True)
    
    writer.save()
    processed_data = output.getvalue()
    return processed_data

st.title("Clientes Cadastrados")

# Exibe o DataFrame no Streamlit
st.write(df)

# Cria o botão para download
if st.button('Baixar Excel'):
    excel_data = to_excel(df)
    st.download_button(label='Clique aqui para baixar',
                       data=excel_data,
                       file_name='clientes_cadastrados.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    