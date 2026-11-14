
import streamlit as st
from game_engine import GameEngine
from game_master import get_game_master_response

st.set_page_config(
    page_title="The Lost Library",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 The Lost Library")
st.subheader("Version 2 – AI Escape Room")

st.write(
    "Explore the mysterious library, investigate objects, "
    "collect items, solve clues and unlock the exit!"
)

# Initialize game
if "engine" not in st.session_state:
    st.session_state.engine = GameEngine()

if "messages" not in st.session_state:
    st.session_state.messages = []

engine = st.session_state.engine

# Restart game
if st.button("🔄 Restart Game"):
    engine.restart_game()
    st.session_state.messages = []
    st.rerun()

# Calculate puzzle progress
completed = sum(
    clue in engine.clues_found
    for clue in [
        "bookshelf_clue",
        "painting_clue",
        "drawer_clue"
    ]
)

st.write(f"**Clues discovered: {completed} / 3**")
st.progress(completed / 3)

# Show player status
with st.sidebar:
    st.header("🎒 Player Status")

    st.write("**Inventory:**")

    if engine.inventory:
        for item in engine.inventory:
            st.write(f"• {item}")
    else:
        st.write("Your inventory is empty.")

    st.divider()

    st.write(
        f"**Drawer:** {'Open' if engine.drawer_open else 'Locked'}"
    )

    st.write(
        f"**Exit door:** {'Unlocked' if engine.door_unlocked else 'Locked'}"
    )

# Welcome message
if not st.session_state.messages:
    try:
        welcome = get_game_master_response(
            engine.get_room_description(),
            "Welcome the player to the Lost Library. "
            "Explain that they should investigate the room "
            "and find a way to escape."
        )
    except Exception:
        welcome = (
            "Welcome, traveler! You are trapped in the Lost Library. "
            "Investigate the objects, collect useful items and "
            "solve the clues to escape."
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": welcome}
    )

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Player input
user_input = st.chat_input(
    "Try: examine desk, examine bookshelf, or open drawer..."
)

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Python validates every player action
    result = engine.process_action(user_input)

    # Update context after Python processes the action
    context = (
        f"Clues discovered: {completed} out of 3. "
        f"Inventory: {', '.join(engine.inventory)}. "
        f"Drawer open: {engine.drawer_open}. "
        f"Door unlocked: {engine.door_unlocked}. "
        f"Game over: {engine.game_over}."
    )

    # Display Python's exact response for blocked actions
    blocked_phrases = [
        "locked",
        "incorrect",
        "not allowed",
        "refuses",
        "need to find",
        "must open",
        "not discovered",
        "already escaped"
    ]

    is_blocked = any(
        phrase in result.lower()
        for phrase in blocked_phrases
    )

    if is_blocked:
        response = result

    else:
        # Gemini provides storytelling only.
        # Python remains responsible for game decisions.
        try:
            narration = get_game_master_response(context, result)

            response = (
                f"**Game result:** {result}\n\n"
                f"{narration}"
            )

        except Exception:
            response = result

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

