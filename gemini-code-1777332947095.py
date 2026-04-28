import streamlit as st

# Configurações de Design - Mantendo o padrão aprovado
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="wide")

# Banco de Dados (Mantido 100% conforme filtros anteriores)
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

# --- BARRA LATERAL ESQUERDA (ESTRUTURA MANTIDA) ---
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

# --- CONTEÚDO PRINCIPAL COM SIMETRIA ---
# Criamos duas colunas grandes: a esquerda para os filtros e a direita para o logo
col_filtros, col_logo = st.columns([1, 1], gap="large")

with col_filtros:
    st.title("🎮 CANAL KABULOPS GAMES")
    st.markdown("---")
    
    nome_player = st.text_input("[START] Qual é o seu nome, Player?", placeholder="Digite seu Nick...")
    
    if nome_player:
        st.write(f"### Seja bem-vindo, **{nome_player}**!")
        
        # Enquete
        st.header("📊 Enquete de Live")
        opcoes_live = ["Pokémon Yellow", "Phantasy Star", "Sonic 2", "Zelda", "RE 2", "KOF 98"]
        voto = st.selectbox("Qual game merece live hoje?", opcoes_live)
        if st.button("Confirmar Voto"):
            st.balloons()
            st.success(f"🏆 Voto em {voto} registrado!")

        st.markdown("---")
        
        # Busca
        st.header("🔍 Busca de Personagem")
        busca = st.text_input("Busque um título ou personagem:").strip().lower()
        if busca:
            personagens = carregar_personagens()
            encontrados = [p for p in personagens if busca in p['jogo'].lower() or busca in p['nome'].lower()]
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} ({p['jogo']})"):
                    st.write(f"**Habilidade:** {p['caracteristica']}")

with col_logo:
    # A mágica da simetria: Logo grande, centralizado e sem texto
    st.markdown("<br><br>", unsafe_allow_html=True) # Espaçamento para alinhar com o topo do formulário
    st.image("3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.jfif", use_container_width=True)
    st.caption("© 2026 Kabulops Retro Gaming - Est. 2026") # Apenas um detalhe discreto abaixo
