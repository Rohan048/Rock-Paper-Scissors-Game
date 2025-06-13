import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")

st.title("🎮 Rock 🪨 Paper 📄 Scissors ✂️ Game")
st.write("Play against the computer!")

choices = ['Rock', 'Paper', 'Scissors']
player_choice = st.selectbox("Choose your option:", choices)

if 'player_score' not in st.session_state:
    st.session_state.player_score=0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score=0
if 'draw' not in st.session_state:
    st.session_state.draw=0

if st.button("Play"):
    computer_choice=random.choice(choices)

    st.write(f"You choose: {player_choice}")
    st.write(f"Computer choose: {computer_choice}")

    if player_choice==computer_choice:
        result="Game is Draw!🤝"
        st.session_state.draw +=1
    elif(player_choice=="Rock" and computer_choice=="Scissors"):
        result="You Win!🎉"
        st.session_state.player_score +=1
    elif(player_choice=="Scissors" and computer_choice=="Paper"):
        result="You Win!🎉"
        st.session_state.player_score +=1
    elif(player_choice=="Paper" and computer_choice=="Rock"):
        result="You Win!🎉"
        st.session_state.player_score +=1
    else:
        result="Computer Win!🎉"
        st.session_state.computer_score +=1

    st.success(result)

    st.markdown("----")
    st.subheader("📊 Scoreboard")
    st.write(f"you: {st.session_state.player_score}")
    st.write(f"Computer: {st.session_state.computer_score}")
    st.write(f"Draw: {st.session_state.draw}")

if st.button("🔄Reset score"):
    st.session_state.player_score =0
    st.session_state.computer_score=0
    st.session_state.draw=0
    st.info("Scores have been reset")


