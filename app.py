import streamlit as st

from support_agent import respond


st.set_page_config(page_title="Relay AI Support")
st.title("Relay AI")
st.caption("A customer-support assistant demo. It cannot access live accounts.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! What can I help you with today? Please don’t share passwords, "
            "verification codes, or full payment-card details.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Describe your issue"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    reply = respond(prompt)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply.message,
            "category": reply.category,
            "needs_human": reply.needs_human,
        }
    )
    st.rerun()

with st.sidebar:
    st.subheader("Try a message")
    st.caption(
        "“My order hasn’t arrived” · “I was charged twice” · "
        "“I need a person”"
    )
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()
