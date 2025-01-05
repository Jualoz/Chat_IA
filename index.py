import streamlit as st

# Crear páginas
chat_page = st.Page("components/chat.py", title="Chat Con IA", icon=":material/smart_toy:")
local_page = st.Page("components/local.py", title="Ejemplo de Uso Transformers", icon=":material/ar_on_you:")
multi_page = st.Page("components/multimodelos.py", title="Varios Modelos", icon=":material/multiple_stop:")

# Configuración inicial
st.set_page_config(page_title="Jualoz Chatbot", page_icon=":material/business_messages:")

# Token en estado de sesión
if "HF_TOKEN" not in st.session_state:
    st.session_state["HF_TOKEN"] = ""

# Barra lateral para configurar el token
with st.sidebar:
    with st.expander("Configurar Token HF"):
        token_input = st.text_input("Introduce tu token de Hugging Face:", type="password")
        if st.button("Guardar Token"):
            if token_input:
                st.session_state["HF_TOKEN"] = token_input
                st.success("Token guardado correctamente.")
            else:
                st.error("El token no puede estar vacío.")

# Verificar si hay un token configurado antes de continuar
if not st.session_state["HF_TOKEN"]:
    st.error("⚠️ Debes configurar tu token en la barra lateral antes de usar la aplicación.")
else:
    # Navegación
    pg = st.navigation([chat_page, local_page, multi_page])
    pg.run()
