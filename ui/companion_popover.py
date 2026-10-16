import streamlit as st

# --- COMPANION POPOVER CHAT  ---
def render_companion_popover():
    """Display a chat companion to help visitors navigate the portfolio."""
    SALUDO = "¡Hola! 👋 ¿Quieres que te cuente de este proyecto?"
    ETIQUETA = "💬 Pregúntame"

    st.markdown(f"""
    <style>
    .st-key-chat_fab {{
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 999999;
        width: auto;
    }}

    /* Botón más grande y llamativo */
    .st-key-chat_fab button {{
        background: linear-gradient(135deg, #ff4b4b, #ff8e53);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.7rem 1.3rem;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        animation: pulso 2s ease-out 3;   /* solo 3 veces, no infinito */
    }}
    .st-key-chat_fab button:hover {{
        transform: scale(1.05);
    }}

    @keyframes pulso {{
        0%   {{ box-shadow: 0 0 0 0 rgba(255,75,75,0.6); }}
        70%  {{ box-shadow: 0 0 0 18px rgba(255,75,75,0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(255,75,75,0); }}
    }}

    /* Burbuja de saludo que aparece y se va sola */
    .st-key-chat_fab::before {{
        content: "{SALUDO}";
        position: absolute;
        bottom: 62px;
        right: 0;
        width: 220px;
        background: white;
        color: #222;
        padding: 10px 14px;
        border-radius: 14px 14px 2px 14px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.2);
        font-size: 0.9rem;
        opacity: 0;
        animation: burbuja 8s ease 2s forwards;  /* aparece a los 2s, dura 8s */
        pointer-events: none;
    }}

    @keyframes burbuja {{
        0%   {{ opacity: 0; transform: translateY(8px); }}
        10%  {{ opacity: 1; transform: translateY(0); }}
        85%  {{ opacity: 1; }}
        100% {{ opacity: 0; }}
    }}

    div[data-testid="stPopoverBody"] {{
        width: min(380px, 90vw);
    }}
    </style>
    """, unsafe_allow_html=True)

    if "msgs" not in st.session_state:
        st.session_state.msgs = [{
            "role": "assistant",
            "content": "¡Hola! Soy el asistente de este portafolio. Puedo explicarte de qué trata este proyecto, qué tecnologías usé y qué problema resuelve. ¿Por dónde empezamos?"
        }]

    with st.container(key="chat_fab"):
        with st.popover(ETIQUETA):
            historial = st.container(height=300)

            # Preguntas sugeridas: siempre visibles
            sugerida = None
            c1, c2 = st.columns(2)
            if c1.button("¿De qué trata?", use_container_width=True, key="sug1"):
                sugerida = "¿De qué trata este proyecto?"
            if c2.button("¿Qué tecnologías usaste?", use_container_width=True, key="sug2"):
                sugerida = "¿Qué tecnologías usaste?"

            prompt = st.chat_input("Escribe tu pregunta") or sugerida

            if prompt:
                st.session_state.msgs.append({"role": "user", "content": prompt})
                st.session_state.msgs.append({"role": "assistant", "content": "Aquí iría la respuesta sobre el proyecto."})

            with historial:
                for m in st.session_state.msgs:
                    st.chat_message(m["role"]).write(m["content"])