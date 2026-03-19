import pandas as pd
import random

# 1. Carregar os dados
df = pd.read_csv('sorteios.csv', sep=';')

print("--- LIA: Analisando Histórico ---")

def analisar_linha(linha):
    colunas_bolas = [f'bola{n}' for n in range(1, 16)]
    numeros = linha[colunas_bolas]
    soma = numeros.sum()
    pares = len([n for n in numeros if n % 2 == 0])
    impares = 15 - pares
    return pd.Series([soma, pares, impares], index=['Soma', 'Pares', 'Impares'])

analise = df.apply(analisar_linha, axis=1)
resultado_final = pd.concat([df['concurso'], analise], axis=1)
print(resultado_final.to_string(index=False))

# 2. Gerador de Jogos com Filtros Estatísticos
def gerar_jogo_inteligente():
    primos_lista = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    
    while True:
        jogo = sorted(random.sample(range(1, 26), 15))
        soma = sum(jogo)
        pares = len([n for n in jogo if n % 2 == 0])
        primos_no_jogo = len([n for n in jogo if n in primos_lista])
        
        # Filtros baseados em tendências reais
        f_soma = 180 <= soma <= 220
        f_pares = pares in [7, 8]
        f_primos = primos_no_jogo in [5, 6]

        if f_soma and f_pares and f_primos:
            return jogo, soma, pares, primos_no_jogo

print("\n--- SUGESTÕES DE JOGOS (SOMA + PARES + PRIMOS) ---")
for i in range(1, 6):
    jogo, s, p, pr = gerar_jogo_inteligente()
    print(f"Sugestão {i}: {jogo} | Soma: {s} | Pares: {p} | Primos: {pr}")