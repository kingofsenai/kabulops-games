# --- ENCICLOPÉDIA OTIMIZADA ---
    st.header("📖 Biblioteca de Personagens") # Palavra trocada conforme solicitado
    termo = st.text_input("Buscar por nome ou jogo:").lower()
    
    biblioteca = carregar_biblioteca_estatica()
    if termo:
        resultados = [p for p in biblioteca if termo in p['nome'].lower() or termo in p['jogo'].lower()]
        if resultados:
            for r in resultados:
                with st.expander(f"🔹 {r['nome']} ({r['jogo']})"):
                    st.write(f"**Papel:** {r['papel']}")
                    st.write(f"**Golpe:** {r['golpe']}")
        else:
            st.warning("Nenhum personagem encontrado.")
