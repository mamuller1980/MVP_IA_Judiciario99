import streamlit as st
from backend import processamento

st.set_page_config(page_title="MVP IA Judiciário", layout="wide")
st.title("MVP - Classificador Inteligente de Petições")

uploaded_file = st.file_uploader("Envie uma petição (formato .txt)", type="txt")

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.subheader("Texto da Petição")
    st.text_area("Conteúdo", text, height=300)
    
    st.subheader("Classificação com IA")
    resultado = processamento.classificar_peticao(text)
    st.markdown(f"**Tipo de Ação:** {resultado['tipo_acao']}")
    st.markdown(f"**Urgência:** {resultado['urgencia']}")
    st.markdown(f"**Resumo:** {resultado['resumo']}")
    
    st.subheader("Minuta Automática Sugerida")
    st.code(resultado['minuta'], language="markdown")

    st.success("Classificação simulada concluída.")