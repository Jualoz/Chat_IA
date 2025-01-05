# **Chatbot Multimodal con IA**

Este proyecto es un sistema de chat que combina generación de texto, clasificación de sentimientos y generación de imágenes utilizando modelos de Hugging Face y Streamlit.

Si deseas probar el proyecto directamente, puedes hacerlo en el siguiente enlace: [Chatbot Multimodal](https://chatbot-jualoz.streamlit.app). Solo necesitas ingresar tu token de Hugging Face en la configuración.

---

## **Estructura del Proyecto**

- **Chat de Generación de Texto:** Un asistente de texto que responde a las consultas del usuario usando modelos avanzados de lenguaje.
- **Chat de Clasificación de Sentimientos:** Clasifica el sentimiento de un texto proporcionado por el usuario (positivo, negativo o neutro).
- **Chat de Generación de Texto e Imágenes:** Genera texto e imágenes que se complementan, como mejorar descripciones de texto y crear imágenes basadas en estas.

---

## **Requisitos Previos**

### **1. Instalar Python**

Asegúrate de tener Python 3.10 instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### **2. Crear un Entorno Virtual**

Crea un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```

### **3. Instalar Dependencias**

Ejecuta el siguiente comando para instalar todas las librerías necesarias (Despues de clonar el repositorio):

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```
streamlit
huggingface_hub
transformers
```

---

## **Configuración del Proyecto**

### **1. Clonar el Repositorio**

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Jualoz/Chat_IA.git
cd Chat_IA
```

### **2. Obtener el Token de Hugging Face**

1. Crea una cuenta en [Hugging Face](https://huggingface.co/).
2. Ve a tu perfil y genera un token de acceso personal desde la sección **Access Tokens**.
3. Copia el token generado.

### **3. Configurar el Token en el Proyecto**

1. Inicia el proyecto con el siguiente comando:
   ```bash
   streamlit run index.py
   ```
2. En la barra lateral, introduce el token en la sección **Configurar Token HF** y haz clic en **Guardar Token**.

---

## **Cómo Usar el Proyecto**

### **1. Chat de Generación de Texto**

1. Ve a la página **Chat Con IA**.
2. Escribe una consulta en el campo de entrada.
3. El modelo responderá basándose en tu entrada.

### **2. Chat de Clasificación de Sentimientos**

1. Ve a la página **Ejemplo de Uso Transformers**.
2. Escribe una frase para analizar su sentimiento.
3. El sistema clasificará el texto como positivo, negativo o neutro.

### **3. Chat de Generación de Texto e Imágenes**

1. Ve a la página **Varios Modelos**.
2. Escribe un mensaje que contenga palabras como "imagen" o "dibuja".
3. El sistema optimizará el texto para la generación de imágenes y creará una imagen basada en la descripción.
4. La imagen se mostrará en pantalla junto con el texto generado.

#### **Diagrama de Funcionamiento**

El siguiente diagrama explica el flujo del tercer chat:

1. **Entrada del Usuario:** El usuario proporciona un mensaje.
2. **Optimización del Texto:** El sistema mejora el mensaje para optimizarlo para la generación de imágenes.
3. **Generación de Imagen:** Se utiliza el modelo seleccionado para crear la imagen.
4. **Resultado:** Se muestra el texto optimizado y la imagen generada al usuario.

![Diagrama de Funcionamiento](./assets/diagrama.drawio)

---

## **Solución de Problemas**

### **1. Error: "El token no es válido"**

- Asegúrate de haber introducido un token válido en la barra lateral.

### **2. Error: "Failed to load model"**

- Verifica que las dependencias están correctamente instaladas.
- Asegúrate de que tienes conexión a internet para acceder a los modelos de Hugging Face.

### **3. Imagen no Generada**

- Verifica que el prompt enviado es claro y específico para la generación de imágenes.
- Asegúrate de que el modelo de imágenes (`black-forest-labs/FLUX.1-dev`) está correctamente configurado.

---

## **Notas Adicionales**

- Los modelos usados incluyen:
  - `Qwen/Qwen2.5-Coder-32B-Instruct` para generación de texto.
  - `sentiment-analysis` para análisis de sentimientos.
  - `black-forest-labs/FLUX.1-dev` para generación de imágenes.
- El historial de mensajes se limita a los últimos 10 intercambios para optimizar el rendimiento.

---

¡Gracias por usar este chatbot multimodal! Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio. 🎉
