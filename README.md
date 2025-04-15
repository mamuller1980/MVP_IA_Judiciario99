
# MVP - IA para o Judiciário Brasileiro

Este projeto é um MVP (Produto Mínimo Viável) de uma solução de inteligência artificial para o Poder Judiciário. Ele classifica petições automaticamente, identifica urgência e sugere minutas judiciais com base no tipo da ação.

## Funcionalidades

- Classificação automática de petições judiciais (simulada)
- Identificação do nível de urgência
- Geração de minuta inicial com base na classificação
- Interface simples com Streamlit

## Estrutura

```
MVP_IA_Judiciario/
├── frontend/
│   └── app.py
├── backend/
│   └── processamento.py
├── sample_data/
│   └── peticao_exemplo.txt
├── requirements.txt
└── README.md
```

## Como rodar localmente

1. Instale o Streamlit:
```
pip install streamlit
```

2. Execute o app:
```
streamlit run frontend/app.py
```

## Como publicar no Streamlit Cloud

1. Crie um repositório no GitHub e envie esses arquivos
2. Acesse [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Conecte sua conta GitHub
4. Clique em “New app” e selecione o repositório
5. Caminho do script: `frontend/app.py`
6. Clique em “Deploy”

Pronto! Seu MVP estará online com um link público para demonstração.
