import streamlit as st

st.set_page_config(page_title="Delete Subscriptions", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first!")
    st.stop()

email = st.session_state.get("email", "Unknown User")

st.markdown(f"<h2><strong>{email.upper()}</strong> - Manage Subscriptions</h2>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("## Your Subscriptions")

subscriptions = [
    {"service": "Netflix", "email": "user_netflix@example.com"},
    {"service": "Spotify", "email": "user_spotify@example.com"},
    {"service": "Hulu", "email": "user_hulu@example.com"},
    {"service": "Disney+", "email": "user_disney@example.com"}
]

for sub in subscriptions:
    col1, col2, col3 = st.columns([2, 4, 2])
    with col1:
        st.markdown(f"**{sub['service']}**")
    with col2:
        st.markdown(sub["email"])
    with col3:
        if st.button(f"Delete {sub['service']}"):
            st.success(f"Deleted {sub['service']} subscription for {sub['email']}")

st.markdown("---")
if st.button("Back to Dashboard"):
    st.switch_page("Dashboard.py")
