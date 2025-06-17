import streamlit as st
import requests

st.title("영어 단어 사전")

st.write("영어 단어를 입력하면 뜻과 예문을 보여줍니다.")

def get_word_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data

word = st.text_input("검색할 영어 단어를 입력하세요:")

if word:
    data = get_word_data(word)
    if data is None:
        st.error("단어를 찾을 수 없습니다. 다시 시도하세요.")
    else:
        # 뜻 보여주기
        st.header(f"'{word}'의 뜻과 예문")
        for meaning in data[0].get('meanings', []):
            part_of_speech = meaning.get('partOfSpeech', '')
            st.subheader(part_of_speech)
            for definition in meaning.get('definitions', []):
                definition_text = definition.get('definition', '')
                example = definition.get('example', '')
                st.write(f"- 뜻: {definition_text}")
                if example:
                    st.write(f"  - 예문: {example}")

