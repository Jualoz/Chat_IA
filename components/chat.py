from config.ia import client, qwen_model, verificar_token
import streamlit as st

if verificar_token():
    st.title("💬 Chatbot")

    # Inicialización del estado de sesión
    if "messages_one" not in st.session_state:
        st.session_state["messages_one"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Máximo número de mensajes en el historial
    MAX_HISTORY = 10

    # Mostrar mensajes previos
    for msg in st.session_state.messages_one:
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
            st.session_state.messages_one.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            # Generar respuesta con manejo de errores
            with st.spinner("Generando respuesta..."):
                try:
                    response = client.chat.completions.create(model=qwen_model, messages=st.session_state.messages_one)
                    msg = response.choices[0].message.content
                except Exception as e:
                    msg = "Hubo un error procesando tu solicitud. Por favor, intenta nuevamente."
                    st.error(f"Error: {e}")

            # Agregar mensaje del asistente al historial
            st.session_state.messages_one.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)

            # Optimización del historial
            if len(st.session_state.messages_one) > MAX_HISTORY:
                st.session_state.messages_one = st.session_state.messages_one[-MAX_HISTORY:]
        