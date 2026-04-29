import streamlit as st  # O IMPORT PRECISA SER A PRIMEIRA LINHA!
import time
import json
import os

# --- CONFIGURAÇÃO DE ALTA PERFORMANCE ---
st.set_page_config(
    page_title="Kabulops Games", 
    page_icon="🎮", 
    layout="centered"
)

# --- SISTEMA DE ARQUIVOS (PERMANÊNCIA) ---
DB_FILE = "database_kabulops.json"

def carregar_dados():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            # JSON não salva sets, então convertemos de volta
            data["usuarios"] = set(data["usuarios"])
            return data
    return {"total": 0, "votos": {}, "usuarios": set()}

def salvar_dados(dados):
    # Convertemos set para lista para o JSON aceitar
    dados_para_salvar = dados.copy()
    dados_para_salvar["usuarios"] = list(dados_para_salvar["usuarios"])
    with open(DB_FILE, "w") as f:
        json.dump(dados_para_salvar, f, indent=4)

# Substituímos o cache_resource pela carga do arquivo
if "db" not in st.session_state:
    st.session_state.db = carregar_dados()

db = st.session_state.db

# --- BIBLIOTECA DE PERSONAGENS (EXPANDIDA) ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # ... (seu conteúdo da biblioteca permanece exatamente o mesmo aqui)
        {"nome": "Suicune", "jogo": "Pokémon Crystal", "papel": "Lendário", "golpe": "Aurora Beam"},
        {"nome": "Link", "jogo": "Zelda: Oracle of Ages", "papel": "Herói", "golpe": "Harp of Ages"},
        {"nome": "Shantae", "jogo": "Shantae", "papel": "Meio-Gênio", "golpe": "Dança da Transformação"},
        {"nome": "Alis Landale", "jogo": "Phantasy Star", "papel": "Protagonista", "golpe": "Espada de Luz"},
        {"nome": "Alex Kidd", "jogo": "Alex Kidd", "papel": "Mascote", "golpe": "Soco Janken"},
        {"nome": "Chrono", "jogo": "Chrono Trigger", "papel": "Herói", "golpe": "Luminaire"},
        {"nome": "Mega Man X", "jogo": "Mega Man X", "papel": "Hunter", "golpe": "X-Buster"},
        {"nome": "Donkey Kong", "jogo": "Donkey Kong Country", "papel": "Líder", "golpe": "Ground Pound"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Velocidade", "golpe": "Spin Dash"},
        {"nome": "Axel Stone", "jogo": "Streets of Rage", "papel": "Lutador", "golpe": "Grand Upper"},
        {"nome": "Lute", "jogo": "Lunar: Silver Star", "papel": "Bardo", "golpe": "Canção de Cura"},
        {"nome": "Nights", "jogo": "Nights into Dreams", "papel": "Espírito", "golpe": "Paraloop"},
        {"nome": "Solid Snake", "jogo": "Metal Gear Solid", "papel": "Espião", "golpe": "Stealth Camouflage"},
        {"nome": "Cloud Strife", "jogo": "Final Fantasy VII", "papel": "Mercenário", "golpe": "Omnislash"},
        {"nome": "Leon Kennedy", "jogo": "Resident Evil 2", "papel": "Policial", "golpe": "Tiro Preciso"},
        {"nome": "Mario", "jogo": "Super Mario 64", "papel": "Herói", "golpe": "Triplo Pulo"},
        {"nome": "James Bond", "jogo": "GoldenEye 007", "papel": "Agente", "golpe": "PP7 Silenciada"},
        {"nome": "Banjo", "jogo": "Banjo-Kazooie", "papel": "Urso", "golpe": "Beak Buster"}
    ]

# --- LÓGICA DE RANKING ---
def get_top_3():
    return sorted(db["votos"].items(), key=lambda x: x[1], reverse=True)[:3]

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=50)
    st.title("Kabulops Games")
    st.markdown("---")
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png", width=50)
    st.markdown("#### **Participe da Pesquisa**")
    st.markdown("---")
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png", width=50)
    st.markdown("#### **Seja um Kabuloso**\n*Inscreva-se*")
    st.markdown("---")

    st.subheader("📊 Placar")
    st.metric("Players Online", db["total"])
    
    ranking = get_top_3()
    if ranking:
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, qtd) in enumerate(ranking):
            st.markdown(f"{medals[i]} {jogo} ({qtd})")

# --- CONTEÚDO PRINCIPAL ---
st.image("https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png")

if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    nick = st.text_input("Digite seu Nick para entrar:", key="login_input")
    if st.button("PRESS START"):
        if nick:
            st.session_state.user = nick
            if nick not in db["usuarios"]:
                db["total"] += 1
                db["usuarios"].add(nick)
                salvar_dados(db) # SALVA A ENTRADA DO NOVO USUÁRIO
            st.rerun()
else:
    st.write(f"### Bem-vindo, **{st.session_state.user}**!")
    
    # ENQUETE EXPANDIDA
    st.header("🗳️ Qual Live você quer ver?")
    opcoes_consoles = [
        "Pokémon Crystal (GBC)", "Phantasy Star (Master)", "Chrono Trigger (SNES)", 
        "Sonic CD (Sega CD)", "Nights into Dreams (Saturn)", "Metal Gear Solid (PS1)",
        "GoldenEye 007 (N64)", "Streets of Rage 2 (Mega Drive)"
    ]
    voto = st.selectbox("Escolha seu jogo favorito:", sorted(opcoes_consoles))
    
    if st.button("Confirmar Voto"):
        db["votos"][voto] = db["votos"].get(voto, 0) + 1
        salvar_dados(db) # SALVA O VOTO PERMANENTEMENTE
        st.balloons()
        st.success(f"Voto para {voto} registrado!")
        time.sleep(0.5)
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
                    st.write(f"**Golpe:** {r['golpe']}")
        else:
            st.warning("Personagem ainda não cadastrado.")
