import streamlit as st

st.set_page_config(page_title="Schedule Clean Up", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in first!")
    st.stop()

st.markdown("## Schedule Clean Up")

st.markdown("### Clean Up Frequency")
frequency = st.radio("Select Frequency:", ["Daily", "Weekly", "Monthly", "Custom"], index=1, horizontal=True)

schedule_time = st.text_input("Setup Schedule Time (HH:MM)", value="21:00")

st.markdown("### Choose What To Delete")
delete_options = st.radio("Select Emails to Delete:", ["Unread Emails", "Old Emails", "Spam", "All Mail"], index=0, horizontal=True)

st.markdown("---")
st.markdown(f"""
<div style='background-color:#fff5cc;padding:1rem;border-radius:10px;'>
    <strong>567 emails will be affected by this cleanup</strong><br>
    - 415 unread emails<br>
    - 27 emails older than 30 days
</div>
""", unsafe_allow_html=True)

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Upcoming Clean Up**")
    st.info(f"Next Week at {schedule_time}")
with col2:
    st.markdown("**Recent Cleanup**")
    st.success(f"Today at {schedule_time} (567 emails)")

if st.button("Back to Clean Up Settings"):
    st.switch_page("pages/CleanUpSettings.py")
