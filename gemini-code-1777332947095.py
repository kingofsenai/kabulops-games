import streamlit as st
import json
import os
import time

# --- LOGICA DE PERSISTÊNCIA ---
ARQUIVO_VOTOS = "votos_live.json"

def carregar_votos():
    if os.path.exists(ARQUIVO_VOTOS):
        with open(ARQUIVO_VOTOS, "r") as f:
            return json.load(f)
    # Se o arquivo não existir, inicia com 0 para as opções conhecidas
    return {opcao: 0 for opcao in opcoes_live}

def salvar_voto_no_disco(votos):
    with open(ARQUIVO_VOTOS, "w") as f:
        json.dump(votos, f, indent=4)

# --- CONFIGURAÇÃO INICIAL ---
opcoes_live = ["Pokémon Yellow", "Resident Evil 1", "Crash Bandicoot", "Sonic the Hedgehog"] # Suas opções aqui
votos_acumulados = carregar_votos()

# --- ENQUETE COM CORREÇÃO DE ANIMAÇÃO ---
st.header("🗳️ Enquete de Live")
voto = st.selectbox("Qual clássico você gostaria de assistir em nossa primeira live?", sorted(opcoes_live))

if st.button("Confirmar Voto"):
    # Atualiza o dicionário local
    votos_acumulados[voto] = votos_acumulados.get(voto, 0) + 1
    
    # SALVA NO ARQUIVO (Isso garante que seja permanente)
    salvar_voto_no_disco(votos_acumulados)
    
    # Efeito visual
    st.balloons()
    st.snow() 
    st.success(f"✅ Voto computado: {voto}!")
    
    time.sleep(1)
    st.rerun()

st.markdown("---")

# Opcional: Mostrar os resultados atuais para você acompanhar
st.subheader("Resultados Parciais")
for jogo, qtd in votos_acumulados.items():
    st.write(f"**{jogo}**: {qtd} votos")
