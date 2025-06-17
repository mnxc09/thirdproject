import streamlit as st
from googletrans import Translator
import nltk
from nltk.corpus import wordnet as wn

# nltk 다운로드 (최초 실행 시)
nltk.download('wordnet')

# 번역기 초기화
translator = Translator()

def get_korean_meaning(word):
    try:
        translated = translator.translate(word, src='en', dest='ko')
        return translated.text
    except Exception as e:
        return "번역 실패"

def get_example_sentence(word):
    synsets = wn.synsets(word)
    if synsets:
        examples = synsets[0].examples()
        if examples:
            return examples[0]
        else:
            return "예문이 없습니다."
    else:
        return "단어를 찾을 수 없습니다."

# Streamlit 앱 UI 구성
st.title("📘 영어 단어 학습 앱")
st.write("영어 단어를 입력하면 한글 뜻과 예문을 보여줍니다.")

# 사용자 입력
word = st.text_input("🔤 영어 단어를 입력하세요:")

if word:
    st.markdown("## 결과")
    meaning = get_korean_meaning(word)
    example = get_example_sentence(word)

    st.write(f"**한글 뜻:** {meaning}")
    st.write(f"**예문:** {example}")
