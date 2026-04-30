import streamlit as st
import time
import json
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Kabulops Games", 
    page_icon="🎮", 
    layout="centered"
)

# --- 2. SISTEMA DE PERSISTÊNCIA ---
DB_FILE = "database_kabulops.json"

def carregar_dados():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                data = json.load(f)
                data["usuarios"] = set(data.get("usuarios", []))
                if "votos" not in data:
                    data["votos"] = {}
                return data
        except:
            pass
    return {"total": 0, "votos": {}, "usuarios": set()}

def salvar_dados(dados):
    dados_para_salvar = dados.copy()
    dados_para_salvar["usuarios"] = list(dados_para_salvar["usuarios"])
    with open(DB_FILE, "w") as f:
        json.dump(dados_para_salvar, f, indent=4)

if "db" not in st.session_state:
    st.session_state.db = carregar_dados()

def get_top_3():
    db = st.session_state.db
    if not db["votos"]:
        return []
    return sorted(db["votos"].items(), key=lambda x: x[1], reverse=True)[:3]

# --- 3. BIBLIOTECA DE PERSONAGENS ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        {"nome": "Suicune", "jogo": "Pokémon Crystal (GBC)", "papel": "Lendário", "golpe": "Aurora Beam / Hydro Pump"},
        {"nome": "Eusine", "jogo": "Pokémon Crystal (GBC)", "papel": "Treinador", "golpe": "Dream Eater / Mean Look"},
        {"nome": "Alis Landale", "jogo": "Phantasy Star (Master)", "papel": "Protagonista", "golpe": "Fire Spell / Light Sword"},
        {"nome": "Myau", "jogo": "Phantasy Star (Master)", "papel": "Guardião", "golpe": "Cure Magic / Trap Disarm"},
        {"nome": "Chrono", "jogo": "Chrono Trigger (SNES)", "papel": "Herói", "golpe": "Luminaire / Cyclone"},
        {"nome": "Frog", "jogo": "Chrono Trigger (SNES)", "papel": "Cavaleiro", "golpe": "Water 2 / Leap Slash"},
        {"nome": "Sonic", "jogo": "Sonic CD (Sega CD)", "papel": "Velocidade", "golpe": "Spin Dash / Super Peel Out"},
        {"nome": "Metal Sonic", "jogo": "Sonic CD (Sega CD)", "papel": "Antagonista", "golpe": "Maximum Overdrive / V. Shield"},
        {"nome": "Nights", "jogo": "Nights into Dreams (Saturn)", "papel": "Espírito", "golpe": "Paraloop / Drill Dash"},
        {"nome": "Reala", "jogo": "Nights into Dreams (Saturn)", "papel": "Rival", "golpe": "Nightmaren Slash / Illusion"},
        {"nome": "Solid Snake", "jogo": "Metal Gear Solid (PS1)", "papel": "Espião", "golpe": "CQC / Stinger Missile"},
        {"nome": "Gray Fox", "jogo": "Metal Gear Solid (PS1)", "papel": "Ciborgue Ninja", "golpe": "Stealth Camouflage / Katana Slash"},
        {"nome": "James Bond", "jogo": "GoldenEye 007 (N64)", "papel": "Agente", "golpe": "Remote Mines / Golden Gun"},
        {"nome": "Alec Trevelyan", "jogo": "GoldenEye 007 (N64)", "papel": "Vilão", "golpe": "Dual RCP-90 / Tactical Strike"},
        {"nome": "Axel Stone", "jogo": "Streets of Rage 2 (Mega Drive)", "papel": "Lutador", "golpe": "Grand Upper / Dragon Wing"},
        {"nome": "Blaze Fielding", "jogo": "Streets of Rage 2 (Mega Drive)", "papel": "Lutadora", "golpe": "Kikousho / Somersault Kick"},
        {"nome": "Kabutops", "jogo": "Pokémon Red/Blue/Yellow", "papel": "Fóssil", "golpe": "Slash / Hydro Pump"},
        {"nome": "Terry Bogard", "jogo": "Fatal Fury", "papel": "Lutador", "golpe": "Power Wave / Burn Knuckle"},
    ]

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=50)
    st.title("Kabulops Games")
    st.markdown("---")
    
    # Pokebola 1: Inscreva-se
    col_insc, text_insc = st.columns([1, 4])
    with col_insc:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png", width=25)
    with text_insc:
        st.link_button("Inscreva-se no Canal", "https://www.youtube.com/@kabulops")

    # Pokebola 2: Enquete
    col_enq, text_enq = st.columns([1, 4])
    with col_enq:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/great-ball.png", width=25)
    with text_enq:
        st.link_button("Participe da Enquete", "#votar")

    st.markdown("---")
    
    st.subheader("📊 Placar Global")
    st.metric("Total de Kabulosos", st.session_state.db["total"])
    
    ranking = get_top_3()
    if ranking:
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, qtd) in enumerate(ranking):
            st.write(f"{medals[i]} {jogo}: **{qtd} votos**")
    else:
        st.write("Nenhum voto ainda!")

# --- 5. ÁREA DE LOGIN / CONTEÚDO ---
st.image("https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png")

if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    st.info("🎮 Entre com seu Nick para votar e ver a biblioteca!")
    nick = st.text_input("Nick:", key="login_input").strip()
    if st.button("PRESS START"):
        if nick:
            st.session_state.user = nick
            if nick not in st.session_state.db["usuarios"]:
                st.session_state.db["total"] += 1
                st.session_state.db["usuarios"].add(nick)
                salvar_dados(st.session_state.db)
            st.rerun()
else:
    st.success(f"Logado como: **{st.session_state.user}**")
    
    # Âncora para o link da barra lateral
    st.markdown('<div id="votar"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    # COLUNA 1: VOTAÇÃO
    with col1:
        st.header("🗳️ Próxima Live")
        opcoes = [
            "Pokémon Crystal (GBC)", "Phantasy Star (Master)", "Chrono Trigger (SNES)", 
            "Sonic CD (Sega CD)", "Nights into Dreams (Saturn)", "Metal Gear Solid (PS1)",
            "GoldenEye 007 (N64)", "Streets of Rage 2 (Mega Drive)"
        ]
        voto_selecionado = st.selectbox("Escolha o jogo:", sorted(opcoes), key="select_voto")
        
        if st.button("Confirmar Voto"):
            votos_atuais = st.session_state.db.get("votos", {})
            votos_atuais[voto_selecionado] = votos_atuais.get(voto_selecionado, 0) + 1
            st.session_state.db["votos"] = votos_atuais
            
            salvar_dados(st.session_state.db)
            st.balloons()
            st.toast(f"Voto em {voto_selecionado} registrado!", icon="✅")
            time.sleep(1)
            st.rerun()

    # COLUNA 2: BUSCA NA BIBLIOTECA
    with col2:
        st.header("📖 Busca Rápida")
        termo = st.text_input("Personagem ou Jogo:", key="input_busca").strip().lower()
        
        if termo:
            biblioteca = carregar_biblioteca_estatica()
            resultados = [
                p for p in biblioteca 
                if termo in p['nome'].lower() or termo in p['jogo'].lower()
            ]
            
            if resultados:
                st.write(f"🔍 Resultados ({len(resultados)}):")
                for r in resultados[:5]:
                    with st.expander(f"✨ {r['nome']}"):
                        st.caption(f"Jogo: {r['jogo']}")
                        st.write(f"**Função:** {r['papel']}")
                        st.write(f"**Golpes:** {r['golpe']}")
            else:
                st.warning("Nada encontrado!")
        else:
            st.caption("Digite para pesquisar...")
