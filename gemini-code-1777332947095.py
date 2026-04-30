import streamlit as st
import time
import json
import os

# --- 1. CONFIGURAÇÃO (Sempre a primeira linha) ---
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# --- 2. SISTEMA DE DADOS ---
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

if "db" not in st.session_state:
    st.session_state.db = carregar_dados()

db = st.session_state.db

def get_top_3():
    if not db["votos"]:
        return []
    return sorted(db["votos"].items(), key=lambda x: x[1], reverse=True)[:3]

# --- 3. BIBLIOTECA (Os 50 personagens) ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # --- BIBLIOTECA DE PERSONAGENS (COMPLETA - 62 REGISTROS) ---
@st.cache_data
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        {"nome": "Suicune", "jogo": "Pokémon Crystal (GBC)", "papel": "Lendário", "golpe": "Aurora Beam / Hydro Pump"},
        {"nome": "Eusine", "jogo": "Pokémon Crystal (GBC)", "papel": "Treinador", "golpe": "Dream Eater / Mean Look"},
        # ... (todos os outros personagens ficam aqui no meio) ...
        {"nome": "Kyo Kusanagi", "jogo": "King of Fighters", "papel": "Lutador", "golpe": "Orochinagi / 100 Shiki"},
        {"nome": "Shinobi", "jogo": "The Revenge of Shinobi", "papel": "Ninja", "golpe": "Shuriken Throw / Mijin Jutsu"}
    ] # <--- ESTE COLCHETE É O QUE ESTÁ FALTANDO!

# --- 4. BARRA LATERAL (Com as 5 Pokébolas) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=40)
    st.title("Kabulops Games")
    st.markdown("---")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png", width=40)
    st.markdown("#### **Pesquisa de Lives**")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png", width=40)
    st.markdown("#### **Seja um Kabuloso**")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/great-ball.png", width=40)
    st.markdown("#### **Biblioteca Retro**")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png", width=40)
    st.markdown("#### **Configurações**")
    st.markdown("---")

    st.subheader("📊 Placar")
    st.metric("Players Online", db["total"])
    
    ranking = get_top_3()
    if ranking:
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, qtd) in enumerate(ranking):
            st.markdown(f"{medals[i]} {jogo} ({qtd})")

# --- 5. CONTEÚDO PRINCIPAL ---
st.image("https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png")

if 'user' not in st.session_state:
    st.session_state.user = None

# TELA DE LOGIN
if not st.session_state.user:
    nick = st.text_input("Digite seu Nick para entrar:", key="login_input")
    if st.button("PRESS START"):
        if nick:
            st.session_state.user = nick
            if nick not in db["usuarios"]:
                db["total"] += 1
                db["usuarios"].add(nick)
                salvar_dados(db)
            st.rerun()

# TELA PÓS-LOGIN (O que o usuário vê logado)
else:
    st.write(f"### Bem-vindo, **{st.session_state.user}**!")
    
    # ENQUETE
    st.header("🗳️ Qual Live você quer ver?")
    opcoes_consoles = [
        "Pokémon Crystal (GBC)", "Phantasy Star (Master)", "Chrono Trigger (SNES)", 
        "Sonic CD (Sega CD)", "Nights into Dreams (Saturn)", "Metal Gear Solid (PS1)",
        "GoldenEye 007 (N64)", "Streets of Rage 2 (Mega Drive)"
    ]
    voto = st.selectbox("Escolha seu jogo favorito:", sorted(opcoes_consoles))
    
    if st.button("Confirmar Voto"):
        db["votos"][voto] = db["votos"].get(voto, 0) + 1
        salvar_dados(db)
        st.balloons()
        st.success(f"Voto para {voto} registrado!")
        time.sleep(1)
        st.rerun()

    st.markdown("---")

    # BIBLIOTECA
    st.header("📖 Biblioteca de Personagens")
    termo = st.text_input("Busque personagens ou consoles:").lower()
    
    biblioteca = carregar_biblioteca_estatica()
    if termo:
        resultados = [p for p in biblioteca if termo in p['nome'].lower() or termo in p['jogo'].lower()]
        if resultados:
            for r in resultados:
                with st.expander(f"🔹 {r['nome']} - {r['jogo']}"):
                    st.write(f"**Papel:** {r['papel']}")
                    st.write(f"**Golpes:** {r['golpe']}")
        else:
            st.warning("Nenhum personagem encontrado com esse termo.")
    else:
        st.info("Digite o nome de um personagem ou console para pesquisar na biblioteca.")
