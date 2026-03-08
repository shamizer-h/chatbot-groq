import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .main-title {
        text-align: center;
        color: #00d4ff;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #888888;
        font-size: 1em;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">AI Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by Groq API</p>', unsafe_allow_html=True)
st.divider()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful and friendly AI assistant. Answer clearly and concisely."},
                    *st.session_state.messages
                ],
                max_tokens=1024,
                temperature=0.7
            )
            bot_reply = response.choices[0].message.content
            st.markdown(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

with st.sidebar:
    st.markdown("### About")
    st.markdown("This chatbot is built using the Groq API with the LLaMA 3 model and deployed via Streamlit.")
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.markdown("**Project:** AI Chatbot")
    st.markdown("**Model:** LLaMA 3.3 70B")
    st.markdown("**Framework:** Streamlit")
