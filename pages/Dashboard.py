import streamlit as st
import base64

st.set_page_config(page_title="Dashboard", layout="wide", initial_sidebar_state="collapsed")

from util import load_css, background
load_css("assets/style2.css")
background("assets/bg2.png")

#if "logged_in" not in st.session_state or not st.session_state.logged_in:
    #st.error("You must log in first!")
    #st.stop()

email = st.session_state.get("email", "Unknown User")

st.markdown(f"<h2><strong>{email.upper()}</strong></h2>", unsafe_allow_html=True)
st.markdown(f"<hr>",unsafe_allow_html=True)

with st.container():
  col1, col2, col3 = st.columns(3, vertical_alignment="center")
  
  with col1:
    st.markdown('<div class="header">', unsafe_allow_html=True)
    left, right = st.columns([1.5, 1])

    with left:
        st.markdown("## Clean Up Settings")

    with right:
        st.image("assets/clean.png", width=80)

    CleanPage = st.button("Clean", key="clean")

    if CleanPage:
       st.switch_page("pages/CleanUpSettings.py")

    st.markdown('</div>', unsafe_allow_html=True)
    
  with col2:
    st.markdown('<div class="header">', unsafe_allow_html=True)
    left, right = st.columns([2, 1], vertical_alignment="center")

    with left:
        st.markdown("## Scan Email")

    with right:
        st.image("assets/mail.png", width=80)

    ScanPage = st.button("Scan", key="scan")

    if ScanPage:
       st.switch_page("pages/ScanEmails.py")

    st.markdown('</div>', unsafe_allow_html=True)

  with col3:
    st.markdown('<div class="header">', unsafe_allow_html=True)
    left, right = st.columns([3, 1], vertical_alignment="center")

    with left:
        st.markdown("### Delete Subscription")

    with right:
        st.image("assets/trash.png", width=50)

    DeletePage = st.button("Delete", key="delete")

    if DeletePage:
       st.switch_page("pages/DeleteSubscriptions.py")

    st.markdown('</div>', unsafe_allow_html=True)

  #with col1:
  #  action_block("Clean Up Settings", "https://img.icons8.com/ios-filled/50/000000/broom.png", "Open Clean Up Settings", "pages/CleanUpSettings.py")
  #with col2:
  #  action_block("Scan Email", "https://img.icons8.com/ios-filled/50/000000/email.png", "Start Scan", "pages/ScanEmails.py")
  #with col3:  
  #  action_block("Delete Subscriptions", "https://img.icons8.com/ios-filled/50/000000/trash.png", "Delete Subscriptions", "pages/DeleteSubscriptions.py")


if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.email = ""
    st.success("You have been logged out.")
    st.switch_page("main.py")
