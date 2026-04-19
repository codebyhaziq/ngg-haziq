import random
import streamlit as st
import pyfiglet

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Number Guesser", page_icon="🎯")

# ASCII Banner
banner = pyfiglet.figlet_format("NUMBER GUESSER")
st.text(banner)

# ---------------- SESSION STATE ----------------
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []
    st.session_state.game_started = False

# ---------------- GAME SETUP ----------------
st.header("Game Setup")

min_number = st.number_input("Smallest number 🔽", value=1)
max_number = st.number_input("Largest number 🔼", value=100)
lives = st.number_input("Lives ❤️", value=5)

if st.button("Start Game 🎮"):
    st.session_state.secret_number = random.randint(min_number, max_number)
    st.session_state.lives = lives
    st.session_state.guesses = []
    st.session_state.game_started = True

# ---------------- GAME LOOP ----------------
if st.session_state.game_started:

    st.subheader("Make a Guess 🤔")

    guess = st.number_input("Your guess", step=1, key="guess_input")

    if st.button("Submit Guess"):

        # Check range
        if guess < min_number or guess > max_number:
            st.warning("Guess must be within your range!")
        else:
            st.session_state.guesses.append(guess)

            distance = abs(st.session_state.secret_number - guess)

            # Correct guess
            if distance == 0:
                st.success("🎉 Correct! You win! 🏆")
                st.session_state.game_started = False

            else:
                st.session_state.lives -= 1

                st.write(f"📜 Previous guesses: {st.session_state.guesses}")
                st.write(f"❤️ Remaining lives: {st.session_state.lives}")

                # Hints
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

                    # Direction hint
                    if guess > st.session_state.secret_number:
                        st.write("⬇️ Try lower!")
                    else:
                        st.write("⬆️ Try higher!")

                # Game over
                if st.session_state.lives == 0:
                    st.error("💀 Game Over!")
                    st.write(f"The correct number was: {st.session_state.secret_number}")
                    st.session_state.game_started = False

# ---------------- RESET BUTTON ----------------
if st.button("Play Again 🔁"):
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []
    st.session_state.game_started = False
