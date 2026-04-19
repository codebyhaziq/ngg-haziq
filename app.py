import random
import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Number Guesser", page_icon="🎯")

# ---------------- HEADER ----------------
st.markdown("""
# 🎯 Number Guesser

### 🚀 Created by Haziq  
Turning simple ideas into interactive games 💡

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

# ---------------- SETUP SCREEN ----------------
if not st.session_state.game_started:

    st.header("🎮 Game Setup")

    # Slider (faster + more game-like)
    min_number, max_number = st.slider(
        "Select your range 🎯",
        min_value=0,
        max_value=1000,
        value=(1, 100)
    )

    # Lives
    lives = st.number_input(
        "Lives ❤️",
        min_value=1,
        max_value=50,
        value=5,
        step=1
    )

    if st.button("Start Game 🚀"):

        if min_number >= max_number:
            st.warning("❌ Minimum must be smaller than maximum!")
        else:
            st.session_state.min_number = min_number
            st.session_state.max_number = max_number
            st.session_state.secret_number = random.randint(min_number, max_number)
            st.session_state.lives = lives
            st.session_state.guesses = []
            st.session_state.game_started = True

            st.success("🔥 Game Started! Haziq’s challenge begins...")

# ---------------- GAME SCREEN ----------------
else:

    st.header("🤔 Make a Guess")

    guess = st.number_input(
        "Your guess",
        min_value=st.session_state.min_number,
        max_value=st.session_state.max_number,
        step=1
    )

    if st.button("Submit Guess 🎯"):

        st.session_state.guesses.append(guess)
        distance = abs(st.session_state.secret_number - guess)

        # Correct guess
        if distance == 0:
            st.success("🎉 You cracked the code! Haziq is impressed 😎")
            st.session_state.game_started = False

        else:
            st.session_state.lives -= 1

            st.write(f"📜 Guesses: {st.session_state.guesses}")
            st.write(f"❤️ Lives left: {st.session_state.lives}")

            if st.session_state.lives > 0:

                if distance <= 2:
                    st.error("🔥 Boiling hot")
                elif distance <= 5:
                    st.warning("🌡️ Hot")
                elif distance <= 10:
                    st.info("🙂 Warm")
                elif distance <= 20:
                    st.info("❄️ Cold")
                else:
                    st.info("🥶 Freezing")

                if guess > st.session_state.secret_number:
                    st.write("⬇️ Try lower!")
                else:
                    st.write("⬆️ Try higher!")

            else:
                st.error("💀 Game Over! Even legends miss sometimes 🔁")
                st.write(f"🔐 The number was: {st.session_state.secret_number}")
                st.session_state.game_started = False

    st.caption("👀 Built with logic, luck, and creativity by Haziq")

# ---------------- RESET ----------------
st.divider()

if st.button("Play Again 🔁"):
    st.session_state.game_started = False
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []

# ---------------- FOOTER ----------------
st.markdown("""
---

### 👑 About the Creator

**Haziq** — a rising developer building interactive games from scratch.  
From simple Python scripts to full web apps, this is just the beginning.

💻 Built with Python & Streamlit  
🚀 More projects coming soon

---

⚡ *"Think simple. Build smart. Execute clean."*
""")
