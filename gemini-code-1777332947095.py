import streamlit as st
import json
import os
import time

# --- PERSISTÊNCIA DE DADOS DO CANAL ---
ARQUIVO_VOTOS = "votos_kabulops.json"

def carregar_votos(opcoes):
    if os.path.exists(ARQUIVO_VOTOS):
        with open(ARQUIVO_VOTOS, "r") as f:
            return json.load(f)
    return {opcao: 0 for opcao in opcoes}

def salvar_voto(votos):
    with open(ARQUIVO_VOTOS, "w") as f:
        json.dump(votos, f, indent=4)

# --- CONFIGURAÇÃO DA LIVE ---
st.set_page_config(page_title="Kabulops Games - Retro Live", page_icon="🦖")

# Lista de clássicos que você costuma trazer
opcoes_live = [
    "Pokémon Yellow (GBC)", 
    "Mega Man X4 (PS1)", 
    "Super Mario 64 (N64)", 
    "Metal Slug (Neo Geo)",
    "Alex Kidd (Master System)"
]

votos_acumulados = carregar_votos(opcoes_live)

# --- INTERFACE DO CANAL ---
st.title("🦖 Kabulops Games")
st.subheader("Onde os clássicos nunca morrem!")

st.markdown("---")

# --- ENQUETE COM PERSISTÊNCIA ---
st.header("🗳️ Escolha o jogo da próxima Live")

col1, col2 = st.columns(2)

with col1:
    voto = st.selectbox("Qual desses você quer ver no canal?", sorted(opcoes_live))
    
    if st.button("Confirmar Voto"):
        # Atualiza e salva no JSON na hora
        votos_acumulados[voto] = votos_acumulados.get(voto, 0) + 1
        salvar_voto(votos_acumulados)
        
        # Feedback visual para a live
        st.balloons()
        st.snow()
        st.success(f"Voto para {voto} registrado para sempre!")
        time.sleep(1)
        st.rerun()

with col2:
    st.write("### Placar Atual")
    # Exibindo os votos de forma organizada
    for jogo in sorted(votos_acumulados.keys()):
        qtd = votos_acumulados[jogo]
        # Barra de progresso visual para o placar
        st.write(f"**{jogo}**: {qtd} votos")
        st.progress(min(qtd / 50, 1.0)) # Ajuste o 50 para sua meta de votos

st.markdown("---")

# Espaço para curiosidades (que você adora colocar)
with st.expander("💡 Curiosidade Retro do Dia"):
    st.info("Você sabia que o Kabutops é inspirado em um Artrópode extinto chamado Trilobita?")
