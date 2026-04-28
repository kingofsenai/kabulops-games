import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games - Pokémon Edition", page_icon="⚡", layout="centered")

# Banco de Dados de Elite (6 Personagens por Franquia)
def carregar_personagens():
    return [
        # --- POKÉMON YELLOW (GEN 1 - GAME BOY) ---
        {"nome": "Pikachu (#025)", "jogo": "Pokémon Yellow", "papel": "Starter / Ícone", "caracteristica": "Electric Type - Choque do Trovão e Agilidade Máxima"},
        {"nome": "Charizard (#006)", "jogo": "Pokémon Yellow", "papel": "Fogo / Voar", "caracteristica": "Fire/Flying - Lança-chamas (Flamethrower) devastador"},
        {"nome": "Blastoise (#009)", "jogo": "Pokémon Yellow", "papel": "Água", "caracteristica": "Water Type - Hydro Pump e defesa impenetrável"},
        {"nome": "Venusaur (#003)", "jogo": "Pokémon Yellow", "papel": "Planta / Venenoso", "caracteristica": "Grass/Poison - Solar Beam e controle de status"},
        {"nome": "Mewtwo (#150)", "jogo": "Pokémon Yellow", "papel": "Lendário / Boss", "caracteristica": "Psychic Type - Amnesia e Psychic (O mais forte da Gen 1)"},
        {"nome": "Kabutops (#141)", "jogo": "Pokémon Yellow", "papel": "Fóssil / Guerreiro", "caracteristica": "Rock/Water - Lâminas afiadas e alta velocidade na água"},

        # --- MARIO BROS ---
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio de habilidades"},
        {"nome": "Luigi", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Salto mais alto que o Mario"},
        {"nome": "Bowser", "jogo": "Super Mario Bros", "papel": "Vilão Supremo", "caracteristica": "Força Bruta e sopro de fogo"},
        {"nome": "Peach", "jogo": "Super Mario Bros", "papel": "Princesa / Suporte", "caracteristica": "Capacidade de flutuar no ar"},
        {"nome": "Toad", "jogo": "Super Mario Bros", "papel": "Aliado", "caracteristica": "Alta velocidade de corrida"},
        {"nome": "Yoshi", "jogo": "Super Mario Bros", "papel": "Montaria", "caracteristica": "Língua extensível e saltos flutuantes"},

        # --- SONIC THE HEDGEHOG ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade supersônica"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Piloto / Gênio", "caracteristica": "Voo com caudas duplas"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Guardião", "caracteristica": "Planar e socos potentes"},
        {"nome": "Amy Rose", "jogo": "Sonic the Hedgehog", "papel": "Aliada", "caracteristica": "Piko Piko Hammer"},
        {"nome": "Shadow", "jogo": "Sonic the Hedgehog", "papel": "Anti-herói", "caracteristica": "Chaos Control e Teleporte"},
        {"nome": "Dr. Eggman", "jogo": "Sonic the Hedgehog", "papel": "Vilão", "caracteristica": "Intelecto de 300 de QI"},

        # --- RESIDENT EVIL / PS1 ---
        {"nome": "Leon S. Kennedy", "jogo": "Resident Evil 2", "papel": "Protagonista", "caracteristica": "Sobrevivência e precisão"},
        {"nome": "Claire Redfield", "jogo": "Resident Evil 2", "papel": "Protagonista", "caracteristica": "Determinação e busca por Chris"},
        {"nome": "Jill Valentine", "jogo": "Resident Evil", "papel": "Mestra das Chaves", "caracteristica": "Especialista em táticas S.T.A.R.S."},
        {"nome": "Chris Redfield", "jogo": "Resident Evil", "papel": "Atirador", "caracteristica": "Força física e combate"},
        {"nome": "Albert Wesker", "jogo": "Resident Evil", "papel": "Vilão", "caracteristica": "Estratégia e traição"},
        {"nome": "Ada Wong", "jogo": "Resident Evil 2", "papel": "Espiã", "caracteristica": "Agilidade e mistério"}
    ]

# Título e Interface
st.title("🎮 KABULOPS GAMES: POKÉDEX EDITION")
st.markdown("---")

nome_player = st.text_input("Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Bem-vindo, **{nome_player}**! Sistema Serebii Gen-1 integrado.")
    
    # Seção: Busca
    st.header("🔍 Busca de Lendas (Retro & Pokémon)")
    busca = st.text_input("Busque por Nome, Jogo ou Pokémon (ex: Kabutops, Pikachu):").strip().lower()
    
    if busca:
        personagens = carregar_personagens()
        # Filtro inteligente que busca no nome ou no jogo
        encontrados = [p for p in personagens if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        
        if encontrados:
            st.success(f"Encontramos {len(encontrados)} registros para sua busca!")
            for p in encontrados:
                with st.expander(f"📍 {p['nome']} - {p['jogo']}"):
                    st.write(f"**Classe:** {p['papel']}")
                    st.write(f"**Habilidade:** {p['caracteristica']}")
        else:
            st.error("Nenhuma lenda encontrada. Verifique a grafia!")

    # Seção: Enquete (12 Opções)
    st.markdown("---")
    st.header("📊 Votação: Qual merece a próxima Live?")
    
    opcoes_live = [
        "1. Pokémon Yellow (Game Boy)", "2. Phantasy Star (Master System)",
        "3. Zelda: A Link to the Past (SNES)", "4. Sonic the Hedgehog 2 (Mega)",
        "5. Super Mario World (SNES)", "6. Cotton 2 (Sega Saturn)",
        "7. Zelda: Ocarina of Time (N64)", "8. King of Fighters '98 (Neo Geo)",
        "9. Castlevania: SotN (PS1)", "10. Metal Gear Solid (PS1)",
        "11. Resident Evil 2 (PS1)", "12. Street Fighter II (Arcade)"
    ]
    
    voto = st.selectbox("Escolha o jogo:", opcoes_live)
    
    if st.button("Confirmar Voto"):
        st.balloons()
        st.success(f"🏆 Voto em **{voto}** registrado para {nome_player}!")

# Sidebar
st.sidebar.markdown("### Kabulops System v3.5")
st.sidebar.info("Base de Dados: Pokémon Gen 1 (Yellow)")
