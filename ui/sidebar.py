import streamlit as st

def render_sidebar():
    
    st.sidebar.markdown("### 📄 Resume")

    with open("assets/CV_MARCIAL_BERNAL_DEVELOPER.pdf", "rb") as f:
        st.sidebar.download_button(
            label="⬇️ Download CV",
            data=f,
            file_name="CV_MARCIAL_BERNAL_DEVELOPER.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.sidebar.markdown("### 📧 Send me an email:")
    st.sidebar.write("marcialb9328@gmail.com")