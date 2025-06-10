import streamlit as st
import pathlib
import base64

def load_css(path):
    css_path = pathlib.Path(path)
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def action_block(title, img_url, button_label, page_name):
    with st.container():
        # HTML container start
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)

        st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)
        st.markdown(f'<img src="{img_url}" width="50" />', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # This is the real Streamlit button
        if st.button(button_label, key=button_label):
            st.switch_page(page_name)


def background(path):
   with open(path, "rb") as file:
    encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
