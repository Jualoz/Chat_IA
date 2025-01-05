from transformers import pipeline
import streamlit as st
from config.ia import sentiment

# Inicializa el modelo de análisis de sentimientos
classifier = pipeline(sentiment)

st.title("Análisis de Sentimientos")
st.write("Esta aplicación utiliza el modelo de Transformers para analizar el sentimiento de un texto. (Realiza el promt en ingles)")

user_input = st.text_area("Escribe un texto para analizar:", "We are very happy to show you the 🤗 Transformers library.")

if st.button("Analizar Sentimiento"):
    with st.spinner("Generando respuesta..."):
        try:
            response = classifier(user_input)
            result = response[0]  # primer resultado
        except Exception as e:
            msg = "Hubo un error procesando tu solicitud. Por favor, intenta nuevamente."
            st.error(f"Error: {e}")

    # Analiza el texto ingresado
    
    # Formatea los resultados
    label = result['label']
    score = result['score']

    # Asigna según el sentimiento
    if label == "POSITIVE":
        st.success(f"🎉 Sentimiento Positivo con una confianza del {score:.2%}")
    elif label == "NEGATIVE":
        st.error(f"😔 Sentimiento Negativo con una confianza del {score:.2%}")
    else:
        st.warning(f"😐 Sentimiento {label} con una confianza del {score:.2%}")
