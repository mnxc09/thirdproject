import streamlit as st
from gtts import gTTS
import os
import time

# 간단한 단어사전 (필요시 확장 가능)
dictionary = {
    "apple": {
        "meaning": "사과",
        "example": "I ate an apple this morning."
    },
    "book": {
        "meaning": "책",
        "example": "This book is very interesting."
    },
    "computer": {
        "meaning": "컴퓨터",
        "example": "She uses a computer for work."
    }
}

st.title("영어 단어 번역기")
st.write("영어 단어를 입력하면 한글 뜻과 예문을 보여주고, 발음을 들려줍니다.")

word = st.text_input("🔤 영어 단어 입력:")

if word:
    lower_word = word.lower()
    if lower_word in dictionary:
        meaning = dictionary[lower_word]["meaning"]
        example = dictionary[lower_word]["example"]

        st.success(f"📘 뜻: {meaning}")
        st.info(f"✏️ 예문: {example}")

        if st.button("🔊 발음 듣기"):
            tts = gTTS(text=lower_word, lang='en')
            filename
