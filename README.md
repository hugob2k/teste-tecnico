# Teste Técnico

Este repositório contém soluções para um teste tecnico que decidir fazer em Python. Cada exercício resolve um problema específico e demonstra conceitos-chave de programação. Abaixo está a descrição de cada exercício:

## Exercício 1: Cálculo de Soma
Este programa calcula a soma dos inteiros de 1 até um valor de índice predefinido usando um loop.

### Descrição do Código:
- Utiliza um loop `while` para iterar de 1 até o índice.
- Calcula a soma acumulada.
- Exibe o resultado.

## Exercício 2: Verificador de Sequência de Fibonacci
Este programa verifica se um número informado pertence à sequência de Fibonacci.

### Descrição do Código:
- Recebe um número como entrada do usuário.
- Calcula iterativamente a sequência de Fibonacci.
- Verifica se o número está presente na sequência e exibe o resultado.

## Exercício 3: Análise de Faturamento Diário
Este programa analisa dados de faturamento diário armazenados em um arquivo JSON e fornece:
- O menor valor de faturamento.
- O maior valor de faturamento.
- O número de dias com faturamento acima da média mensal.

### Descrição do Código:
- Lê os dados do arquivo `faturamento.json`.
- Filtra os dias com faturamento maior que zero.
- Calcula as métricas necessárias e exibe os resultados.

## Exercício 4: Representação de Faturamento por Estado
Este programa calcula a representação percentual do faturamento de diferentes estados em relação ao faturamento total.

### Descrição do Código:
- Armazena os dados de faturamento por estado em um dicionário.
- Calcula o faturamento total.
- Determina e exibe a contribuição percentual de cada estado.

## Exercício 5: Inversão de String
Este programa inverte uma string fornecida sem utilizar funções prontas de reversão.

### Descrição do Código:
- Recebe uma string como entrada do usuário.
- Usa um loop para inverter a string.
- Exibe a string invertida.

## Pré-requisitos
- Python 3.x
- Arquivo JSON (`faturamento.json`) para o Exercício 3.

## Como Executar
1. Clone este repositório.
2. Certifique-se de que o Python 3.x está instalado no seu sistema.
3. Coloque o arquivo `faturamento.json` no mesmo diretório que os scripts.
4. Execute o script com o comando:
   ```bash
   python nome_do_script.py
   ```
5. Siga as instruções para os exercícios que requerem entrada do usuário.

## Exemplo de Arquivo JSON
Certifique-se de que o arquivo `faturamento.json` possui a seguinte estrutura para o Exercício 3:

```json
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0}
]
```

## Contato
Para dúvidas ou problemas, fique à vontade para abrir uma issue ou entrar em contato diretamente.
