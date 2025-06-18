import streamlit as st
from deep_translator import GoogleTranslator

# 앱 제목
st.title("영어 단어 → 한국어 번역기")
st.write("영어 단어를 입력하면 한글 뜻을 알려드립니다.")

# 사용자 입력
word = st.text_input("🔤 영어 단어를 입력하세요:")

# 번역 실행
if word:
    try:
        translated = GoogleTranslator(source='en', target='ko').translate(word)
        st.success(f"📘 '{word}'의 한글 뜻: {translated}")
    except Exception as e:
        st.error(f"❌ 오류가 발생했습니다: {e}")
