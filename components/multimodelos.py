from config.ia import client, qwen_spanish, flux_model, verificar_token
from huggingface_hub import InferenceClient
import streamlit as st

# Verificar y usar el token
if verificar_token():
    # Inicialización del cliente Hugging Face
    token = st.session_state["HF_TOKEN"]
    image_client = InferenceClient(model=flux_model, token=token)

    st.title("💬 Chatbot con Generación de Imágenes")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "¿En qué puedo ayudarte hoy? Usa 'imagen' o 'dibuja' para generar una imagen."}
        ]

    MAX_HISTORY = 10

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Escribe tu mensaje aquí..."):
        if len(prompt.strip()) == 0:
            st.warning("El mensaje no puede estar vacío.")
        elif len(prompt) > 1000:
            st.warning("El mensaje es demasiado largo.")
        else:
            st.session_state["messages"].append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            if "imagen" in prompt.lower() or "dibuja" in prompt.lower():
                with st.spinner("Generando imagen basada en tu descripción..."):
                    message = [
                        {"role": "system", "content": "Eres un experto en ingeniería de prompts. Ayuda a optimizar descripciones."},
                        {"role": "user", "content": f"Mejora el siguiente prompt: '{prompt}'. Dame solo el texto en inglés, optimizado para generar una imagen."}
                    ]
                    try:
                        response = client.chat.completions.create(model=qwen_spanish, messages=message)
                        improved_prompt = response.choices[0].message.content.strip()
                        image = image_client.text_to_image(improved_prompt)
                        st.image(image, caption="Imagen generada", use_container_width=True)
                        msg = "Aquí tienes la imagen generada según tu solicitud."
                    except Exception as e:
                        st.error(f"Error al generar la imagen: {e}")
            else:
                with st.spinner("Procesando tu solicitud..."):
                    try:
                        response = client.chat.completions.create(model=qwen_spanish, messages=st.session_state["messages"])
                        msg = response.choices[0].message.content
                    except Exception as e:
                        msg = "Hubo un error procesando tu solicitud. Inténtalo de nuevo."
                        st.error(f"Error: {e}")

            st.session_state["messages"].append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)

            if len(st.session_state["messages"]) > MAX_HISTORY:
                st.session_state["messages"] = st.session_state["messages"][-MAX_HISTORY:]
