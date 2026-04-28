import streamlit as st
import time

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# --- ESCUDO DE PERSISTÊNCIA (Dados Globais) ---
@st.cache_resource
def iniciar_banco_global():
    return {
        "total_players": 0,
        "votos_acumulados": {},
        "players_vistos": set()
    }

banco_global = iniciar_banco_global()

# --- FUNÇÃO DE RANKING OTIMIZADA ---
def obter_ranking():
    # Ordena os votos do maior para o menor
    ranking_ordenado = sorted(
        banco_global["votos_acumulados"].items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    return ranking_ordenado

# --- MEGA ENCICLOPÉDIA RECHEADA ---
def carregar_personagens():
    return [
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "golpe": "Thunderbolt"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "golpe": "Slash"},
        {"nome": "Scorpion", "jogo": "Mortal Kombat", "papel": "Vingador", "golpe": "Spear"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "golpe": "Spin Dash"},
        # ... (mantenha os outros aqui)
    ]

opcoes_live = [
    "Alex Kidd in Miracle World", "Castle of Illusion", "Phantasy Star", "Wonder Boy III", 
    "Shinobi (Master)", "Sonic (Master)", "Streets of Rage 2", "Mortal Kombat II", 
    "Resident Evil 2", "Castlevania: SotN", "Metal Gear Solid"
]

# URLs das Imagens
url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"
url_logo   = "https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png"

# --- BARRA LATERAL (RANKING TOP 3) ---
with st.sidebar:
    st.image(url_logo, width=150)
    st.markdown("### **Estatísticas da Live**")
    st.metric(label="Players Totais", value=banco_global["total_players"])
    
    st.markdown("---")
    st.subheader("🏆 Ranking Atual")
    
    ranking = obter_ranking()
    
    if ranking:
        # TOP 1 - OURO
        st.markdown(f"🥇 **1º: {ranking[0][0]}** ({ranking[0][1]} votos)")
        
        # TOP 2 - PRATA (se existir)
        if len(ranking) > 1:
            st.markdown(f"🥈 **2º: {ranking[1][0]}** ({ranking[1][1]} votos)")
            
        # TOP 3 - BRONZE (se existir)
        if len(ranking) > 2:
            st.markdown(f"🥉 **3º: {ranking[2][0]}** ({ranking[2][1]} votos)")
    else:
        st.caption("Nenhum voto computado ainda.")
    
    st.markdown("---")
    st.image(url_master, width=50)

# --- CONTEÚDO PRINCIPAL ---
col_esq, col_logo, col_dir = st.columns([1, 3, 1])
with col_logo:
    try:
        st.image(url_logo, use_container_width=True)
    except:
        st.title("KABULOPS RETRO GAMING")

st.markdown("---")

if 'player_logado' not in st.session_state:
    st.session_state.player_logado = None

if st.session_state.player_logado is None:
    nome_input = st.text_input("[START] Digite seu Nick:", placeholder="Ex: Player1...")
    if st.button("PRESS START"):
        if nome_input:
            st.session_state.player_logado = nome_input
            if nome_input not in banco_global["players_vistos"]:
                banco_global["total_players"] += 1
                banco_global["players_vistos"].add(nome_input)
            st.rerun()
else:
    st.write(f"### Bem-vindo, **{st.session_state.player_logado}**!")
    
    st.header("🗳️ Enquete de Live")
    voto = st.selectbox("Qual clássico você quer na próxima live?", sorted(opcoes_live))
    
    if st.button("Confirmar Voto"):
        banco_global["votos_acumulados"][voto] = banco_global["votos_acumulados"].get(voto, 0) + 1
        st.balloons()
        st.success(f"Voto computado para {voto}!")
        time.sleep(1)
        st.rerun()

    st.markdown("---")

    # --- BUSCA NA ENCICLOPÉDIA ---
    st.header("📖 Enciclopédia")
    busca = st.text_input("Busque um herói ou jogo:").strip().lower()
    
    if busca:
        encontrados = [p for p in carregar_personagens() if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        if encontrados:
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} - {p['jogo']}"):
                    st.write(f"**Papel:** {p['papel']}")
                    st.write(f"**Golpe:** {p['golpe']}")
        else:
            st.warning("Nada encontrado no banco de dados.")
