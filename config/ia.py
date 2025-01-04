import streamlit as st
from huggingface_hub import InferenceClient

# Obtener el token
token = st.secrets['HF_TOKEN']

# Si se quiere asignar directamente habilitar la siguiente linea con tu token, y desahbilitar la anterior
# token = 'HF_TOKEN'
client = InferenceClient(api_key=token)

# Modelos
qwen_model = "Qwen/Qwen2.5-72B-Instruct"
