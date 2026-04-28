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

# --- FUNÇÃO DE RANKING ---
def obter_ranking():
    return sorted(
        banco_global["votos_acumulados"].items(), 
        key=lambda item: item[1], 
        reverse=True
    )

# --- MEGA ENCICLOPÉDIA ---
def carregar_personagens():
    return [
        # --- POKÉMON YELLOW ---
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "golpe": "Thunderbolt (Choque do Trovão)"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "golpe": "Slash (Lâminas de Corte)"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "golpe": "Flamethrower (Lança-chamas)"},
        {"nome": "Blastoise", "jogo": "Pokémon Yellow", "papel": "Defensor", "golpe": "Hydro Pump (Jato d'Água)"},
        {"nome": "Venusaur", "jogo": "Pokémon Yellow", "papel": "Suporte", "golpe": "Solar Beam (Raio Solar)"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "golpe": "Psychic (Poder Psíquico)"},
        {"nome": "Dragonite", "jogo": "Pokémon Yellow", "papel": "Pseudo-Lendário", "golpe": "Hyper Beam (Hiper Raio)"},
        {"nome": "Gengar", "jogo": "Pokémon Yellow", "papel": "Assassino", "golpe": "Dream Eater (Comedor de Sonhos)"},
        {"nome": "Snorlax", "jogo": "Pokémon Yellow", "papel": "Tanque", "golpe": "Body Slam (Pancada Corporal)"},

        # --- STREET FIGHTER ---
        {"nome": "Ryu", "jogo": "Street Fighter II", "papel": "Protagonista", "golpe": "Hadouken"},
        {"nome": "Ken", "jogo": "Street Fighter II", "papel": "Rival", "golpe": "Shoryuken"},
        {"nome": "Chun-Li", "jogo": "Street Fighter II", "papel": "Velocidade", "golpe": "Kikoken"},
        {"nome": "Guile", "jogo": "Street Fighter II", "papel": "Defensivo", "golpe": "Sonic Boom"},
        {"nome": "Blanka", "jogo": "Street Fighter II", "papel": "Selvagem", "golpe": "Electric Thunder"},
        {"nome": "Zangief", "jogo": "Street Fighter II", "papel": "Grappler", "golpe": "Spinning Piledriver"},

        # --- MORTAL KOMBAT ---
        {"nome": "Scorpion", "jogo": "Mortal Kombat", "papel": "Vingador", "golpe": "Spear (Get Over Here!)"},
        {"nome": "Sub-Zero", "jogo": "Mortal Kombat", "papel": "Criomante", "golpe": "Ice Blast (Congelamento)"},
        {"nome": "Raiden", "jogo": "Mortal Kombat", "papel": "Deus", "golpe": "Torpedo Elétrico"},
        {"nome": "Liu Kang", "jogo": "Mortal Kombat", "papel": "Campeão", "golpe": "Bicycle Kick"},
        {"nome": "Kitana", "jogo": "Mortal Kombat", "papel": "Princesa", "golpe": "Fan Throw"},
        {"nome": "Johnny Cage", "jogo": "Mortal Kombat", "papel": "Astro", "golpe": "Shadow Kick"},

        # --- MARIO & SONIC & OUTROS ---
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "golpe": "Fireball"},
        {"nome": "Luigi", "jogo": "Super Mario World", "papel": "Herói", "golpe": "Super Pulo"},
        {"nome": "Yoshi", "jogo": "Super Mario World", "papel": "Montaria", "golpe": "Língua Extensível"},
        {"nome": "Bowser", "jogo": "Super Mario Bros", "papel": "Vilão", "golpe": "Fire Breath"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "golpe": "Spin Dash"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Apoio", "golpe": "Voo com Caudas"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Força", "golpe": "Soco Planador"},
        {"nome": "Alex Kidd", "jogo": "Alex Kidd", "papel": "Mascote", "golpe": "Soco Janken"}
    ]

opcoes_live = [
    "Alex Kidd in Miracle World", "Castle of Illusion", "Phantasy Star", "Wonder Boy III", "Shinobi (Master)", 
    "Sonic (Master)", "Asterix", "Psycho Fox", "Golden Axe", "California Games", "Sonic 2", "Streets of Rage 2", 
    "Shinobi III", "Gunstar Heroes", "Earthworm Jim", "Mortal Kombat II", "Street Fighter II Special Edition", 
    "Comix Zone", "Aladdin", "Castle of Illusion (Mega)", "Resident Evil 2", "Castlevania: SotN", 
    "Metal Gear Solid", "Crash Bandicoot 3", "Final Fantasy VII", "Tekken 3", "Silent Hill", 
    "Tony Hawk's Pro Skater 2", "Spider-Man", "Gran Turismo 2"
]

url_logo = "https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png"

# --- BARRA LATERAL ATUALIZADA ---
with st.sidebar:
    url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
    url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
    url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"

    # Seção 1
    c1, c2 = st.columns([1, 3])
    with c1: st.image(url_luxury, width=60)
    with c2: st.markdown("#### **Kabulops Games**")
    st.markdown("---")
    
    # Seção 2 (Texto Alterado)
    c3, c4 = st.columns([1, 3])
    with c3: st.image(url_master, width=60)
    with c4: st.markdown("#### **Participe da Pesquisa**")
    st.markdown("---")
    
    # Seção 3 (Texto Alterado em duas linhas)
    c5, c6 = st.columns([1, 3])
    with c5: st.image(url_ultra, width=60)
    with c6: st.markdown("#### **Seja um Kabuloso**\n*Inscreva-se*")
    st.markdown("---")

    st.subheader("📊 Estatísticas")
    st.metric(label="Players Totais", value=banco_global["total_players"])
    
    st.markdown("---")
    st.subheader("🏆 Top 3 da Live")
    ranking = obter_ranking()
    if ranking:
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, votos) in enumerate(ranking[:3]):
            st.markdown(f"{medals[i]} **{jogo}** ({votos} votos)")
    else:
        st.caption("Aguardando votos...")

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
    voto = st.selectbox("Qual clássico você gostaria de assistir?", sorted(opcoes_live))
    
    if st.button("Confirmar Voto"):
        banco_global["votos_acumulados"][voto] = banco_global["votos_acumulados"].get(voto, 0) + 1
        st.balloons()
        st.snow()
        st.success(f"Voto computado: {voto}!")
        time.sleep(1)
        st.rerun()

    st.markdown("---")

    # --- ENCICLOPÉDIA RECHEADA ---
    st.header("📖 Enciclopédia de Personagens")
    busca = st.text_input("Busque um herói ou vilão:").strip().lower()
    
    if busca:
        encontrados = [p for p in carregar_personagens() if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        if encontrados:
            for p in encontrados:
                with st.expander(f"⭐ {p['nome']} - {p['jogo']}"):
                    st.write(f"**Papel:** {p['papel']}")
                    st.write(f"**Golpe Especial:** {p['golpe']}")
        else:
            st.warning("Personagem não encontrado.")
