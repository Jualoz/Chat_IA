import streamlit as st

chat_page = st.Page("components/chat.py", title="Create entry", icon=":material/smart_toy:")
prueba_page = st.Page("config/ia.py", title="Create entry", icon=":material/smart_toy:")

pg = st.navigation([chat_page, prueba_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()