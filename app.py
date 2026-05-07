import streamlit as st
import os
import requests

api_key = os.environ.get("GROQ_API_KEY")

st.set_page_config(page_title="Chat Upgrade App", page_icon="💬")
st.title("Chat Upgrade App")
st.write("Type any message and get an upgraded version instantly")
st.markdown("---")

mode = st.radio("Who are you talking to?",
["Love Mode", "Family Mode", "Friends Mode"],
horizontal=True)

user_message = st.text_area("Type your message here:",
placeholder="Example: good morning, i miss you, how are you",
height=120)

tones = {
"Love Mode": "romantic and loving",
"Family Mode": "warm and caring",
"Friends Mode": "fun and casual"
}

if st.button("Upgrade My Message"):
    if user_message.strip():
        with st.spinner("Upgrading your message..."):
            headers = {
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json"
            }
            data = {
                "model": "llama3-8b-8192",
                "messages": [
                    {
                        "role": "user",
                        "content": "Rewrite this message in a " + tones[mode] + " tone. Give 3 short versions numbered 1, 2, 3. Message: " + user_message
                    }
                ],
                "max_tokens": 300
            }
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )
            result = response.json()
            if "choices" in result:
                answer = result["choices"][0]["message"]["content"]
                st.markdown("---")
                st.subheader("Your Upgraded Messages:")
                st.write(answer)
                st.info("Copy your favourite and paste it in your chat!")
            else:
                st.error("Groq said: " + str(result))
    else:
        st.warning("Please type a message first!")
