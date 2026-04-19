import random
import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Number Guesser", page_icon="🎯")

st.title("🎯 Number Guesser")

# ---------------- SESSION STATE ----------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []
    st.session_state.min_number = 1
    st.session_state.max_number = 100

# ---------------- GAME SETUP ----------------
if not st.session_state.game_started:

    st.header("Game Setup")

    min_number = st.number_input("Smallest number 🔽", value=1)
    max_number = st.number_input("Largest number 🔼", value=100)
    lives = st.number_input("Lives ❤️", value=5)

    if st.button("Start Game 🎮"):

        if min_number >= max_number:
            st.warning("Max number must be greater than min number!")
        else:
            st.session_state.min_number = min_number
            st.session_state.max_number = max_number
            st.session_state.secret_number = random.randint(min_number, max_number)
            st.session_state.lives = lives
            st.session_state.guesses = []
            st.session_state.game_started = True

# ---------------- GAME PLAY ----------------
else:
    st.header("Make a Guess 🤔")

    guess = st.number_input("Your guess", step=1)

    if st.button("Submit Guess"):

        if guess < st.session_state.min_number or guess > st.session_state.max_number:
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

                if st.session_state.lives > 0:

                    # Hints
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
                    st.write(f"The number was {st.session_state.secret_number}")
                    st.session_state.game_started = False

# ---------------- PLAY AGAIN ----------------
st.divider()

if st.button("Play Again 🔁"):
    st.session_state.game_started = False
    st.session_state.secret_number = None
    st.session_state.lives = 0
    st.session_state.guesses = []
