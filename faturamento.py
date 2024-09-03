import json

# Exemplo de dados em JSON (substitua com o seu JSON)
faturamento_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 15000},
        {"dia": 2, "valor": 20000},
        {"dia": 3, "valor": 25000},
        {"dia": 4, "valor": 30000}
        // Adicione os dados restantes
    ]
}
'''

# Remover o comentário do JSON
faturamento_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 15000},
        {"dia": 2, "valor": 20000},
        {"dia": 3, "valor": 25000},
        {"dia": 4, "valor": 30000}
    ]
}
'''

# Carregar os dados JSON
dados = json.loads(faturamento_json)

# Processar os dados
valores = [item['valor'] for item in dados['faturamento']]
media = sum(valores) / len(valores) if valores else 0
menor_valor = min(valores) if valores else 0
maior_valor = max(valores) if valores else 0
dias_acima_media = sum(1 for valor in valores if valor > media)

# Imprimir os resultados
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Número de dias acima da média: {dias_acima_media}")
