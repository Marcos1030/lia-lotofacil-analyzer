import pandas as pd

# 1. Carregar os dados do arquivo CSV que você criou
# Usamos sep=';' porque os dados estão separados por ponto e vírgula
df = pd.read_csv('sorteios.csv', sep=';')

print("--- LIA: Analisando Histórico ---")

# 2. Função para analisar cada linha (cada concurso)
def analisar_linha(linha):
    # Pegamos as bolas de 1 a 15
    colunas_bolas = [f'bola{n}' for n in range(1, 16)]
    numeros = linha[colunas_bolas]
    
    soma = numeros.sum()
    pares = len([n for n in numeros if n % 2 == 0])
    impares = 15 - pares
    
    return pd.Series([soma, pares, impares], index=['Soma', 'Pares', 'Impares'])

# 3. Aplicar a lógica em todas as linhas da planilha
analise = df.apply(analisar_linha, axis=1)
resultado_final = pd.concat([df['concurso'], analise], axis=1)

# 4. Mostrar o resultado final na tela
print(resultado_final.to_string(index=False))

# 5. Resumo estatístico
print("\n--- RESUMO DO HISTÓRICO ---")
print(f"Média de Soma: {resultado_final['Soma'].mean():.2f}")
print(f"Padrão mais comum de Pares: {resultado_final['Pares'].mode()[0]}")
import random

def gerar_jogo_inteligente():
    while True:
        # Gera 15 números aleatórios entre 1 e 25
        jogo = sorted(random.sample(range(1, 26), 15))
        soma = sum(jogo)
        pares = len([n for n in jogo if n % 2 == 0])
        
        # FILTROS: Só aceita o jogo se a soma for entre 180 e 220
        # E se tiver entre 7 e 8 pares (os padrões que mais saem)
        if 180 <= soma <= 220 and pares in [7, 8]:
            return jogo, soma, pares

print("\n--- SUGESTÕES DE JOGOS (FILTRADOS) ---")
for i in range(1, 6):
    jogo, s, p = gerar_jogo_inteligente()
    print(f"Sugestão {i}: {jogo} | Soma: {s} | Pares: {p}")