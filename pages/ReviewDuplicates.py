import streamlit as st

st.set_page_config(page_title="Review Junk Emails")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first!")
    st.stop()

st.title("📄 Review Duplicates Emails")
st.info("This page would display all junk emails for review. (Demo placeholder)")
