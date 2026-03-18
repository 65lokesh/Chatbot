from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv()
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available models:")
for m in genai.list_models():
    print("-", m.name)

st.set_page_config(page_title="Gemini Translator", page_icon="🌍")
st.title("🌍 Gemini Language Translator")

input_language = st.text_input("Input Language", "English")
output_language = st.text_input("Output Language", "Spanish")
input_text = st.text_area("Text to translate")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate from {input_language} to {output_language}."),
    ("user", "{text}")
])

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


chain = prompt | llm | StrOutputParser()

if st.button("Translate"):
    if input_text:
        result = chain.invoke({
            "input_language": input_language,
            "output_language": output_language,
            "text": input_text
        })
        st.success(result)
