@st.cache_data
def carregar_biblioteca_estatica():
    return [
        # --- GAME BOY COLOR (Exemplo: Pokémon Crystal / Zelda) ---
        {"nome": "Suicune", "jogo": "Pokémon Crystal", "papel": "Lendário", "golpe": "Aurora Beam"},
        {"nome": "Eusine", "jogo": "Pokémon Crystal", "papel": "Buscador", "golpe": "Estratégia Mística"},
        {"nome": "Link", "jogo": "Zelda: Oracle of Ages", "papel": "Herói", "golpe": "Harp of Ages"},
        {"nome": "Nayru", "jogo": "Zelda: Oracle of Ages", "papel": "Oráculo", "golpe": "Canto do Tempo"},
        {"nome": "Shantae", "jogo": "Shantae", "papel": "Meio-Gênio", "golpe": "Dança da Transformação"},
        {"nome": "Risky Boots", "jogo": "Shantae", "papel": "Vilã", "golpe": "Canhão Pirata"},
        {"nome": "Mario", "jogo": "Mario Tennis GBC", "papel": "Atleta", "golpe": "Super Saca"},
        {"nome": "Walrus", "jogo": "Metal Gear Ghost Babel", "papel": "Chefe", "golpe": "Metralhadora Pesada"},

        # --- MASTER SYSTEM (Exemplo: Phantasy Star / Wonder Boy) ---
        {"nome": "Alis Landale", "jogo": "Phantasy Star", "papel": "Protagonista", "golpe": "Espada de Luz"},
        {"nome": "Myau", "jogo": "Phantasy Star", "papel": "Guardião", "golpe": "Cura / Garras"},
        {"nome": "Odin", "jogo": "Phantasy Star", "papel": "Guerreiro", "golpe": "Machado de Ferro"},
        {"nome": "Noah", "jogo": "Phantasy Star", "papel": "Mago", "golpe": "Magia de Vento"},
        {"nome": "Wonder Boy", "jogo": "Wonder Boy III", "papel": "Herói", "golpe": "Transformação em Dragão"},
        {"nome": "Meka Dragon", "jogo": "Wonder Boy III", "papel": "Vilão", "golpe": "Sopro de Fogo"},
        {"nome": "Joe Musashi", "jogo": "Shinobi", "papel": "Ninja", "golpe": "Shuriken Storm"},
        {"nome": "Alex Kidd", "jogo": "Alex Kidd: Miracle World", "papel": "Mascote", "golpe": "Soco Janken"},

        # --- SNES (Exemplo: Chrono Trigger / Donkey Kong) ---
        {"nome": "Chrono", "jogo": "Chrono Trigger", "papel": "Herói", "golpe": "Cyclone / Luminaire"},
        {"nome": "Frog", "jogo": "Chrono Trigger", "papel": "Cavaleiro", "golpe": "Frog Squash"},
        {"nome": "Magus", "jogo": "Chrono Trigger", "papel": "Anti-Herói", "golpe": "Dark Matter"},
        {"nome": "Donkey Kong", "jogo": "Donkey Kong Country", "papel": "Líder", "golpe": "Ground Pound"},
        {"nome": "Diddy Kong", "jogo": "Donkey Kong Country", "papel": "Parceiro", "golpe": "Cartwheel Attack"},
        {"nome": "King K. Rool", "jogo": "Donkey Kong Country", "papel": "Vilão", "golpe": "Bala de Canhão"},
        {"nome": "Mega Man X", "jogo": "Mega Man X", "papel": "Hunter", "golpe": "X-Buster / Dash"},
        {"nome": "Zero", "jogo": "Mega Man X", "papel": "Lenda", "golpe": "Z-Saber"},

        # --- SEGA SATURN (Exemplo: Nights / Guardian Heroes) ---
        {"nome": "Nights", "jogo": "Nights into Dreams", "papel": "Espírito", "golpe": "Paraloop"},
        {"nome": "Reala", "jogo": "Nights into Dreams", "papel": "Rival", "golpe": "Ataque de Vácuo"},
        {"nome": "Han", "jogo": "Guardian Heroes", "papel": "Guerreiro", "golpe": "Espada de Fogo"},
        {"nome": "Serena", "jogo": "Guardian Heroes", "papel": "Clériga", "golpe": "Magia de Gelo"},
        {"nome": "Segata Sanshiro", "jogo": "Segata Sanshiro Shinkirou", "papel": "Mestre", "golpe": "Judô Explosivo"},
        {"nome": "Akira Yuki", "jogo": "Virtua Fighter 2", "papel": "Lutador", "golpe": "Tetsuzanko"},
        {"nome": "Pai Chan", "jogo": "Virtua Fighter 2", "papel": "Agilidade", "golpe": "Ensenki"},
        {"nome": "Leon", "jogo": "Resident Evil (Saturn)", "papel": "Policial", "golpe": "Tiro de Precisão"},

        # --- NINTENDO 64 (Exemplo: 007 / Banjo Kazooie) ---
        {"nome": "James Bond", "jogo": "GoldenEye 007", "papel": "Agente", "golpe": "PP7 Silenciada"},
        {"nome": "Alec Trevelyan", "jogo": "GoldenEye 007", "papel": "Vilão", "golpe": "Traição Tática"},
        {"nome": "Banjo", "jogo": "Banjo-Kazooie", "papel": "Urso Herói", "golpe": "Beak Buster"},
        {"nome": "Kazooie", "jogo": "Banjo-Kazooie", "papel": "Ave Suporte", "golpe": "Egg Firing"},
        {"nome": "Gruntilda", "jogo": "Banjo-Kazooie", "papel": "Bruxa Vilã", "golpe": "Feitiço de Rima"},
        {"nome": "Fox McCloud", "jogo": "Star Fox 64", "papel": "Líder", "golpe": "Barrel Roll"},
        {"nome": "Falco Lombardi", "jogo": "Star Fox 64", "papel": "Ás", "golpe": "Apoio Aéreo"},
        {"nome": "Wolf O'Donnell", "jogo": "Star Fox 64", "papel": "Rival", "golpe": "Wolfen Attack"},
    ]
