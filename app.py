import streamlit as st
import fitz  # PyMuPDF
from backend import processamento

st.set_page_config(page_title="MVP IA Judiciário", layout="wide")
st.title("MVP - Classificador Inteligente de Petições")

uploaded_file = st.file_uploader("Envie uma petição (.pdf ou .txt)", type=["txt", "pdf"])

def extrair_texto_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    texto = ""
    for page in doc:
        texto += page.get_text()
    return texto

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extrair_texto_pdf(uploaded_file)
    else:
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
