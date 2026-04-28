import streamlit as st

# ... (Mantenha as Configurações de Design e Banco de Dados iguais)

# --- CONFIGURAÇÃO DA BARRA LATERAL (URLs para garantir que não dê erro) ---
url_luxury = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/luxury-ball.png"
url_master = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
url_ultra  = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png"

# COLE AQUI O LINK DA SUA IMAGEM NO GITHUB (Botão 'Copy Raw' no GitHub)
# Exemplo: "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/NOME_DA_IMAGEM.jpg"
url_logo_kabulops = "COLE_AQUI_O_LINK_DA_IMAGEM_RAW" 

with st.sidebar:
    c1, c2 = st.columns([1, 2])
    with c1: st.image(url_luxury, width=70)
    with c2: st.markdown("### **Kabulops Games**")
    st.markdown("---")
    c3, c4 = st.columns([1, 2])
    with c3: st.image(url_master, width=70)
    with c4: st.markdown("### **Participe da Pesquisa**")
    st.markdown("---")
    c5, c6 = st.columns([1, 2])
    with c5: st.image(url_ultra, width=70)
    with c6: st.markdown("#### **Torne-se um Kabuloso!**")

# --- CONTEÚDO PRINCIPAL ---
# Usamos um bloco 'try/except' (o escudo do programador)
# Se a imagem falhar, o app não quebra; ele apenas mostra o título em texto.

try:
    col_v_esq, col_logo, col_v_dir = st.columns([1, 3, 1])
    with col_logo:
        # Tenta carregar a imagem pela URL ou pelo nome do arquivo
        st.image(https://github.com/kingofsenai/kabulops-games/blob/main/3a705bfa-a5e1-46fe-95c06-bdc5b1d9ac81.png, use_container_width=True)
except Exception:
    st.title("🎮 CANAL KABULOPS GAMES")

st.markdown("---")

# ... (Mantenha o restante dos filtros de Nome, Enquete e Busca)
