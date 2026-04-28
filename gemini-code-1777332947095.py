import streamlit as st  # O IMPORT PRECISA SER A PRIMEIRA LINHA!
import time

# --- CONFIGURAÇÃO DE ALTA PERFORMANCE ---
st.set_page_config(
    page_title="Kabulops Games", 
    page_icon="🎮", 
    layout="centered"
)

# --- BANCO DE DADOS GLOBAL ---
@st.cache_resource
def banco_de_dados():
    # Iniciamos com os dados básicos
    return {"total": 0, "votos": {}, "usuarios": set()}

db = banco_de_dados()

# --- BIBLIOTECA DE PERSONAGENS (EXPANDIDA) ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # --- GAME BOY COLOR ---
        {"nome": "Suicune", "jogo": "Pokémon Crystal", "papel": "Lendário", "golpe": "Aurora Beam"},
        {"nome": "Link", "jogo": "Zelda: Oracle of Ages", "papel": "Herói", "golpe": "Harp of Ages"},
        {"nome": "Shantae", "jogo": "Shantae", "papel": "Meio-Gênio", "golpe": "Dança da Transformação"},
        # --- MASTER SYSTEM ---
        {"nome": "Alis Landale", "jogo": "Phantasy Star", "papel": "Protagonista", "golpe": "Espada de Luz"},
        {"nome": "Alex Kidd", "jogo": "Alex Kidd", "papel": "Mascote", "golpe": "Soco Janken"},
        # --- SNES ---
        {"nome": "Chrono", "jogo": "Chrono Trigger", "papel": "Herói", "golpe": "Luminaire"},
        {"nome": "Mega Man X", "jogo": "Mega Man X", "papel": "Hunter", "golpe": "X-Buster"},
        {"nome": "Donkey Kong", "jogo": "Donkey Kong Country", "papel": "Líder", "golpe": "Ground Pound"},
        # --- MEGA DRIVE ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Velocidade", "golpe": "Spin Dash"},
        {"nome": "Axel Stone", "jogo": "Streets of Rage", "papel": "Lutador", "golpe": "Grand Upper"},
        # --- SEGA CD ---
        {"nome": "Lute", "jogo": "Lunar: Silver Star", "papel": "Bardo", "golpe": "Canção de Cura"},
        # --- SEGA SATURN ---
        {"nome": "Nights", "jogo": "Nights into Dreams", "papel": "Espírito", "golpe": "Paraloop"},
        # --- PLAYSTATION 1 ---
        {"nome": "Solid Snake", "jogo": "Metal Gear Solid", "papel": "Espião", "golpe": "Stealth Camouflage"},
        {"nome": "Cloud Strife", "jogo": "Final Fantasy VII", "papel": "Mercenário", "golpe": "Omnislash"},
        {"nome": "Leon Kennedy", "jogo": "Resident Evil 2", "papel": "Policial", "golpe": "Tiro Preciso"},
        # --- NINTENDO 64 ---
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
            st.rerun()
else:
    st.write(f"### Bem-vindo, **{st.session_state.user}**!")
    
    # ENQUETE EXPANDIDA
    st.header("🗳️ Qual Live você quer ver?")
    # Lista com os novos jogos
    opcoes_consoles = [
        "Pokémon Crystal (GBC)", "Phantasy Star (Master)", "Chrono Trigger (SNES)", 
        "Sonic CD (Sega CD)", "Nights into Dreams (Saturn)", "Metal Gear Solid (PS1)",
        "GoldenEye 007 (N64)", "Streets of Rage 2 (Mega Drive)"
    ]
    voto = st.selectbox("Escolha seu jogo favorito:", sorted(opcoes_consoles))
    
    if st.button("Confirmar Voto"):
        db["votos"][voto] = db["votos"].get(voto, 0) + 1
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
