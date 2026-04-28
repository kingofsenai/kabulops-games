import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# Banco de Dados de Personagens (Mantido 100%)
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

# --- BARRA LATERAL ESQUERDA (MANTIDA) ---
with st.sidebar:
    # Item 1: Luxury Ball
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=70)
    with c2:
        st.markdown("### **Kabulops Games**")
    st.markdown("---")
    
    # Item 2: Master Ball
    c3, c4 = st.columns([1, 2])
    with c3:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png", width=70)
    with c4:
        st.markdown("### **Participe da Pesquisa**")
    st.markdown("---")
    
    # Item 3: Ultra Ball
    c5, c6 = st.columns([1, 2])
    with c5:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png", width=70)
    with c6:
        st.markdown("#### **Torne-se um Kabuloso, inscreva-se no canal!**")

# --- CONTEÚDO PRINCIPAL (COM O LOGO NO TOPO) ---

# Centralizando o Logo entre a sidebar e o conteúdo
col_vazia_esq, col_logo, col_vazia_dir = st.columns([1, 3, 1])
with col_logo:
    st.image("3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.jpg", use_container_width=True)

st.markdown("---")

# 1ª ETAPA: NOME DO PLAYER (Filtros preservados)
nome_player = st.text_input("[START] Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Seja bem-vindo, **{nome_player}**!")
    st.markdown("---")

    # 2ª ETAPA: ENQUETE DE LIVE
    st.header("📊 Enquete de Live")
    st.write(f"{nome_player}, qual game merece uma live hoje?")
    
    opcoes_live = [
        "1. Pokémon Yellow", "2. Phantasy Star", "3. Zelda", 
        "4. Sonic 2", "5. Super Mario World", "6. Castlevania: SotN"
    ]
    
    voto = st.selectbox("Escolha uma opção:", opcoes_live)
    
    if st.button("Confirmar Voto"):
        st.balloons()
        st.success(f"🏆 VOTO REGISTRADO: {voto}")

    st.markdown("---")

    # 3ª ETAPA: BUSCA DE PERSONAGEM
    st.header("🔍 Busca de Personagem")
    busca = st.text_input("Busque um título ou personagem:").strip().lower()
    
    if busca:
        personagens = carregar_personagens()
        encontrados = [p for p in personagens if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        
        if encontrados:
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} ({p['jogo']})"):
                    st.write(f"**Habilidade:** {p['caracteristica']}")
        else:
            st.warning(f"❌ '{busca}' não localizado.")
