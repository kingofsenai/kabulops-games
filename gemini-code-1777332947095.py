import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# Banco de Dados de Personagens
def carregar_personagens():
    return [
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio e Salto"},
        {"nome": "Luigi", "jogo": "Super Mario Bros", "papel": "Coadjuvante", "caracteristica": "Salto Alto e Velocidade"},
        {"nome": "Bowser", "jogo": "Super Mario Bros", "papel": "Vilão", "caracteristica": "Força Bruta e Chamas"},
        {"nome": "Alex Kidd", "jogo": "Alex Kidd in Miracle World", "papel": "Herói", "caracteristica": "Agilidade"},
        {"nome": "Janken o Terrível", "jogo": "Alex Kidd in Miracle World", "papel": "Vilão", "caracteristica": "Pedra-Papel-Tesoura"},
        {"nome": "Alis Landale", "jogo": "Phantasy Star", "papel": "Heroína", "caracteristica": "Liderança"},
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade"},
        {"nome": "Dr. Robotnik", "jogo": "Sonic the Hedgehog", "papel": "Vilão", "caracteristica": "Intelecto genial"},
        {"nome": "Mega Man X", "jogo": "Mega Man X", "papel": "Herói", "caracteristica": "Evolução"},
        {"nome": "Sigma", "jogo": "Mega Man X", "papel": "Vilão", "caracteristica": "Persistência"},
        {"nome": "Terry Bogard", "jogo": "Fatal Fury / Neo Geo", "papel": "Herói", "caracteristica": "Carisma e Poder"},
        {"nome": "Geese Howard", "jogo": "Fatal Fury / Neo Geo", "papel": "Vilão", "caracteristica": "Autoridade e Contra-ataque"},
        {"nome": "Solid Snake", "jogo": "Metal Gear Solid", "papel": "Herói", "caracteristica": "Furtividade"},
        {"nome": "Leon S. Kennedy", "jogo": "Resident Evil 2", "papel": "Herói", "caracteristica": "Sobrevivência"}
    ]

# Cabeçalho Visual
st.title("🎮 CANAL KABULOPS GAMES")
st.subheader("Onde o Retro encontra o Código de Alto Nível")
st.markdown("---")

# Interação: Nome do Player
nome_player = st.text_input("Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Seja bem-vindo, **{nome_player}**!")
    
    # Seção: Busca de Lendas
    st.header("🔍 Busca de Lendas por Franquia")
    busca_jogo = st.text_input("Busque um título (ex: Mario, Sonic, Metal Gear):").strip().lower()
    
    if busca_jogo:
        personagens = carregar_personagens()
        encontrados = [p for p in personagens if busca_jogo in p['jogo'].lower() or busca_jogo in p['nome'].lower()]
        
        if encontrados:
            st.success(f"Resultados encontrados para '{busca_jogo.capitalize()}':")
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} ({p['jogo']})"):
                    st.write(f"**Status:** {p['papel']}")
                    st.write(f"**Skill:** {p['caracteristica']}")
        else:
            st.error(f"'{busca_jogo}' não foi localizado no banco de dados.")

    # Seção: Enquete de Live
    st.markdown("---")
    st.header("📊 Enquete: Qual game merece uma live?")
    
    opcoes_live = [
        "Phantasy Star (Master System)", "Zelda: A Link to the Past (SNES)",
        "Sonic the Hedgehog 2 (Mega Drive)", "Pokémon Red/Blue (Game Boy)",
        "Super Mario World (SNES)", "Cotton 2 (Sega Saturn)",
        "Zelda: Ocarina of Time (N64)", "King of Fighters '98 (Neo Geo)",
        "Castlevania: SotN (PS1)", "Metal Gear Solid (PS1)"
    ]
    
    voto = st.selectbox("Escolha seu jogo favorito:", opcoes_live)
    
    if st.button("Confirmar Voto"):
        st.balloons() # Efeito de comemoração
        st.success(f"🏆 VOTO REGISTRADO: {voto}")
        st.info(f"Valeu, {nome_player}! O feedback da comunidade é o nosso combustível.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("💻 **Kabulops System v2.0**")
st.sidebar.write("Desenvolvido por Kabulops")
