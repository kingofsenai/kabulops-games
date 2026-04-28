import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# --- ESCUDO DE PERSISTÊNCIA (Dados que sobrevivem ao F5) ---
@st.cache_resource
def iniciar_banco_global():
    # Isso aqui só roda UMA VEZ no servidor. 
    # Os dados aqui dentro ficam guardados mesmo se você atualizar a página.
    return {
        "total_players": 0,
        "votos_acumulados": {},
        "players_vistos": set() # Para não contar o mesmo player duas vezes no contador
    }

banco_global = iniciar_banco_global()

# --- BANCO DE DADOS DE PERSONAGENS ---
def carregar_personagens():
    return [
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "caracteristica": "Electric Type - Choque do Trovão"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "caracteristica": "Fire/Flying - Lança-chamas"},
        {"nome": "Blastoise", "jogo": "Pokémon Yellow", "papel": "Defensor", "caracteristica": "Water Type - Hydro Pump"},
        {"nome": "Venusaur", "jogo": "Pokémon Yellow", "papel": "Suporte", "caracteristica": "Grass/Poison - Solar Beam"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "caracteristica": "Psychic Type - Psychic"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "caracteristica": "Rock/Water - Lâminas de Corte"},
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio"},
        {"nome": "Luigi", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Salto Alto"},
        {"nome": "Bowser", "jogo": "Super Mario Bros", "papel": "Vilão", "caracteristica": "Força Bruta"},
        {"nome": "Yoshi", "jogo": "Super Mario Bros", "papel": "Montaria", "caracteristica": "Língua Extensível"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade Ultra"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Piloto", "caracteristica": "Voo Duplo"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Guardião", "caracteristica": "Planar e Escalar"}
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
        st.caption(f"Votos: {banco_global['votos_acumulados'][mais_votado]}")
    else:
        st.caption("Aguardando primeiro voto...")

# --- CONTEÚDO PRINCIPAL ---
col_esq, col_logo, col_dir = st.columns([1, 3, 1])
with col_logo:
    try:
        st.image(url_logo, use_container_width=True)
    except:
        st.title("🎮 KABULOPS RETRO GAMING")

st.markdown("---")

# Sistema de Login (Session State local para o nome do player)
if 'player_logado' not in st.session_state:
    st.session_state.player_logado = None

if st.session_state.player_logado is None:
    nome_input = st.text_input("[START] Digite seu Nick para entrar:", placeholder="Ex: Player1...")
    if st.button("PRESS START"):
        if nome_input:
            st.session_state.player_logado = nome_input
            # Só aumenta o contador se for um player novo na sessão global
            if nome_input not in banco_global["players_vistos"]:
                banco_global["total_players"] += 1
                banco_global["players_vistos"].add(nome_input)
            st.rerun()
else:
    st.write(f"### Bem-vindo ao Canal, **{st.session_state.player_logado}**!")
    
    # Enquete
    st.header("📊 Enquete de Live")
    opcoes_live = [
        "Pokémon Yellow (GB)", "Super Mario World (SNES)", 
        "Sonic 2 (Mega Drive)", "Zelda: Ocarina of Time (N64)",
        "Castlevania: SotN (PS1)", "Resident Evil 2 (PS1)"
    ]
    
    voto = st.selectbox("Qual clássico você gostaria de assistir em nossa primeira live?", opcoes_live)
    
    if st.button("Confirmar Voto"):
        # Grava no banco global (sobrevive ao F5)
        banco_global["votos_acumulados"][voto] = banco_global["votos_acumulados"].get(voto, 0) + 1
        st.balloons()
        st.success(f"Voto em '{voto}' registrado!")
        st.rerun()

    st.markdown("---")

    # Busca de Personagem
    st.header("🔍 Enciclopédia de Personagens")
    busca = st.text_input("Busque um herói ou vilão:").strip().lower()
    
    if busca:
        personagens = carregar_personagens()
        encontrados = [p for p in personagens if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        
        if encontrados:
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} - {p['jogo']}"):
                    st.write(f"**Papel:** {p['papel']}")
                    st.write(f"**Habilidade:** {p['caracteristica']}")
        else:
            st.warning("Personagem não encontrado.")
