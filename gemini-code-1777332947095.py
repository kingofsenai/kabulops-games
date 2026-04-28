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
# --- BARRA LATERAL (VERSÃO KABULOSA HD) ---
with st.sidebar:
    # Cabeçalho com Pokébolas em Alta Resolução
    # Usando artes oficiais para melhor definição
    url_luxury_hd = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
    url_master_hd = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
    url_ultra_hd  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"

    # Layout de Grade para as Pokébolas e Textos
    c1, c2 = st.columns([1, 3])
    with c1: st.image(url_luxury_hd, width=60)
    with c2: st.markdown("#### **Kabulops Games**")
    
    st.markdown("---")
    
    c3, c4 = st.columns([1, 3])
    with c3: st.image(url_master_hd, width=60)
    with c4: st.markdown("#### **Pesquisa Ativa**")
    
    st.markdown("---")
    
    c5, c6 = st.columns([1, 3])
    with c5: st.image(url_ultra_hd, width=60)
    with c6: st.markdown("#### **Clube Kabuloso**")
    
    st.markdown("---")

    # --- SEÇÃO DE ESTATÍSTICAS E RANKING ---
    st.subheader("📊 Painel de Dados")
    st.metric(label="Players Totais", value=banco_global["total_players"])
    
    st.markdown("---")
    st.subheader("🏆 Top 3 da Comunidade")
    
    ranking = obter_ranking()
    
    if ranking:
        # Exibição elegante do Top 3
        cores = ["#FFD700", "#C0C0C0", "#CD7F32"] # Ouro, Prata, Bronze
        medals = ["🥇", "🥈", "🥉"]
        
        for i, (jogo, votos) in enumerate(ranking[:3]):
            st.markdown(f"{medals[i]} **{jogo}**")
            st.caption(f"{votos} votos registrados")
    else:
        st.info("Aguardando o primeiro voto!")
