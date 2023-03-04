import json

# Carrega os dados do faturamento mensal a partir de um arquivo JSON
with open('faturamento.json') as f:
    faturamento = json.load(f)

# Remove os valores de faturamento para dias sem registro
faturamento = [valor for valor in faturamento if valor != None]

# Calcula o menor e o maior valor de faturamento ocorrido em um dia do mês
menor_valor = min(dia['valor'] for dia in faturamento)
maior_valor = max(dia['valor'] for dia in faturamento)

# Cria uma lista de valores de faturamento diário
valores_faturamento = [dia['valor'] for dia in faturamento]

# Calcula a média apenas dos valores de faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Conta o número de dias em que o faturamento foi maior que a média
dias_acima_da_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

# Imprime os resultados
print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média:", dias_acima_da_media)
