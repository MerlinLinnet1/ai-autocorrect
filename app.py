import streamlit as st
from autocorrect import correct_text

st.title("AI Autocorrect Tool")

st.write("Enter a sentence and I'll try to correct the spelling!")

text = st.text_area("Your sentence:")

if st.button("Correct Spelling"):
    if text.strip():
        result = correct_text(text)

        st.write("Original:", text)
        st.write("Corrected:", result)
    else:
        st.warning("Please enter a sentence first.")
