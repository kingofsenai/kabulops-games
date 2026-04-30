import streamlit as st
import time
import json
import os

# --- 1. CONFIGURAÇÃO (Sempre a primeira linha) ---
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# --- 2. SISTEMA DE DADOS ---
DB_FILE = "database_kabulops.json"

def carregar_dados():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            data["usuarios"] = set(data["usuarios"])
            return data
    return {"total": 0, "votos": {}, "usuarios": set()}

def salvar_dados(dados):
    dados_para_salvar = dados.copy()
    dados_para_salvar["usuarios"] = list(dados_para_salvar["usuarios"])
    with open(DB_FILE, "w") as f:
        json.dump(dados_para_salvar, f, indent=4)

if "db" not in st.session_state:
    st.session_state.db = carregar_dados()

db = st.session_state.db

def get_top_3():
    if not db["votos"]:
        return []
    return sorted(db["votos"].items(), key=lambda x: x[1], reverse=True)[:3]

# --- 3. BIBLIOTECA (Os 50 personagens) ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # --- BIBLIOTECA DE PERSONAGENS (COMPLETA - 62 REGISTROS) ---
@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # --- JOGOS DA ENQUETE (2 POR JOGO) ---
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

        # --- NOVOS: STREET FIGHTER II ---
        {"nome": "Ryu", "jogo": "Street Fighter II", "papel": "Lutador", "golpe": "Hadouken / Shoryuken"},
        {"nome": "Chun-Li", "jogo": "Street Fighter II", "papel": "Interpol", "golpe": "Hyakuretsu Kyaku / Spinning Bird Kick"},
        {"nome": "Guile", "jogo": "Street Fighter II", "papel": "Major", "golpe": "Sonic Boom / Flash Kick"},
        {"nome": "M. Bison", "jogo": "Street Fighter II", "papel": "Vilão", "golpe": "Psycho Crusher / Scissor Kick"},

        # --- NOVOS: MORTAL KOMBAT II ---
        {"nome": "Liu Kang", "jogo": "Mortal Kombat II", "papel": "Campeão", "golpe": "Dragon Fireball / Bicycle Kick"},
        {"nome": "Scorpion", "jogo": "Mortal Kombat II", "papel": "Espectro", "golpe": "Spear / Teleport Punch"},
        {"nome": "Sub-Zero", "jogo": "Mortal Kombat II", "papel": "Ninja", "golpe": "Ice Blast / Slide Attack"},
        {"nome": "Kitana", "jogo": "Mortal Kombat II", "papel": "Princesa", "golpe": "Fan Toss / Square Wave Punch"},

        # --- NOVOS: CADILLACS AND DINOSAURS ---
        {"nome": "Jack Tenrec", "jogo": "Cadillacs and Dinosaurs", "papel": "Mecânico", "golpe": "Dashing Uppercut / Slide Kick"},
        {"nome": "Hannah Dundee", "jogo": "Cadillacs and Dinosaurs", "papel": "Diplomata", "golpe": "Spinning Kick / Knife Mastery"},
        {"nome": "Mustapha Cairo", "jogo": "Cadillacs and Dinosaurs", "papel": "Engenheiro", "golpe": "Flying Kick / Tornado Kick"},
        {"nome": "Mess O'Bradovich", "jogo": "Cadillacs and Dinosaurs", "papel": "Gigante", "golpe": "Power Slam / Flying Body Press"},

        # --- POKÉMON (1ª GERAÇÃO) ---
        {"nome": "Kabutops", "jogo": "Pokémon Yellow/Red/Blue", "papel": "Fóssil", "golpe": "Slash / Hydro Pump"},
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Mascote", "golpe": "Thunderbolt / Quick Attack"},
        {"nome": "Charizard", "jogo": "Pokémon Red/Blue", "papel": "Fogo/Voador", "golpe": "Flamethrower / Fire Blast"},
        {"nome": "Blastoise", "jogo": "Pokémon Red/Blue", "papel": "Água", "golpe": "Hydro Pump / Skull Bash"},
        {"nome": "Venusaur", "jogo": "Pokémon Red/Blue", "papel": "Planta/Veneno", "golpe": "Solar Beam / Sleep Powder"},
        {"nome": "Mewtwo", "jogo": "Pokémon Red/Blue", "papel": "Psíquico", "golpe": "Psychic / Recover"},
        {"nome": "Gengar", "jogo": "Pokémon Red/Blue", "papel": "Fantasma", "golpe": "Shadow Ball / Confuse Ray"},
        {"nome": "Dragonite", "jogo": "Pokémon Red/Blue", "papel": "Dragão", "golpe": "Hyper Beam / Dragon Rage"},
        {"nome": "Snorlax", "jogo": "Pokémon Red/Blue", "papel": "Tanque", "golpe": "Body Slam / Rest"},
        {"nome": "Gyarados", "jogo": "Pokémon Red/Blue", "papel": "Água/Dragão", "golpe": "Dragon Dance / Hydro Pump"},
        {"nome": "Arcanine", "jogo": "Pokémon Red/Blue", "papel": "Fogo", "golpe": "Extreme Speed / Flare Blitz"},
        {"nome": "Alakazam", "jogo": "Pokémon Red/Blue", "papel": "Psíquico", "golpe": "Teleport / Psybeam"},

        # --- CLÁSSICOS NINTENDO (64/SNES) ---
        {"nome": "Mario", "jogo": "Super Mario 64", "papel": "Herói", "golpe": "Triple Jump / Ground Pound"},
        {"nome": "Link", "jogo": "Ocarina of Time", "papel": "Herói", "golpe": "Spin Attack / Din's Fire"},
        {"nome": "Fox McCloud", "jogo": "Star Fox 64", "papel": "Líder", "golpe": "Barrel Roll / Nova Bomb"},
        {"nome": "Donkey Kong", "jogo": "Donkey Kong 64", "papel": "Líder", "golpe": "Giant Punch / Coconut Cannon"},
        {"nome": "Samus Aran", "jogo": "Super Metroid", "papel": "Caçadora", "golpe": "Screw Attack / Ice Beam"},
        {"nome": "Yoshi", "jogo": "Yoshi's Island", "papel": "Aliado", "golpe": "Egg Throw / Flutter Jump"},
        {"nome": "Kirby", "jogo": "Kirby Super Star", "papel": "Herói", "golpe": "Copy Ability / Star Spit"},
        {"nome": "Captain Falcon", "jogo": "F-Zero X", "papel": "Piloto", "golpe": "Falcon Punch / Falcon Kick"},

        # --- CLÁSSICOS PLAYSTATION 1 ---
        {"nome": "Cloud Strife", "jogo": "Final Fantasy VII", "papel": "Mercenário", "golpe": "Omnislash / Cross-Slash"},
        {"nome": "Sephiroth", "jogo": "Final Fantasy VII", "papel": "Antagonista", "golpe": "Supernova / Octaslash"},
        {"nome": "Leon Kennedy", "jogo": "Resident Evil 2", "papel": "Policial", "golpe": "Shotgun Blast / Knife Strike"},
        {"nome": "Crash Bandicoot", "jogo": "Crash Bandicoot", "papel": "Mascote", "golpe": "Spin Attack / Body Slam"},
        {"nome": "Spyro", "jogo": "Spyro the Dragon", "papel": "Dragão", "golpe": "Flame Breath / Charge"},
        {"nome": "Jin Kazama", "jogo": "Tekken 3", "papel": "Lutador", "golpe": "Laser Scraper / Electric Wind"},
        {"nome": "Lara Croft", "jogo": "Tomb Raider", "papel": "Arqueóloga", "golpe": "Dual Pistols / Handstand"},

        # --- RETRÔ ARCADE / MASTER / MEGA ---
        {"nome": "Alex Kidd", "jogo": "Alex Kidd in Miracle World", "papel": "Príncipe", "golpe": "Janken Punch / Peticopter"},
        {"nome": "Mega Man X", "jogo": "Mega Man X", "papel": "Hunter", "golpe": "X-Buster / Dash Attack"},
        {"nome": "Zero", "jogo": "Mega Man X", "papel": "Hunter", "golpe": "Z-Saber / Ryuenjin"},
        {"nome": "Terry Bogard", "jogo": "Fatal Fury", "papel": "Lutador", "golpe": "Power Wave / Burn Knuckle"},
        {"nome": "Mai Shiranui", "jogo": "King of Fighters", "papel": "Kunoichi", "golpe": "Kacho Sen / Ryuubi no Mai"},
        {"nome": "Kyo Kusanagi", "jogo": "King of Fighters", "papel": "Lutador", "golpe": "Orochinagi / 100 Shiki"},
        {"nome": "Shinobi", "jogo": "The Revenge of Shinobi", "papel": "Ninja", "golpe": "Shuriken Throw / Mijin Jutsu"}
    ]

