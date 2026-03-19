import pandas as pd
import random

# 1. Carregar os dados
df = pd.read_csv('sorteios.csv', sep=';')

# Pegar o último sorteio para usar como base de repetição
colunas_bolas = [f'bola{n}' for n in range(1, 16)]
ultimo_sorteio = set(df.iloc[-1][colunas_bolas].values)

print(f"--- LIA: Analisando Histórico (Baseado no concurso {df.iloc[-1]['concurso']}) ---")

# 2. Gerador de Jogos com Filtro de Repetição
def gerar_jogo_inteligente(base_anterior):
    primos_lista = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    
    while True:
        jogo = sorted(random.sample(range(1, 26), 15))
        soma = sum(jogo)
        pares = len([n for n in jogo if n % 2 == 0])
        primos = len([n for n in jogo if n in primos_lista])
        
        # FILTRO NOVO: Quantos números do jogo atual estavam no sorteio anterior?
        repetidos = len(set(jogo).intersection(base_anterior))
        
        # REGRAS ESTATÍSTICAS
        f_soma = 180 <= soma <= 220
        f_pares = pares in [7, 8, 9]
        f_primos = primos in [5, 6]
        f_repetidos = repetidos in [8, 9, 10] # A regra de ouro!

        if f_soma and f_pares and f_primos and f_repetidos:
            return jogo, soma, pares, repetidos

print("\n--- SUGESTÕES COM FILTRO DE REPETIÇÃO (8 a 10 do anterior) ---")
for i in range(1, 6):
    jogo, s, p, r = gerar_jogo_inteligente(ultimo_sorteio)
    print(f"Sugestão {i}: {jogo} | Soma: {s} | Pares: {p} | Repetidos: {r}")