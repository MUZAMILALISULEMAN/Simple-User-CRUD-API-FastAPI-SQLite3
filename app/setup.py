# from pydantic import BaseModel,validator

# class User(BaseModel):
#     id: int
#     name: str
#     is_active: bool

# user = User(id = 2,name="3",is_active=False)
# print(user.json())
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Are You Happy?", layout="centered")
st.title("😄 Are You Happy?")

# Input
user_input = st.text_area("Write something about how you're feeling:")

if user_input:
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity  # -1 to 1

    # Show result
    if polarity > 0.1:
        st.success("You're feeling HAPPY! 😊")
    elif polarity < -0.1:
        st.error("You're NOT feeling happy 😔")
    else:
        st.warning("Hmm, it's NEUTRAL 🤔")
