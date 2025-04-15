import spacy

# Carrega o modelo português grande
nlp = spacy.load("pt_core_news_lg")

def extrair_entidades(texto):
    doc = nlp(texto)
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return entidades
