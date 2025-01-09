# Exercício 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"Valor de SOMA: {SOMA}")

# Exercício 2
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# Exercício 3
import json

# Abrir e carregar o arquivo JSON que foi enviado para o email
with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

# Filtrar os valores de faturamento válidos (maiores que 0)
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcular os resultados
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for dia in valores if dia > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Exercício 4
def calcula_percentual():
    estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = sum(estados.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in estados.items()}

    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

calcula_percentual()

# Exercício 5
def inverte_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

string = input("Informe uma string para ser invertida: ")
print(f"String invertida: {inverte_string(string)}")