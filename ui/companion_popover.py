import streamlit as st

# --- COMPANION POPOVER CHAT  ---
def render_companion_popover():
    """Display a chat companion to help visitors navigate the portfolio."""
    st.markdown("""
    <style>
    .st-key-chat_fab {
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 999999;
        width: auto;
    }
    div[data-testid="stPopoverBody"] {
        width: min(380px, 90vw);
    }
    </style>
    """, unsafe_allow_html=True)

    if "msgs" not in st.session_state:
        st.session_state.msgs = []

    with st.container(key="chat_fab"):
        with st.popover("💬"):
            historial = st.container(height=350)   # zona con scroll
            prompt = st.chat_input("Escribe tu mensaje")

            if prompt:
                st.session_state.msgs.append({"role": "user", "content": prompt})
                st.session_state.msgs.append({"role": "assistant", "content": "¡Hola! ¿En qué te ayudo?"})

            with historial:
                for m in st.session_state.msgs:
                    st.chat_message(m["role"]).write(m["content"])