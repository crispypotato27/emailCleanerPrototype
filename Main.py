import streamlit as st
import imaplib

st.set_page_config(
    page_title="Login page",
    #layout="wide",
    initial_sidebar_state="collapsed"
)

from util import load_css, background
load_css("assets/style.css")


# Background image
background("assets/bg.png")


with st.container():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="left-column">', unsafe_allow_html=True)
        st.markdown("# Welcome back!")
        st.markdown("### Email Cleaner")
        st.markdown('*“An intelligent email assistant that automatically organizes, filters, and declutters your inbox — so you never miss what matters.”*')
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="right-column">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">Login</div>', unsafe_allow_html=True)
        
        email = st.text_input("Email", label_visibility="collapsed", placeholder="Email", key="email_input")
        password = st.text_input("Password", label_visibility="collapsed", placeholder="Password (16 Characters)", key="password", type="password")
        login = st.button("Log in", key="login")

        if login:
            if email and password:
                #try:
                    # Connect to the IMAP server
                    mail = imaplib.IMAP4_SSL('imap.gmail.com')
                    #mail.login(email, password)

                    st.success("Login successful!")
                    st.session_state.logged_in = True
                    st.session_state.email = email
                    st.session_state.app_password = password
                    st.success(f"Logged in as {email}!")
                    st.switch_page("pages/Dashboard.py")

                #except imaplib.IMAP4.error as e:
                    st.error(f"Login failed: {e}")
            else:
                st.warning("Please enter both email and password.")

        st.markdown("""
            <div class="tutorial">
                Here’s a <a href="https://www.youtube.com/watch?v=N_J3HCATA1c">tutorial</a> how to set up an account!
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
