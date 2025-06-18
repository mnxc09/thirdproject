import streamlit as st

# 영어-한글 사전 (필요한 만큼 추가 가능)
english_korean_dict = {
    "apple": "사과",
    "book": "책",
    "computer": "컴퓨터",
    "dog": "개",
    "elephant": "코끼리",
    "friend": "친구",
    "house": "집",
    "love": "사랑",
    "music": "음악",
    "school": "학교"
}

# 앱 제목
st.title("영어 단어 → 한글 뜻 변환기")

# 사용자 입력
word = st.text_input("영어 단어를 입력하세요:").strip().lower()

# 변환 결과 출력
if word:
    meaning = english_korean_dict.get(word)
    if meaning:
        st.success(f"'{word}'의 뜻은 '{meaning}'입니다.")
    else:
        st.warning(f"'{word}'는 사전에 등록되지 않은 단어입니다.")
