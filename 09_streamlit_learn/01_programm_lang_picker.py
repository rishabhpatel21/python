import streamlit as st  # type: ignore

language = st.selectbox('Select a programming language', ['Python', 'R', 'Java', 'C++', 'JavaScript'])

st.success(f'You selected {language} language')
