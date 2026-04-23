import streamlit as st

st.set_page_config(page_title="LegalCheck KZ", page_icon="⚖️")
st.title("⚖️ LegalCheck")
st.write("Анализ договоров по законодательству РК")

text = st.text_area("Вставьте текст договора:", height=300)

if st.button("Проверить"):
    if text:
        # Поиск рисков
        if "одностороннем порядке" in text.lower():
            st.error("🔴 **Критично:** Нарушение ст. 401 ГК РК (Одностороннее изменение условий).")
        if "штраф" in text.lower():
            st.warning("🟡 **Внимание:** Проверьте соразмерность неустойки по ст. 353 ГК РК.")
        if not any(word in text.lower() for word in ["одностороннем", "штраф"]):
            st.success("Явных рисков по ключевым словам не найдено.")
    else:
        st.info("Введите текст для анализа.")
