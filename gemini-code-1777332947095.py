import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# Banco de Dados (Mantido 100%)
def carregar_personagens():
    return [
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "caracteristica": "Electric Type - Choque do Trovão"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "caracteristica": "Fire/Flying - Lança-chamas"},
        {"nome": "Blastoise", "jogo": "Pokémon Yellow", "papel": "Defensor", "caracteristica": "Water Type - Hydro Pump"},
        {"nome": "Venusaur", "jogo": "Pokémon Yellow", "papel": "Suporte", "caracteristica": "Grass/Poison - Solar Beam"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "caracteristica": "Psychic Type - Amnesia/Psychic"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "caracteristica": "Rock/Water - Lâminas de Corte"},
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade"}
    ]

# Links das Pokébolas (URLs Externas)
url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"

# --- LINK DO SEU LOGO (CORRIGIDO COM ASPAS E FORMATO RAW) ---
url_logo = "https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png"

# --- BARRA LATERAL ---
with st.sidebar:
    c1, c2 = st.columns([1, 2])
    with c1: st.image(url_luxury, width=70)
    with c2: st.markdown("### **Kabulops Games**")
    st.markdown("---")
    
    c3, c4 = st.columns([1, 2])
    with c3: st.image(url_master, width=70)
    with c4: st.markdown("### **Participe da Pesquisa**")
    st.markdown("---")
    
    c5, c6 = st.columns([1, 2])
    with c5: st.image(url_ultra, width=70)
    with c6: st.markdown("#### **Torne-se um Kabuloso!**")

# --- CONTEÚDO PRINCIPAL (LOGO CENTRALIZADO) ---
col_esq, col_logo, col_dir = st.columns([1, 3, 1])
with col_logo:
    # O uso do 'try' garante que o app não quebre se o link falhar
    try:
        st.image(url_logo, use_container_width=True)
    except:
        st.title("🎮 CANAL KABULOPS GAMES")

st.markdown("---")

# --- FILTROS (MANTIDOS EXATAMENTE ONDE ESTÃO) ---
nome_player = st.text_input("[START] Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Seja bem-vindo, **{nome_player}**!")
    st.markdown("---")

    st.header("📊 Enquete de Live")
    opcoes_live = ["Pokémon Yellow", "Phantasy Star", "Zelda", "Sonic 2", "Super Mario World", "Castlevania"]
    voto = st.selectbox("Qual game merece live hoje?", opcoes_live)
    
    if st.button("Confirmar Voto"):
        st.balloons()
        st.success(f"🏆 VOTO REGISTRADO: {voto}")

    st.markdown("---")

    st.header("🔍 Busca de Personagem")
    busca = st.text_input("Busque um título ou personagem:").strip().lower()
    
    if busca:
        personagens = carregar_personagens()
        encontrados = [p for p in personagens if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        for p in encontrados:
            with st.expander(f"📌 {p['nome']} ({p['jogo']})"):
                st.write(f"**Habilidade:** {p['caracteristica']}")
