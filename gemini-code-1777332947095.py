import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# Banco de Dados (Mantido conforme solicitado)
def carregar_personagens():
    return [
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "caracteristica": "Electric Type - Choque do Trovão"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "caracteristica": "Fire/Flying - Lança-chamas"},
        {"nome": "Blastoise", "jogo": "Pokémon Yellow", "papel": "Defensor", "caracteristica": "Water Type - Hydro Pump"},
        {"nome": "Venusaur", "jogo": "Pokémon Yellow", "papel": "Suporte", "caracteristica": "Grass/Poison - Solar Beam"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "caracteristica": "Psychic Type - Amnesia/Psychic"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "caracteristica": "Rock/Water - Lâminas de Corte"},
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio"},
        {"nome": "Luigi", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Salto Alto"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Guardião", "caracteristica": "Planar/Escalar"}
    ]

# URLs das Imagens (Substituindo os arquivos locais que causaram erro)
url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"

# --- BARRA LATERAL (LAYOUT COM URLs PARA EVITAR ERRO) ---
with st.sidebar:
    # Item 1: Kabulops Games
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(url_luxury, width=80) 
    with col2:
        st.markdown("### **Kabulops Games**")
    
    st.markdown("---")
    
    # Item 2: Participe da Pesquisa
    col3, col4 = st.columns([1, 2])
    with col3:
        st.image(url_master, width=80)
    with col4:
        st.markdown("### **Participe da Pesquisa**")
        
    st.markdown("---")
    
    # Item 3: Torne-se um Kabuloso
    col5, col6 = st.columns([1, 2])
    with col5:
        st.image(url_ultra, width=80)
    with col6:
        st.markdown("### **Torne-se um Kabuloso, inscreva-se no canal!**")

# --- CONTEÚDO PRINCIPAL (FILTROS MANTIDOS) ---
st.title("🎮 CANAL KABULOPS GAMES")
st.markdown("---")

nome_player = st.text_input("[START] Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Seja bem-vindo, **{nome_player}**!")
    st.markdown("---")

    # 2ª ETAPA: ENQUETE DE LIVE
    st.header("📊 Enquete de Live")
    st.write(f"{nome_player}, qual game merece uma live hoje?")
    
    opcoes_live = [
        "1. Pokémon Yellow", "2. Phantasy Star", "3. Zelda: ALTTP", 
        "4. Sonic 2", "5. Super Mario World", "6. Cotton 2",
        "7. Zelda: OOT", "8. KOF '98", "9. Castlevania: SotN",
        "10. Metal Gear Solid", "11. Resident Evil 2", "12. Street Fighter II"
    ]
    
    voto = st.selectbox("Escolha uma opção de 1 a 12:", opcoes_live)
    
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
                    st.write(f"**Papel:** {p['papel']}")
                    st.write(f"**Característica:** {p['caracteristica']}")
