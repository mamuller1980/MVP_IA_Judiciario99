import spacy
import os

def carregar_modelo():
    try:
        return spacy.load("pt_core_news_lg")
    except OSError:
        from spacy.cli import download
        download("pt_core_news_lg")
        return spacy.load("pt_core_news_lg")

nlp = carregar_modelo()

def extrair_entidades(texto):
    doc = nlp(texto)
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return entidades
