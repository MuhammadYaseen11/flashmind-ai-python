import streamlit as st
from flashcard_gen import generate_flashcards

st.set_page_config(page_title="FlashMind", layout="centered")
st.title("🧠 FlashMind - AI Flashcard Generator")

text_input = st.text_area("Paste your notes or text here:", height=250)

if st.button("Generate Flashcards"):
    if text_input.strip() == "":
        st.warning("Please paste some content.")
    else:
        with st.spinner("Generating flashcards..."):
            output = generate_flashcards(text_input)
            st.success("Flashcards generated!")
            st.text_area("Your Flashcards:", output, height=300)

