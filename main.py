import streamlit as st
import requests
from gtts import gTTS
import os

# DeepL API 키 설정
DEEPL_API_KEY = 'YOUR_DEEPL_API_KEY'  # 여기에 본인의 DeepL API 키를 입력하세요.

# DeepL API를 사용하여 번역하는 함수
def translate_text(text, target_lang='KO'):
    url = f'https://api-free.deepl.com/v2/translate?auth_key={DEEPL_API_KEY}&text={text}&target_lang={target_lang}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['translations'][0]['text']
    else:
        return None

# 예문 제공 함수 (예시로 간단한 예문을 반환)
def get_example_sentence(word):
    examples = {
        'apple': 'I ate an apple for breakfast.',
        'book': 'She is reading a book.',
        'computer': 'He works on a computer all day.'
    }
    return examples.get(word.lower(), '예문을 찾을 수 없습니다.')

# 앱 제목
st.title("영어 단어 번역기 및 발음 출력기")
st.write("영어 단어를 입력하면 한글 뜻과 예문을 알려주며, 발음도 들을 수 있습니다.")

# 사용자 입력
word = st.text_input("영어 단어를 입력하세요:")

if word:
    # 번역
    translation = translate_text(word)
    if translation:
        st.write(f"**한글 뜻**: {translation}")
    else:
        st.write("번역에 실패했습니다.")

    # 예문
    example = get_example_sentence(word)
    st.write(f"**예문**: {example}")

    # 발음 출력
    if st.button("발음 듣기"):
        tts = gTTS(text=word, lang='en')
        tts.save("word.mp3")
        with open("word.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
        os.remove("word.mp3")