# --- 4. BARRA LATERAL (Com as 5 Pokébolas) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png", width=40)
    st.title("Kabulops Games")
    st.markdown("---")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png", width=40)
    st.markdown("#### **Pesquisa de Lives**")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png", width=40)
    st.markdown("#### **Seja um Kabuloso**")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/great-ball.png", width=40)
    st.markdown("#### **Biblioteca Retro**")
    
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png", width=40)
    st.markdown("#### **Configurações**")
    st.markdown("---")

    st.subheader("📊 Placar")
    st.metric("Players Online", db["total"])
    
    ranking = get_top_3()
    if ranking:
        medals = ["🥇", "🥈", "🥉"]
        for i, (jogo, qtd) in enumerate(ranking):
            st.markdown(f"{medals[i]} {jogo} ({qtd})")

# --- 5. CONTEÚDO PRINCIPAL ---
st.image("https://raw.githubusercontent.com/kingofsenai/kabulops-games/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png")

if 'user' not in st.session_state:
    st.session_state.user = None

# TELA DE LOGIN
if not st.session_state.user:
    nick = st.text_input("Digite seu Nick para entrar:", key="login_input")
    if st.button("PRESS START"):
        if nick:
            st.session_state.user = nick
            if nick not in db["usuarios"]:
                db["total"] += 1
                db["usuarios"].add(nick)
                salvar_dados(db)
            st.rerun()

