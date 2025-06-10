import streamlit as st
import time

st.set_page_config(page_title="Scan Emails", layout="centered")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first!")
    st.stop()

st.title("📧 Scan Emails")
st.subheader("Scanning inbox for subscriptions...")

progress_bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.02)
    progress_bar.progress(i)

include_unsubscribed = st.checkbox("Include unsubscribed emails", value=True)
filter_days = st.number_input("Filter emails older than", min_value=0, max_value=365, value=30, step=1)

if st.button("Cancel"):
    st.info("Scan canceled. Returning to dashboard...")
    time.sleep(1)
    st.switch_page("pages/Dashboard.py")

if st.button("Done"):
    st.success("Scan completed!")
    st.switch_page("pages/Results.py")
