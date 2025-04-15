import streamlit as st
import fitz  # PyMuPDF
from nlp_spacy import extrair_entidades

st.set_page_config(page_title="IA para o Judiciário", layout="wide")

st.title("💼 Análise de Petições com IA")
st.markdown("Faça upload de uma petição em PDF para extrair e analisar entidades com NLP.")

uploaded_file = st.file_uploader("📄 Envie uma petição (PDF)", type=["pdf"])

def extrair_texto_pdf(file):
    texto = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            texto += page.get_text()
    return texto

if uploaded_file:
    texto = extrair_texto_pdf(uploaded_file)
    st.subheader("📝 Texto da Petição")
    st.write(texto[:2000] + "..." if len(texto) > 2000 else texto)

    entidades = extrair_entidades(texto)
    st.subheader("🔎 Entidades Reconhecidas com spaCy")
    if entidades:
        for entidade, label in entidades:
            st.markdown(f"- **{label}**: {entidade}")
    else:
        st.info("Nenhuma entidade encontrada no texto.")
