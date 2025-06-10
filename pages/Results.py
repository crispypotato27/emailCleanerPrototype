import streamlit as st

st.set_page_config(page_title="Scan Results", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first!")
    st.stop()

email = st.session_state.get("email", "Unknown User")
junk_count = st.session_state.get("junk_count", 0)
spam_count = st.session_state.get("spam_count", 0)
duplicates_count = st.session_state.get("duplicates_count", 0)

st.markdown(f"<h2 style='text-align: center;'><strong>{email.upper()}</strong></h2>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center;'>Scanned: {junk_count + spam_count + duplicates_count} emails</h4>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

box_style = """
    background-color: #fff5cc;
    padding: 1.5rem;
    border-radius: 10px;
    text-align: center;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
"""

with col1:
    st.markdown(f"<div style='{box_style}'>", unsafe_allow_html=True)
    st.markdown("**Junk found:**")
    st.markdown(f"<h2>{junk_count}</h2>", unsafe_allow_html=True)
    if st.button("🧹 Clean Junk"):
        st.session_state.junk_count = 0
        st.success("Junk cleaned successfully!")
    if st.button("🔍 Review Junk"):
        st.switch_page("pages/ReviewJunk.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div style='{box_style}'>", unsafe_allow_html=True)
    st.markdown("**Spam found:**")
    st.markdown(f"<h2>{spam_count}</h2>", unsafe_allow_html=True)
    if st.button("🧹 Clean Spam"):
        st.session_state.spam_count = 0
        st.success("Spam cleaned successfully!")
    if st.button("🔍 Review Spam"):
        st.switch_page("pages/ReviewSpam.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div style='{box_style}'>", unsafe_allow_html=True)
    st.markdown("**Duplicates found:**")
    st.markdown(f"<h2>{duplicates_count}</h2>", unsafe_allow_html=True)
    if st.button("🧹 Clean Duplicates"):
        st.session_state.duplicates_count = 0
        st.success("Duplicates cleaned successfully!")
    if st.button("🔍 Review Duplicates"):
        st.switch_page("pages/ReviewDuplicates.py")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; margin-top: 2rem;'>", unsafe_allow_html=True)
if st.button("🚀 Clean All"):
    st.session_state.junk_count = 0
    st.session_state.spam_count = 0
    st.session_state.duplicates_count = 0
    st.success("All categories cleaned!")
st.markdown("</div>", unsafe_allow_html=True)
