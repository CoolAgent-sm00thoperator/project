import streamlit as st

st.set_page_config(page_title="My Web", layout="wide", page_icon=":cow:")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.container():
    st.title("Welcome To My Streamlit Website!")
    st.subheader("Hey! I am Aryan Kejriwal.")

st.write("##")
st.write("---")

with st.container():
    l_col, r_col = st.columns(2)
    with l_col:
        st.write("I am Left Column!")

    with r_col:
        st.write("I am Right Column!")
