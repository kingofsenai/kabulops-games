import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# --- INICIALIZAÇÃO DO SISTEMA DE MÉTRICAS (Session State) ---
if 'total_players' not in st.session_state:
    st.session_state.total_players = 0
if 'votos_acumulados' not in st.session_state:
    st.session_state.votos_acumulados = {}

# Banco de Dados de Personagens
def carregar_personagens():
    return [
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "caracteristica": "Electric Type"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "caracteristica": "Rock/Water - Lâminas"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade"},
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio"}
    ]

# URLs das Imagens
url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"
url_logo   = "https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png"

# --- BARRA LATERAL ---
with st.sidebar:
    # Painel de Identidade
    c1, c2 = st.columns([1, 2])
    with c1: st.image(url_luxury, width=70)
    with c2: st.markdown("### **Kabulops Games**")
    
    st.markdown("---")
    
    # --- NOVO BOX DE RESULTADOS PARCIAIS ---
    st.subheader("📊 Estatísticas da Live")
    st.metric(label="Players que acessaram", value=st.session_state.total_players)
    
    if st.session_state.votos_acumulados:
        # Pega o jogo mais votado
        mais_votado = max(st.session_state.votos_acumulados, key=st.session_state.votos_acumulados.get)
        qtd_votos = st.session_state.votos_acumulados[mais_votado]
        st.write(f"**Líder da Enquete:**")
        st.success(f"{mais_votado} ({qtd_votos} votos)")
    else:
        st.info("Nenhum voto registrado ainda.")

    st.markdown("---")
    st.write("🔴 **Torne-se um Kabuloso!**")

# --- CONTEÚDO PRINCIPAL ---
col_esq, col_logo, col_dir = st.columns([1, 3, 1])
with col_logo:
    st.image(url_logo, use_container_width=True)

st.markdown("---")

# Login do Player
if 'player_logado' not in st.session_state:
    nome_input = st.text_input("[START] Qual é o seu nome, Player?", placeholder="Digite seu Nick...")
    if st.button("Entrar no Game"):
        if nome_input:
            st.session_state.player_logado = nome_input
            st.session_state.total_players += 1 # Conta novo acesso
            st.rerun()
else:
    st.write(f"### Seja bem-vindo, **{st.session_state.player_logado}**!")
    
    # Enquete
    st.header("📊 Enquete de Live")
    opcoes = ["Pokémon Yellow", "Sonic 2", "Super Mario World", "Castlevania"]
    escolha = st.selectbox("Qual game merece live hoje?", opcoes)
    
    if st.button("Confirmar Voto"):
        # Registra o voto no estado da sessão
        st.session_state.votos_acumulados[escolha] = st.session_state.votos_acumulados.get(escolha, 0) + 1
        st.balloons()
        st.success(f"Voto computado para {escolha}!")
        st.rerun() # Atualiza o box na lateral imediatamente

    st.markdown("---")
    
    # Busca de Personagem (Mantida)
    st.header("🔍 Busca de Personagem")
    busca = st.text_input("Busque um título ou personagem:").strip().lower()
    if busca:
        encontrados = [p for p in carregar_personagens() if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        for p in encontrados:
            with st.expander(f"📌 {p['nome']}"):
                st.write(f"**Habilidade:** {p['caracteristica']}")
