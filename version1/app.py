
import streamlit as st
from game_master import get_game_master_response

st.set_page_config(
    page_title="The Lost Library",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 The Lost Library")
st.subheader("An AI-Powered Escape Room")

st.write(
    "Welcome to the mysterious digital library. "
    "Solve three puzzles to unlock the exit!"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    with st.spinner("The AI Librarian is preparing your puzzle..."):
        welcome = get_game_master_response(
            [],
            "Start the escape room game."
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": welcome}
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Enter your answer or ask for a hint...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("The AI Librarian is thinking..."):
            response = get_game_master_response(
                st.session_state.messages[:-1],
                user_input
            )
            st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

if st.button("🔄 Restart Game"):
    st.session_state.messages = []
    st.rerun()
