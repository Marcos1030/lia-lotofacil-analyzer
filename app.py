import streamlit as st
import pandas as pd
import random
import urllib3

# Configuração da Página
st.set_page_config(page_title="LIA - Lotofácil Analyzer", page_icon="🤖")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

st.title("🤖 LIA - Lotofácil Intelligence Analyzer")
st.markdown("---")

# 1. Carregar Dados
try:
    df = pd.read_csv('sorteios.csv', sep=';')
    colunas_bolas = [f'bola{n}' for n in range(1, 16)]
    ultimo_sorteio = set(df.iloc[-1][colunas_bolas].values)
    num_concurso = df.iloc[-1]['concurso']
    
    st.sidebar.header("📊 Status do Sistema")
    st.sidebar.success(f"Base de dados: Concurso {num_concurso}")
except:
    st.error("Erro ao carregar sorteios.csv. Verifique se o arquivo existe.")

# 2. Lógica do Gerador
def gerar_jogo_inteligente(base_anterior):
    primos_lista = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    while True:
        jogo = sorted(random.sample(range(1, 26), 15))
        soma, pares = sum(jogo), len([n for n in jogo if n % 2 == 0])
        primos = len([n for n in jogo if n in primos_lista])
        repetidos = len(set(jogo).intersection(base_anterior))
        
        if (180 <= soma <= 220) and (pares in [7, 8, 9]) and (primos in [5, 6]) and (repetidos in [8, 9, 10]):
            return jogo, soma, pares, repetidos

# 3. Interface do Usuário
st.subheader("🎲 Gerar Sugestões Inteligentes")
quantidade = st.slider("Quantos jogos deseja gerar?", 1, 10, 5)

if st.button("Gerar Jogos Agora 🚀"):
    col1, col2 = st.columns(2)
    for i in range(quantidade):
        jogo, s, p, r = gerar_jogo_inteligente(ultimo_sorteio)
        with st.expander(f"Sugestão {i+1}: {str(jogo)}"):
            st.write(f"**Soma:** {s} | **Pares:** {p} | **Repetidos:** {r}")

st.markdown("---")
if st.checkbox("Mostrar histórico de sorteios"):
    st.dataframe(df.tail(10)) # Mostra os últimos 10
   # 4. Análise Visual (Gráfico Interativo)
st.markdown("---")
st.subheader("📈 Análise de Frequência Dinâmica")

# Slider para escolher a quantidade de sorteios
quantidade = st.slider("Selecione quantos sorteios analisar:", 5, len(df), 15)

# Filtrando os últimos 'n' sorteios
base_filtrada = df.tail(quantidade)
todos_numeros_filtrados = base_filtrada[colunas_bolas].values.flatten()
frequencia = pd.Series(todos_numeros_filtrados).value_counts().sort_index()

# Exibindo o gráfico atualizado
st.bar_chart(frequencia)

st.info(f"💡 Analisando os números dos últimos {quantidade} concursos.")