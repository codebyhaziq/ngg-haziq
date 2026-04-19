import random
import streamlit as st

# ---------------- PAGE ----------------
st.set_page_config(page_title="Number Guesser", page_icon="🎯", layout="centered")

# ---------------- HEADER ----------------
st.markdown("""
# 🎯 Number Guesser

### 🚀 Created by **Haziq**  
Turning simple ideas into interactive games 💡

---
""")

# ---------------- STATE ----------------
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

    min_s, max_s = st.slider(
        "Select range 🎯",
        0, 1000,
        (st.session_state.min_number, st.session_state.max_number)
    )

    col1, col2 = st.columns(2)

    with col1:
        min_number = st.number_input(
            "Minimum 🔽",
            0, 1000,
            value=min_s,
            step=1
        )

    with col2:
        max_number = st.number_input(
            "Maximum 🔼",
            0, 1000,
            value=max_s,
            step=1
        )

    lives = st.number_input("Lives ❤️", 1, 20, 5, 1)

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

            st.success("🔥 Game Started!")
            st.balloons()

# ---------------- GAME ----------------
else:

    st.header("🤔 Guess the Number")

    st.info(f"Range: {st.session_state.min_number} - {st.session_state.max_number}")

    # ✅ ENTER KEY FIX (REAL SOLUTION)
    with st.form("guess_form"):

        guess_input = st.text_input("Your guess (type number and press Enter)")

        submitted = st.form_submit_button("🎯 Submit Guess")

    # ---------------- GAME LOGIC ----------------
    if submitted:

        try:
            guess = int(guess_input)
        except:
            st.error("❌ Please enter a valid number!")
            st.stop()

        if guess < st.session_state.min_number or guess > st.session_state.max_number:
            st.warning("❌ Out of range!")
            st.stop()

        st.session_state.guesses.append(guess)
        distance = abs(st.session_state.secret_number - guess)

        # WIN
        if distance == 0:
            st.success("🏆 YOU WIN! Haziq approves 😎")
            st.snow()
            st.session_state.game_started = False

        else:
            st.session_state.lives -= 1

            st.write(f"📜 Guesses: {st.session_state.guesses}")
            st.write(f"❤️ Lives: {st.session_state.lives}")

            # HINTS
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
                st.write("⬇️ Lower!")
            else:
                st.write("⬆️ Higher!")

            # GAME OVER
            if st.session_state.lives == 0:
                st.error("💀 Game Over")
                st.write(f"Number was: {st.session_state.secret_number}")
                st.snow()
                st.session_state.game_started = False

    st.caption("👑 Built by Haziq")

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
### 👑 About the Creator

**Haziq** — a rising developer turning ideas into interactive experiences.  
This Number Guesser is just the beginning.

💻 Python + Streamlit  
🚀 More projects coming soon

---

⚡ *"Simple ideas. Powerful execution."*
""")
