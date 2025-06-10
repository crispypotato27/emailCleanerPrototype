import streamlit as st

st.set_page_config(page_title="Clean Up Settings", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first!")
    st.stop()

st.markdown("## Clean Up Settings")

if st.button("Set up a scheduled clean up"):
    st.switch_page("pages/ScheduleCleanUp.py")

if st.button("Back to Dashboard"):
    st.switch_page("pages/Dashboard.py")
