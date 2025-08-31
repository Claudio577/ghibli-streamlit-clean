import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Catálogo Ghibli", layout="centered")
st.title("🎬 Catálogo do Studio Ghibli")

# Escolher o tipo de dado
tipo = st.selectbox(
    "O que você quer buscar?",
    ["films", "people", "species", "locations", "vehicles"]
)

# Entrada do usuário
query = st.text_input("Digite parte do título ou nome:")

# Só busca se o usuário digitar algo
if query:
    url = f"https://ghibliapi.vercel.app/{tipo}"
    resp = requests.get(url)

    if resp.status_code == 200:
        data = resp.json()

        # Filtrar resultados que contenham a palavra digitada
        resultados = [
            item for item in data
            if query.lower() in item.get("title", "").lower()
            or query.lower() in item.get("name", "").lower()
        ]

        # Mostrar resultados
        if resultados:
            for r in resultados:
                st.subheader(r.get("title") or r.get("name"))
                st.json(r)
                st.write("---")
        else:
            st.warning("Nenhum resultado encontrado 😕")
    else:
        st.error("Erro ao acessar a API do Ghibli.")
else:
    st.info("Digite algo na busca acima para começar 🔎")
