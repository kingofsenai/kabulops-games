import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# --- ESCUDO DE PERSISTÊNCIA ---
@st.cache_resource
def iniciar_banco_global():
    return {
        "total_players": 0,
        "votos_acumulados": {},
        "players_vistos": set()
    }

banco_global = iniciar_banco_global()

# --- BANCO DE DADOS EXPANDIDO ---
def carregar_personagens():
    return [
        # --- POKÉMON (Novos + Clássicos) ---
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "caracteristica": "Electric Type - Choque do Trovão"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "caracteristica": "Rock/Water - Lâminas de Corte"},
        {"nome": "Dragonite", "jogo": "Pokémon Yellow", "papel": "Pseudo-Lendário", "caracteristica": "Dragon/Flying - Hyper Beam"},
        {"nome": "Gengar", "jogo": "Pokémon Yellow", "papel": "Assassino", "caracteristica": "Ghost/Poison - Dream Eater"},
        {"nome": "Arcanine", "jogo": "Pokémon Yellow", "papel": "Veloz", "caracteristica": "Fire Type - Extreme Speed"},
        {"nome": "Lapras", "jogo": "Pokémon Yellow", "papel": "Transporte/Tanque", "caracteristica": "Water/Ice - Ice Beam"},
        {"nome": "Snorlax", "jogo": "Pokémon Yellow", "papel": "Tanque", "caracteristica": "Normal Type - Body Slam"},

        # --- STREET FIGHTER ---
        {"nome": "Ryu", "jogo": "Street Fighter II", "papel": "Protagonista", "caracteristica": "Hadouken / Shoryuken"},
        {"nome": "Chun-Li", "jogo": "Street Fighter II", "papel": "Velocidade", "caracteristica": "Hyakuretsu Kyaku (Lightning Kick)"},
        {"nome": "Guile", "jogo": "Street Fighter II", "papel": "Defensivo", "caracteristica": "Sonic Boom / Flash Kick"},
        {"nome": "Akuma", "jogo": "Street Fighter II", "papel": "Antagonista", "caracteristica": "Shun Goku Satsu"},
        {"nome": "Blanka", "jogo": "Street Fighter II", "papel": "Selvagem", "caracteristica": "Electric Thunder"},

        # --- MORTAL KOMBAT ---
        {"nome": "Scorpion", "jogo": "Mortal Kombat", "papel": "Vingador", "caracteristica": "Get Over Here! (Spear)"},
        {"nome": "Sub-Zero", "jogo": "Mortal Kombat", "papel": "Criomante", "caracteristica": "Congelamento"},
        {"nome": "Raiden", "jogo": "Mortal Kombat", "papel": "Deus do Trovão", "caracteristica": "Teleporte e Raios"},
        {"nome": "Kitana", "jogo": "Mortal Kombat", "papel": "Princesa", "caracteristica": "Leques Cortantes"},
        {"nome": "Liu Kang", "jogo": "Mortal Kombat", "papel": "Campeão", "caracteristica": "Bicycle Kick / Dragão de Fogo"},

        # --- PERSONAGENS CLÁSSICOS ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade"},
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Pulo e Fogo"},
        {"nome": "Alex Kidd", "jogo": "Alex Kidd in Miracle World", "papel": "Mascote", "caracteristica": "Soco de Pedra"},
    ]

# Lista de Jogos para Enquete (Expandida com 10 de cada console)
opcoes_live = [
    # MASTER SYSTEM
    "Alex Kidd in Miracle World", "Castle of Illusion", "Phantasy Star", "Wonder Boy III", "Shinobi (Master)", "Sonic (Master)", "Asterix", "Psycho Fox", "Golden Axe", "California Games",
    # MEGA DRIVE
    "Sonic 2", "Streets of Rage 2", "Shinobi III", "Gunstar Heroes", "Earthworm Jim", "Mortal Kombat II", "Street Fighter II Special Edition", "Comix Zone", "Aladdin", "Castle of Illusion (Mega)",
    # PLAYSTATION 1
    "Resident Evil 2", "Castlevania: SotN", "Metal Gear Solid", "Crash Bandicoot 3", "Final Fantasy VII", "Tekken 3", "Silent Hill", "Tony Hawk's Pro Skater 2", "Spider-Man", "Gran Turismo 2"
]

# URLs das Imagens
url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"
url_logo   = "https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png"

# --- BARRA LATERAL ---
with st.sidebar:
    c1, c2 = st.columns([1, 2])
    with c1: st.image(url_luxury, width=75)
    with c2: st.markdown("### **Kabulops Games**")
    st.markdown("---")
    c3, c4 = st.columns([1, 2])
    with c3: st.image(url_master, width=75)
    with c4: st.markdown("### **Participe da Pesquisa**")
    st.markdown("---")
    c5, c6 = st.columns([1, 2])
    with c5: st.image(url_ultra, width=75)
    with c6: st.markdown("#### **Torne-se um Kabuloso!**")
    st.markdown("---")
    
    st.subheader("📊 Estatísticas")
    st.metric(label="Players Totais", value=banco_global["total_players"])
    if banco_global["votos_acumulados"]:
        mais_votado = max(banco_global["votos_acumulados"], key=banco_global["votos_acumulados"].get)
        st.write(f"**Líder:** {mais_votado}")
    else:
        st.caption("Aguardando votos...")

# --- CONTEÚDO PRINCIPAL ---
col_esq, col_logo, col_dir = st.columns([1, 3, 1])
with col_logo:
    try:
        st.image(url_logo, use_container_width=True)
    except:
        st.title("🎮 KABULOPS RETRO GAMING")

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
    
    # Enquete
    st.header("📊 Enquete de Live")
    voto = st.selectbox("Qual clássico você gostaria de assistir em nossa primeira live?", sorted(opcoes_live))
    
    if st.button("Confirmar Voto"):
        banco_global["votos_acumulados"][voto] = banco_global["votos_acumulados"].get(voto, 0) + 1
        st.balloons()
        st.success(f"Voto em '{voto}' registrado!")
        st.rerun()

    st.markdown("---")

    # Busca de Personagem
    st.header("🔍 Enciclopédia de Personagens")
    busca = st.text_input("Busque um herói ou vilão:").strip().lower()
    
    if busca:
        encontrados = [p for p in carregar_personagens() if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        if encontrados:
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} - {p['jogo']}"):
                    st.write(f"**Papel:** {p['papel']}")
                    st.write(f"**Habilidade:** {p['caracteristica']}")
        else:
            st.warning("Personagem não encontrado.")
