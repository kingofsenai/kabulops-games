def carregar_personagens():
    return [
        # --- POKÉMON YELLOW ---
        {"nome": "Pikachu", "jogo": "Pokémon Yellow", "papel": "Starter", "golpe": "Thunderbolt (Choque do Trovão)"},
        {"nome": "Kabutops", "jogo": "Pokémon Yellow", "papel": "Guerreiro", "golpe": "Slash (Lâminas de Corte)"},
        {"nome": "Charizard", "jogo": "Pokémon Yellow", "papel": "Atacante", "golpe": "Flamethrower (Lança-chamas)"},
        {"nome": "Mewtwo", "jogo": "Pokémon Yellow", "papel": "Lendário", "golpe": "Psychic (Poder Psíquico)"},
        {"nome": "Blue (Rival)", "jogo": "Pokémon Yellow", "papel": "Rival", "golpe": "Evolução Estratégica"},

        # --- STREET FIGHTER II ---
        {"nome": "Ryu", "jogo": "Street Fighter II", "papel": "Protagonista", "golpe": "Hadouken"},
        {"nome": "Ken Masters", "jogo": "Street Fighter II", "papel": "Rival", "golpe": "Shoryuken"},
        {"nome": "Chun-Li", "jogo": "Street Fighter II", "papel": "Velocidade", "golpe": "Hyakuretsu Kyaku"},
        {"nome": "Guile", "jogo": "Street Fighter II", "papel": "Defensivo", "golpe": "Sonic Boom"},
        {"nome": "M. Bison", "jogo": "Street Fighter II", "papel": "Vilão Final", "golpe": "Psycho Crusher"},

        # --- RESIDENT EVIL 2 ---
        {"nome": "Leon S. Kennedy", "jogo": "Resident Evil 2", "papel": "Policial Novato", "golpe": "Precisão com Pistola"},
        {"nome": "Claire Redfield", "jogo": "Resident Evil 2", "papel": "Sobrevivente", "golpe": "Lança-Granadas"},
        {"nome": "Ada Wong", "jogo": "Resident Evil 2", "papel": "Espiã", "golpe": "Grappling Gun"},
        {"nome": "Sherry Birkin", "jogo": "Resident Evil 2", "papel": "Protegida", "golpe": "Furtividade"},
        {"nome": "Mr. X (Tyrant)", "jogo": "Resident Evil 2", "papel": "Perseguidor", "golpe": "Soco Devastador"},

        # --- CASTLEVANIA: SOTN ---
        {"nome": "Alucard", "jogo": "Castlevania: SotN", "papel": "Protagonista", "golpe": "Soul Steal / Morcego"},
        {"nome": "Richter Belmont", "jogo": "Castlevania: SotN", "papel": "Caçador de Vampiros", "golpe": "Grand Cross"},
        {"nome": "Maria Renard", "jogo": "Castlevania: SotN", "papel": "Invocadora", "golpe": "Guardian Knuckle"},
        {"nome": "Dracula", "jogo": "Castlevania: SotN", "papel": "Vilão Final", "golpe": "Dark Metamorphosis"},
        {"nome": "Death (Morte)", "jogo": "Castlevania: SotN", "papel": "Ceifador", "golpe": "Foice de Almas"},

        # --- METAL GEAR SOLID ---
        {"nome": "Solid Snake", "jogo": "Metal Gear Solid", "papel": "Agente Lendário", "golpe": "CQC / Stealth"},
        {"nome": "Meryl Silverburgh", "jogo": "Metal Gear Solid", "papel": "Aliada", "golpe": "Atiradora"},
        {"nome": "Hal 'Otacon' Emmerich", "jogo": "Metal Gear Solid", "papel": "Suporte Técnico", "golpe": "Hackeamento"},
        {"nome": "Liquid Snake", "jogo": "Metal Gear Solid", "papel": "Antagonista", "golpe": "Liderança de Elite"},
        {"nome": "Psycho Mantis", "jogo": "Metal Gear Solid", "papel": "Místico", "golpe": "Telecinese (Lê seu Memory Card)"},

        # --- CRASH BANDICOOT 3 ---
        {"nome": "Crash", "jogo": "Crash Bandicoot 3", "papel": "Herói", "golpe": "Spin Attack (Giro)"},
        {"nome": "Coco Bandicoot", "jogo": "Crash Bandicoot 3", "papel": "Gênia da Computação", "golpe": "Ataque com Laptop"},
        {"nome": "Aku Aku", "jogo": "Crash Bandicoot 3", "papel": "Protetor", "golpe": "Invencibilidade Temporal"},
        {"nome": "Dr. Neo Cortex", "jogo": "Crash Bandicoot 3", "papel": "Cientista Maluco", "golpe": "Raio Laser"},
        {"nome": "Tiny Tiger", "jogo": "Crash Bandicoot 3", "papel": "Força Bruta", "golpe": "Salto Esmagador"},

        # --- FINAL FANTASY VII ---
        {"nome": "Cloud Strife", "jogo": "Final Fantasy VII", "papel": "Ex-SOLDIER", "golpe": "Omnislash (Braver)"},
        {"nome": "Tifa Lockhart", "jogo": "Final Fantasy VII", "papel": "Lutadora", "golpe": "Final Heaven"},
        {"nome": "Aerith Gainsborough", "jogo": "Final Fantasy VII", "papel": "Mística", "golpe": "Great Gospel"},
        {"nome": "Barret Wallace", "jogo": "Final Fantasy VII", "papel": "Líder da AVALANCHE", "golpe": "Big Shot"},
        {"nome": "Sephiroth", "jogo": "Final Fantasy VII", "papel": "Anjo de uma Asa", "golpe": "Super Nova"},

        # --- TEKKEN 3 ---
        {"nome": "Jin Kazama", "jogo": "Tekken 3", "papel": "Protagonista", "golpe": "Laser Scraper"},
        {"nome": "Ling Xiaoyu", "jogo": "Tekken 3", "papel": "Agilidade", "golpe": "Storming Flower"},
        {"nome": "Hwoarang", "jogo": "Tekken 3", "papel": "Taekwondo", "golpe": "Sky Rocket"},
        {"nome": "Eddy Gordo", "jogo": "Tekken 3", "papel": "Capoeira", "golpe": "Roda Gigante"},
        {"nome": "Heihachi Mishima", "jogo": "Tekken 3", "papel": "Lenda", "golpe": "Electric Wind God Fist"},
        
        # --- SONIC, MARIO, MORTAL KOMBAT e ALEX KIDD (Já incluídos na anterior) ---
        {"nome": "Sonic", "jogo": "Sonic the Hedgehog", "papel": "Herói", "golpe": "Spin Dash"},
        {"nome": "Tails", "jogo": "Sonic the Hedgehog", "papel": "Apoio", "golpe": "Voo"},
        {"nome": "Knuckles", "jogo": "Sonic the Hedgehog", "papel": "Força", "golpe": "Planar"},
        {"nome": "Amy Rose", "jogo": "Sonic the Hedgehog", "papel": "Martelo", "golpe": "Piko Piko Hammer"},
        {"nome": "Dr. Eggman", "jogo": "Sonic the Hedgehog", "papel": "Vilão", "golpe": "E-Mech"},
    ]
