import requests
import pandas as pd
import urllib3

# Desativa avisos de segurança da Caixa
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def buscar_dados_oficiais():
    print("🚀 Conectando ao servidor da Caixa...")
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/"
    
    try:
        response = requests.get(url, verify=False, timeout=10)
        dados = response.json()
        
        concurso = dados['numero']
        dezenas = sorted([int(d) for d in dados['listaDezenas']])
        
        print(f"✅ Sucesso! Último concurso encontrado: {concurso}")
        return concurso, dezenas
    except Exception as e:
        print(f"❌ Erro ao buscar dados: {e}")
        return None, None

def atualizar_banco_de_dados(num, dezenas):
    df = pd.read_csv('sorteios.csv', sep=';')
    
    if num in df['concurso'].values:
        print(f"⚠️ O concurso {num} já está no seu arquivo. Nada a atualizar.")
    else:
        nova_linha = [num] + dezenas
        df.loc[len(df)] = nova_linha
        df.to_csv('sorteios.csv', sep=';', index=False)
        print(f"✨ Arquivo 'sorteios.csv' atualizado com sucesso!")

# Executa o processo
num_sorteio, lista_dezenas = buscar_dados_oficiais()
if num_sorteio:
    atualizar_banco_de_dados(num_sorteio, lista_dezenas)