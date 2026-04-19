import random
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Guesser",
    page_icon="🎯",
    layout="centered"
)

# ---------------- THEME ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}
h1, h2, h3 {
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
# 🎯 Number Guesser

### 🚀 Created by **Haziq**
*From simple logic to a full interactive experience 💡*

---
""")

# ---------------- SESSION STATE ----------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []
    st.session_state.min_number = 1
    st.session_state.max_number = 100

# ---------------- SETUP ----------------
if not st.session_state.game_started:

    st.header("🎮 Game Setup")

    min_number, max_number = st.slider(
        "Select your range 🎯",
        0, 1000, (1, 100)
    )

    st.write("Fine-tune your range if needed 👇")

    col1, col2 = st.columns(2)

    with col1:
        min_number = st.number_input("Minimum 🔽", 0, 1000, min_number, 1)

    with col2:
        max_number = st.number_input("Maximum 🔼", 0, 1000, max_number, 1)

    lives = st.slider("Lives ❤️", 1, 20, 5)

    if st.button("🚀 Start Game"):

        if min_number >= max_number:
            st.error("Minimum must be smaller than maximum!")
        else:
            st.session_state.min_number = min_number
            st.session_state.max_number = max_number
            st.session_state.secret_number = random.randint(min_number, max_number)
            st.session_state.lives = lives
            st.session_state.guesses = []
            st.session_state.game_started = True

            st.success("🔥 Game Started! Let’s goooo!")
            st.balloons()

# ---------------- GAME ----------------
else:

    st.header("🤔 Make Your Guess")

    # Lives progress bar (WOW factor)
    max_lives = st.slider("Difficulty View (read-only)", 1, 20, st.session_state.lives)
    st.progress(st.session_state.lives / max_lives if max_lives > 0 else 0)

    guess = st.number_input(
        "Enter your guess",
        min_value=st.session_state.min_number,
        max_value=st.session_state.max_number,
        step=1
    )

    if st.button("🎯 Submit Guess"):

        st.session_state.guesses.append(guess)
        distance = abs(st.session_state.secret_number - guess)

        # WIN
        if distance == 0:
            st.success("🏆 YOU WIN! Haziq approves this genius move 😎")
            st.snow()
            st.session_state.game_started = False

        else:
            st.session_state.lives -= 1

            st.write(f"📜 Guesses: {st.session_state.guesses}")
            st.write(f"❤️ Lives left: {st.session_state.lives}")

            # HINT SYSTEM (WOW UPGRADED)
            if distance <= 2:
                st.error("🔥 ABSOLUTELY HOT!")
                st.markdown("### 🌡️ You're basically touching it!")
            elif distance <= 5:
                st.warning("🌡️ Very Hot!")
            elif distance <= 10:
                st.info("🙂 Warm")
            elif distance <= 20:
                st.info("❄️ Cold")
            else:
                st.info("🥶 Freezing")

            # Direction hint
            if guess > st.session_state.secret_number:
                st.write("⬇️ Go LOWER!")
            else:
                st.write("⬆️ Go HIGHER!")

            # GAME OVER
            if st.session_state.lives == 0:
                st.error("💀 GAME OVER")
                st.write(f"🔐 The number was: {st.session_state.secret_number}")
                st.snow()
                st.session_state.game_started = False

    st.caption("👑 Built with logic, luck & creativity by Haziq")

# ---------------- RESET ----------------
st.divider()

if st.button("🔁 Play Again"):
    st.session_state.game_started = False
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []

# ---------------- FOOTER ----------------
st.markdown("""
---
### 👑 About Haziq

A young developer turning ideas into interactive experiences.  
This Number Guesser is just the beginning.

💻 Python + Streamlit  
🚀 More impressive projects coming soon

---

⚡ *"Simple ideas. Powerful execution."*
""")