# TELA PÓS-LOGIN (O que o usuário vê logado)
else:
    st.write(f"### Bem-vindo, **{st.session_state.user}**!")
    
    # ENQUETE
    st.header("🗳️ Qual Live você quer ver?")
    opcoes_consoles = [
        "Pokémon Crystal (GBC)", "Phantasy Star (Master)", "Chrono Trigger (SNES)", 
        "Sonic CD (Sega CD)", "Nights into Dreams (Saturn)", "Metal Gear Solid (PS1)",
        "GoldenEye 007 (N64)", "Streets of Rage 2 (Mega Drive)"
    ]
    voto = st.selectbox("Escolha seu jogo favorito:", sorted(opcoes_consoles))
    
    if st.button("Confirmar Voto"):
        db["votos"][voto] = db["votos"].get(voto, 0) + 1
        salvar_dados(db)
        st.balloons()
        st.success(f"Voto para {voto} registrado!")
        time.sleep(1)
        st.rerun()

    st.markdown("---")

    # BIBLIOTECA
    st.header("📖 Biblioteca de Personagens")
    termo = st.text_input("Busque personagens ou consoles:").lower()
    
    biblioteca = carregar_biblioteca_estatica()
    if termo:
        resultados = [p for p in biblioteca if termo in p['nome'].lower() or termo in p['jogo'].lower()]
        if resultados:
            for r in resultados:
                with st.expander(f"🔹 {r['nome']} - {r['jogo']}"):
                    st.write(f"**Papel:** {r['papel']}")
                    st.write(f"**Golpes:** {r['golpe']}")
        else:
            st.warning("Nenhum personagem encontrado com esse termo.")
    else:
        st.info("Digite o nome de um personagem ou console para pesquisar na biblioteca.")
