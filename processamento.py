import random

TIPOS_ACAO = [
    "Indenização por Danos Morais",
    "Ação de Alimentos",
    "Revisional de Contrato",
    "Cobrança Indevida",
    "Ação Possessória"
]

MINUTAS = {
    "Indenização por Danos Morais": "Vistos, etc. Defiro a inicial. Cite-se o réu. Intime-se.",
    "Ação de Alimentos": "Defiro alimentos provisórios no valor de 30% do salário mínimo. Designo audiência.",
    "Revisional de Contrato": "Determino a apresentação do contrato pelo banco. Vista ao autor para réplica.",
    "Cobrança Indevida": "Concedo liminar para suspensão da cobrança. Oficie-se à instituição financeira.",
    "Ação Possessória": "Defiro liminar de reintegração de posse. Cumpra-se com urgência."
}

def classificar_peticao(texto):
    tipo_acao = random.choice(TIPOS_ACAO)
    urgencia = random.choice(["Baixa", "Média", "Alta"])
    resumo = f"Simulação: texto indica uma ação do tipo '{tipo_acao}' com urgência {urgencia.lower()}."
    minuta = MINUTAS[tipo_acao]
    return {
        "tipo_acao": tipo_acao,
        "urgencia": urgencia,
        "resumo": resumo,
        "minuta": minuta
    }