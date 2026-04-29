import streamlit as st
import pandas as pd
import json
import os
import time

# --- 1. CONFIGURAÇÕES E PERSISTÊNCIA ---
ARQUIVO_VOTOS = "votos_live.json"
NOME_APP = "ERICK SUPER DRUGSTORE"

def carregar_votos(opcoes):
    if os.path.exists(ARQUIVO_VOTOS):
        with open(ARQUIVO_VOTOS, "r") as f:
            return json.load(f)
    return {opcao: 0 for opcao in opcoes}

def salvar_voto_no_disco(votos):
    with open(ARQUIVO_VOTOS, "w") as f:
        json.dump(votos, f, indent=4)

# --- 2. DADOS DO SISTEMA (Métricas que você já usa) ---
# Mantendo o total de unidades que você corrigiu anteriormente
TOTAL_UNIDADES_ESTOQUE = 17475 
opcoes_live = ["Pokémon Yellow", "Resident Evil 1", "Crash Bandicoot", "Neo Geo Classics"]
votos_acumulados = carregar_votos(opcoes_live)

# --- 3. INTERFACE PRINCIPAL ---
st.set_page_config(page_title=NOME_APP, layout="wide")
st.title(f"🏪 {NOME_APP}")
st.write(f"Olá, operador! Bem-vindo ao painel de controle.")

# Sidebar com Métricas de Inventário
st.sidebar.header("Painel de Inventário")
st.sidebar.metric("Total em Estoque", f"{TOTAL_UNIDADES_ESTOQUE:,}".replace(",", "."))

# --- 4. ABA DE ENQUETE (Sua nova funcionalidade permanente) ---
st.markdown("---")
st.header("🗳️ Enquete de Live - Canal Kabulops")

col1, col2 = st.columns([1, 1])

with col1:
    voto = st.selectbox("Qual clássico vamos jogar na estreia?", sorted(opcoes_live))
    if st.button("Confirmar Voto"):
        votos_acumulados[voto] = votos_acumulados.get(voto, 0) + 1
        salvar_voto_no_disco(votos_acumulados)
        st.balloons()
        st.snow()
        st.success(f"Voto para {voto} gravado permanentemente!")
        time.sleep(1)
        st.rerun()

with col2:
    st.subheader("Placar em Tempo Real")
    # Exibe os resultados em uma tabela simples
    df_votos = pd.DataFrame(list(votos_acumulados.items()), columns=['Jogo', 'Votos'])
    st.table(df_votos.set_index('Jogo'))

st.markdown("---")
# Aqui você pode continuar colando o restante das suas funções de busca/filtros
