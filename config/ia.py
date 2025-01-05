import streamlit as st
from huggingface_hub import InferenceClient

# Obtener el token desde el estado de sesión
if "HF_TOKEN" not in st.session_state or not st.session_state["HF_TOKEN"]:
    raise ValueError("⚠️ El token de Hugging Face no está configurado. Configúralo antes de usar esta aplicación.")

token = st.session_state["HF_TOKEN"]

# Inicialización del cliente Hugging Face
client = InferenceClient(api_key=token)

# Modelos
qwen_model = "Qwen/Qwen2.5-72B-Instruct"
qwen_spanish = "Qwen/Qwen2.5-Coder-32B-Instruct"
sentiment = "sentiment-analysis"
flux_model = "black-forest-labs/FLUX.1-dev"


def verificar_token():
    if not st.session_state.get("HF_TOKEN"):
        st.sidebar.error("⚠️ Debes configurar tu token de Hugging Face para usar la aplicación.")
        return False
    return True