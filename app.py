import streamlit as st
import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="Chat Upgrade App", page_icon="💬")
st.title("💬 Chat Upgrade App")
st.write("Type any message — get an upgraded version instantly")
st.markdown("---")

mode = st.radio("Who are you talking to?",
["Love Mode", "Family Mode", "Friends Mode"],
horizontal=True)

user_message = st.text_area("Type your message here:",
placeholder="Example: good morning, i miss you, how are you",
height=120)

tones = {
"Love Mode": "romantic and loving",
"Family Mode": "warm caring and family appropriate",
"Friends Mode": "fun casual and friendly"
}

if st.button("Upgrade My Message"):
    if user_message.strip():
        with st.spinner("Upgrading your message..."):
            tone = tones[mode]
            prompt = "Rewrite this message in a " + tone + " tone. Give 3 short versions numbered 1, 2, 3. Message: " + user_message
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            result = response.choices[0].message.content
            st.markdown("---")
            st.subheader("Your Upgraded Messages:")
            st.write(result)
            st.info("Copy your favourite and paste it in your chat!")
    else:
        st.warning("Please type a message first!")
