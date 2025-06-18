import streamlit as st
from googletrans import Translator

# 페이지 제목
st.title("영어 단어 번역기")
st.write("영어 단어를 입력하면 한글 뜻을 알려드립니다.")

# 번역기 초기화
translator = Translator()

# 사용자 입력
word = st.text_input("영어 단어를 입력하세요:")

# 번역 결과 표시
if word:
    try:
        result = translator.translate(word, src='en', dest='ko')
        st.success(f"'{word}'의 한글 뜻: {result.text}")
    except Exception as e:
        st.error(f"번역에 실패했습니다: {e}")
