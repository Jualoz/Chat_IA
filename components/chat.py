from config.ia import client, qwen_model
import streamlit as st

# Configuración inicial del título
st.title("💬 Chatbot")

# Inicialización del estado de sesión
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Máximo número de mensajes en el historial
MAX_HISTORY = 10

# Mostrar mensajes previos
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Validación de la entrada
    if len(prompt.strip()) == 0:
        st.warning("El mensaje no puede estar vacío.")
    elif len(prompt) > 1000:
        st.warning("El mensaje es demasiado largo.")
    else:
        # Agregar mensaje del usuario al historial
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Generar respuesta con manejo de errores
        with st.spinner("Generando respuesta..."):
            try:
                response = client.chat.completions.create(model=qwen_model, messages=st.session_state.messages)
                msg = response.choices[0].message.content
            except Exception as e:
                msg = "Hubo un error procesando tu solicitud. Por favor, intenta nuevamente."
                st.error(f"Error: {e}")

        # Agregar mensaje del asistente al historial
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

        # Optimización del historial
        if len(st.session_state.messages) > MAX_HISTORY:
            st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]
