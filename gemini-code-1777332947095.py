import streamlit as st

# Configurações de Design
st.set_page_config(page_title="Kabulops Games", page_icon="🎮", layout="centered")

# Banco de Dados (Mantido 100%)
def carregar_personagens():
    return [
        # --- POKÉMON YELLOW (GEN 1) ---
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "caracteristica": "Electric Type - Choque do Trovão"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "caracteristica": "Fire/Flying - Lança-chamas"},
        {"nome": "Blastoise", "jogo": "Pokémon Yellow", "papel": "Defensor", "caracteristica": "Water Type - Hydro Pump"},
        {"nome": "Venusaur", "jogo": "Pokémon Yellow", "papel": "Suporte", "caracteristica": "Grass/Poison - Solar Beam"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "caracteristica": "Psychic Type - Amnesia/Psychic"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "caracteristica": "Rock/Water - Lâminas de Corte"},

        # --- SUPER MARIO BROS ---
        {"nome": "Mario", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Equilíbrio"},
        {"nome": "Luigi", "jogo": "Super Mario Bros", "papel": "Herói", "caracteristica": "Salto Alto"},
        {"nome": "Bowser", "jogo": "Super Mario Bros", "papel": "Vilão", "caracteristica": "Força Bruta"},
        {"nome": "Peach", "jogo": "Super Mario Bros", "papel": "Realeza", "caracteristica": "Flutuar"},
        {"nome": "Toad", "jogo": "Super Mario Bros", "papel": "Suporte", "caracteristica": "Velocidade"},
        {"nome": "Yoshi", "jogo": "Super Mario Bros", "papel": "Montaria", "caracteristica": "Língua Extensível"},

        # --- SONIC THE HEDGEHOG ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "caracteristica": "Velocidade"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Piloto", "caracteristica": "Voo Duplo"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Guardião", "caracteristica": "Planar e Escalar"},
        {"nome": "Amy Rose", "jogo": "Sonic the Hedgehog", "papel": "Aliada", "caracteristica": "Martelo Piko Piko"},
        {"nome": "Metal Sonic", "jogo": "Sonic the Hedgehog", "papel": "Rival", "caracteristica": "Cópia de Habilidades"},
        {"nome": "Dr. Robotnik", "jogo": "Sonic the Hedgehog", "papel": "Vilão", "caracteristica": "Máquinas Geniais"}
    ]

# --- BARRA LATERAL ESQUERDA (COM POKÉBOLAS ESPECIAIS) ---
with st.sidebar:
    st.title("⚫ Kabulops Games") # Representando a Luxury Ball (Preta/Ouro)
    st.markdown("---")
    st.write("### 🔮 Participe da Pesquisa") # Representando a Master Ball (Roxa)
    st.info("🟡 Torne-se um Kabuloso, inscreva-se no canal!") # Representando a Ultra Ball (Amarela)

# --- CONTEÚDO PRINCIPAL ---
st.title("🎮 CANAL KABULOPS GAMES")
st.markdown("---")

# 1ª ETAPA: NOME DO PLAYER
nome_player = st.text_input("[START] Qual é o seu nome, Player?", placeholder="Digite seu Nick...")

if nome_player:
    st.write(f"### Seja bem-vindo, **{nome_player}**!")
    st.markdown("---")

    # 2ª ETAPA: ENQUETE DE LIVE
    st.header("📊 Enquete de Live")
    st.write(f"{nome_player}, qual game merece uma live hoje?")
    
    opcoes_live = [
        "1. Pokémon Yellow (Game Boy)", "2. Phantasy Star (Master System)",
        "3. Zelda: A Link to the Past (SNES)", "4. Sonic the Hedgehog 2 (Mega Drive)",
        "5. Super Mario World (SNES)", "6. Cotton 2 (Sega Saturn)",
        "7. Zelda: Ocarina of Time (N64)", "8. King of Fighters '98 (Neo Geo)",
        "9. Castlevania: SotN (PS1)", "10. Metal Gear Solid (PS1)",
        "11. Resident Evil 2 (PS1)", "12. Street Fighter II (Arcade)"
    ]
    
    voto = st.selectbox("Escolha uma opção de 1 a 12:", opcoes_live)
    
    if st.button("Confirmar Voto"):
        st.balloons()
        st.success(f"🏆 VOTO REGISTRADO: {voto}")
        st.info(f"Valeu, {nome_player}! O feedback da comunidade é o nosso combustível.")

    st.markdown("---")

    # 3ª ETAPA: BUSCA DE PERSONAGEM
    st.header("🔍 Busca de Personagem")
    busca = st.text_input("Busque um título ou personagem (ex: Mario, Sonic, Pikachu):").strip().lower()
    
    if busca:
        personagens = carregar_personagens()
        encontrados = [p for p in personagens if busca in p['jogo'].lower() or busca in p['nome'].lower()]
        
        if encontrados:
            st.info(f"✅ Resultados para '{busca.capitalize()}':")
            for p in encontrados:
                with st.expander(f"📌 {p['nome']} ({p['jogo']})"):
                    st.write(f"**Papel:** {p['papel']}")
                    st.write(f"**Característica:** {p['caracteristica']}")
        else:
            st.warning(f"❌ O personagem ou jogo '{busca}' não foi localizado.")
