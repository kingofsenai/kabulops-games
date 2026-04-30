import streamlit as st
import time
import json
import os

# 1. CONFIGURAÇÃO (Sempre o primeiro)
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# 2. SISTEMA DE ARQUIVOS (Definições)
DB_FILE = "database_kabulops.json"

def carregar_dados():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            data["usuarios"] = set(data["usuarios"])
            return data
    return {"total": 0, "votos": {}, "usuarios": set()}

def salvar_dados(dados):
    dados_para_salvar = dados.copy()
    dados_para_salvar["usuarios"] = list(dados_para_salvar["usuarios"])
    with open(DB_FILE, "w") as f:
        json.dump(dados_para_salvar, f, indent=4)

# 3. LÓGICA DE RANKING (Defina a função ANTES de usar)
def get_top_3():
    # Se não houver votos ainda, retornamos lista vazia para evitar erro
    if "votos" not in db or not db["votos"]:
        return []
    return sorted(db["votos"].items(), key=lambda x: x[1], reverse=True)[:3]

# 4. INICIALIZAÇÃO DO BANCO (Onde o 'db' nasce)
if "db" not in st.session_state:
    st.session_state.db = carregar_dados()

db = st.session_state.db

# 5. BIBLIOTECA (A lista gigante de 50 personagens que te passei)
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # ... (cole aqui os 50 personagens da lista anterior)
    ]

# 6. INTERFACE - BARRA LATERAL (Agora ela pode chamar o get_top_3 com segurança)
with st.sidebar:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=50)
    st.title("Kabulops Games")
    st.markdown("---")
    
    st.subheader("📊 Placar")
    st.metric("Players Online", db["total"])
    
    ranking = get_top_3() # <--- AGORA O INIMIGO FOI DERROTADO AQUI
    if ranking:
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, qtd) in enumerate(ranking):
            st.markdown(f"{medals[i]} {jogo} ({qtd})")

# 7. CONTEÚDO PRINCIPAL (O restante do código de Login e Enquete)
# ...
