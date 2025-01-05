import streamlit as st

chat_page = st.Page("components/chat.py", title="Chat Con IA", icon=":material/smart_toy:")
local_page = st.Page("components/local.py", title="Ejemplo de Uso Transformers", icon=":material/ar_on_you:")
multi_page = st.Page("components/multimodelos.py", title="Varios Modelos", icon=":material/multiple_stop:")

pg = st.navigation([chat_page, local_page, multi_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()