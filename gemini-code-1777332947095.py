import streamlit as st
import time

# --- CONFIGURAÇÃO DE ALTA PERFORMANCE ---
st.set_page_config(
    page_title="Kabulops Games", 
    page_icon="🎮", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- CACHE DE DADOS ESTÁTICOS (Não muda, carrega 1x só) ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # --- POKÉMON YELLOW ---
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "golpe": "Thunderbolt"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "golpe": "Slash"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "golpe": "Flamethrower"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "golpe": "Psychic"},
        {"nome": "Blue (Rival)", "jogo": "Pokémon Yellow", "papel": "Rival", "golpe": "Evolução Estratégica"},

        # --- STREET FIGHTER II ---
        {"nome": "Ryu", "jogo": "Street Fighter II", "papel": "Protagonista", "golpe": "Hadouken"},
        {"nome": "Ken Masters", "jogo": "Street Fighter II", "papel": "Rival", "golpe": "Shoryuken"},
        {"nome": "Chun-Li", "jogo": "Street Fighter II", "papel": "Velocidade", "golpe": "Kikoken"},
        {"nome": "Guile", "jogo": "Street Fighter II", "papel": "Defensivo", "golpe": "Sonic Boom"},
        {"nome": "M. Bison", "jogo": "Street Fighter II", "papel": "Vilão Final", "golpe": "Psycho Crusher"},

        # --- RESIDENT EVIL 2 ---
        {"nome": "Leon S. Kennedy", "jogo": "Resident Evil 2", "papel": "Policial", "golpe": "Precisão"},
        {"nome": "Claire Redfield", "jogo": "Resident Evil 2", "papel": "Sobrevivente", "golpe": "Lança-Granadas"},
        {"nome": "Ada Wong", "jogo": "Resident Evil 2", "papel": "Espiã", "golpe": "Grappling Gun"},
        {"nome": "Sherry Birkin", "jogo": "Resident Evil 2", "papel": "Protegida", "golpe": "Furtividade"},
        {"nome": "Mr. X", "jogo": "Resident Evil 2", "papel": "Perseguidor", "golpe": "Soco Devastador"},

        # --- METAL GEAR SOLID ---
        {"nome": "Solid Snake", "jogo": "Metal Gear Solid", "papel": "Agente", "golpe": "CQC / Stealth"},
        {"nome": "Meryl Silverburgh", "jogo": "Metal Gear Solid", "papel": "Aliada", "golpe": "Atiradora"},
        {"nome": "Otacon", "jogo": "Metal Gear Solid", "papel": "Suporte Técnico", "golpe": "Hackeamento"},
        {"nome": "Liquid Snake", "jogo": "Metal Gear Solid", "papel": "Antagonista", "golpe": "Liderança"},
        {"nome": "Psycho Mantis", "jogo": "Metal Gear Solid", "papel": "Místico", "golpe": "Telecinese"},

        # --- FINAL FANTASY VII ---
        {"nome": "Cloud Strife", "jogo": "Final Fantasy VII", "papel": "Ex-SOLDIER", "golpe": "Omnislash"},
        {"nome": "Tifa Lockhart", "jogo": "Final Fantasy VII", "papel": "Lutadora", "golpe": "Final Heaven"},
        {"nome": "Aerith", "jogo": "Final Fantasy VII", "papel": "Mística", "golpe": "Great Gospel"},
        {"nome": "Barret Wallace", "jogo": "Final Fantasy VII", "papel": "Líder", "golpe": "Big Shot"},
        {"nome": "Sephiroth", "jogo": "Final Fantasy VII", "papel": "Antagonista", "golpe": "Super Nova"},
        
        # --- SONIC THE HEDGEHOG ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "golpe": "Spin Dash"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Apoio", "golpe": "Voo"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Força", "golpe": "Planar"},
        {"nome": "Amy Rose", "jogo": "Sonic the Hedgehog", "papel": "Martelo", "golpe": "Piko Piko Hammer"},
        {"nome": "Dr. Eggman", "jogo": "Sonic the Hedgehog", "papel": "Vilão", "golpe": "E-Mech"},
    ]

# --- BANCO DE DADOS GLOBAL ---
@st.cache_resource
def banco_de_dados():
    return {"total": 0, "votos": {}, "usuarios": set()}

db = banco_de_dados()

# --- LÓGICA DE RANKING RÁPIDA ---
def get_top_3():
    return sorted(db["votos"].items(), key=lambda x: x[1], reverse=True)[:3]

# --- UI DA BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=50)
    st.title("Kabulops Games")
    st.markdown("---")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png", width=50)
    st.markdown("#### **Participe da Pesquisa**")
    st.markdown("---")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png", width=50)
    st.markdown("#### **Seja um Kabuloso**\n*Inscreva-se*")
    st.markdown("---")

    st.subheader("📊 Placar Geral")
    st.metric("Jogadores Online", db["total"])
    
    ranking = get_top_3()
    if ranking:
        st.write("🏆 **Top 3 Live:**")
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, qtd) in enumerate(ranking):
            st.markdown(f"{medals[i]} {jogo} ({qtd})")
    else:
        st.caption("Aguardando votos...")

# --- CORPO PRINCIPAL ---
st.image("https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png")

if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    nick = st.text_input("Digite seu Nick para entrar:", key="login_input")
    if st.button("PRESS START"):
        if nick:
            st.session_state.user = nick
            if nick not in db["usuarios"]:
                db["total"] += 1
                db["usuarios"].add(nick)
            st.rerun()
else:
    st.markdown(f"### Bem-vindo ao Game, **{st.session_state.user}**!")
    
    # ENQUETE
    with st.container():
        st.header("🗳️ Próxima Live")
        opcoes = ["Resident Evil 2", "Final Fantasy VII", "Sonic 2", "Street Fighter II", "Castlevania: SotN", "Metal Gear Solid", "Tekken 3"]
        voto = st.selectbox("Escolha o clássico:", sorted(opcoes))
        
        if st.button("Confirmar Voto"):
            db["votos"][voto] = db["votos"].get(voto, 0) + 1
            st.balloons()
            st.success("Voto Computado!")
            time.sleep(0.5)
            st.rerun()

    st.markdown("---")

    # ENCICLOPÉDIA OTIMIZADA
    st.header("📖 Biblioteca de Heróis")
    termo = st.text_input("Buscar por nome ou jogo:").lower()
    
    biblioteca = carregar_biblioteca_estatica()
    if termo:
        resultados = [p for p in biblioteca if termo in p['nome'].lower() or termo in p['jogo'].lower()]
        if resultados:
            for r in resultados:
                with st.expander(f"🔹 {r['nome']} ({r['jogo']})"):
                    st.write(f"**Papel:** {r['papel']}")
                    st.write(f"**Golpe:** {r['golpe']}")
        else:
            st.warning("Nada encontrado.")
