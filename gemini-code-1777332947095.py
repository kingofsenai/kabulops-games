import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games - Ultra Edition", page_icon="🎮", layout="centered")

# Banco de Dados Expandido (Power Up Ativado)
def carregar_personagens():
    return [
        # --- POKÉMON (GEN 1 - YELLOW VERSION) ---
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Protagonista", "caracteristica": "Choque do Trovão e Agilidade"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Aliado/Evolução", "caracteristica": "Lança-chamas e Voar"},
        {"nome": "Blastoise", "jogo": "Pokémon Yellow", "papel": "Aliado/Evolução", "caracteristica": "Canhão d'Água e Defesa"},
        {"nome": "Venusaur", "jogo": "Pokémon Yellow", "papel": "Aliado/Evolução", "caracteristica": "Raio Solar e Controle"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lenda/Boss", "caracteristica": "Poder Psíquico Supremo"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Fóssil/Guerreiro", "caracteristica": "Lâminas de Corte e Velocidade na Água"},

        # --- SUPER MARIO BROS ---
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio"},
        {"nome": "Luigi", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Salto Alto"},
        {"nome": "Bowser", "jogo": "Super Mario Bros", "papel": "Vilão", "caracteristica": "Força Bruta"},
        {"nome": "Peach", "jogo": "Super Mario Bros", "papel": "Realeza", "caracteristica": "Flutuar"},
        {"nome": "Toad", "jogo": "Super Mario Bros", "papel": "Suporte", "caracteristica": "Velocidade"},
        {"nome": "Yoshi", "jogo": "Super Mario Bros", "papel": "Montaria", "caracteristica": "Língua Extensível"},

        # --- SONIC THE HEDGEHOG ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade da Luz"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Genio/Piloto", "caracteristica": "Voo Duplo"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Rival/Aliado", "caracteristica": "Planar e Escalar"},
        {"nome": "Amy Rose", "jogo": "Sonic the Hedgehog", "papel": "Aliada", "caracteristica": "Martelo Piko Piko"},
        {"nome": "Metal Sonic", "jogo": "Sonic the Hedgehog", "papel": "Rival Robô", "caracteristica": "Cópia de Habilidades"},
        {"nome": "Dr. Robotnik", "jogo": "Sonic the Hedgehog", "papel": "Vilão", "caracteristica": "Maquinário Genial"},

        # --- MEGA MAN X ---
        {"nome": "Mega Man X", "jogo": "Mega Man X", "papel": "Herói", "caracteristica": "Upgrade de Armadura"},
        {"nome": "Zero", "jogo": "Mega Man X", "papel": "Mentor", "caracteristica": "Z-Saber e Agilidade"},
        {"nome": "Sigma", "jogo": "Mega Man X", "papel": "Vilão", "caracteristica": "Evolução Viral"},
        {"nome": "Vile", "jogo": "Mega Man X", "papel": "Rival", "caracteristica": "Armamento Pesado"},
        {"nome": "Axl", "jogo": "Mega Man X", "papel": "Atirador", "caracteristica": "Cópia de Forma"},
        {"nome": "Iris", "jogo": "Mega Man X", "papel": "Suporte", "caracteristica": "Navegação e Inteligência"}
    ]

# Título
st.title("🎮 KABULOPS GAMES: ULTRA VERSION")
st.markdown("---")

# Interação: Nome do Player
nome_player = st.text_input("Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Bem-vindo, **{nome_player}**! O sistema está atualizado.")
    
    # Seção: Busca
    st.header("🔍 Enciclopédia de Lendas")
    busca = st.text_input("Busque por Jogo, Personagem ou Pokémon:").strip().lower()
    
    if busca:
        dados = carregar_personagens()
        encontrados = [p for p in dados if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        
        if encontrados:
            st.success(f"Foram encontrados {len(encontrados)} registros.")
            for p in encontrados:
                with st.expander(f"📍 {p['nome']} ({p['jogo']})"):
                    st.write(f"**Classe:** {p['papel']}")
                    st.write(f"**Poder Principal:** {p['caracteristica']}")
        else:
            st.error("Nenhuma lenda encontrada com esse nome.")

    # Seção: Enquete de Live (12 Opções)
    st.markdown("---")
    st.header("📊 Votação da Comunidade")
    
    opcoes_live = [
        "1. Pokémon Yellow (Game Boy)",
        "2. Phantasy Star (Master System)",
        "3. Zelda: A Link to the Past (SNES)",
        "4. Sonic the Hedgehog 2 (Mega Drive)",
        "5. Super Mario World (SNES)",
        "6. Cotton 2 (Sega Saturn)",
        "7. Zelda: Ocarina of Time (N64)",
        "8. King of Fighters '98 (Neo Geo)",
        "9. Castlevania: SotN (PS1)",
        "10. Metal Gear Solid (PS1)",
        "11. Resident Evil 2 (PS1)",
        "12. Street Fighter II (Arcade)"
    ]
    
    voto = st.selectbox("Qual o próximo jogo da live?", opcoes_live)
    
    if st.button("Confirmar Voto"):
        st.balloons()
        st.success(f"🏆 {nome_player}, seu voto em **{voto}** foi processado!")

# Sidebar
st.sidebar.markdown("### Kabulops System v3.0")
st.sidebar.info("Base de dados: Expandida ✅")
st.sidebar.write("Foco: Pokémon Gen 1 & Clássicos Retro")
