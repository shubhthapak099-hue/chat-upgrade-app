import streamlit as st
import os
from huggingface_hub import InferenceClient

client = InferenceClient(token=os.environ.get("HF_TOKEN"))

st.set_page_config(page_title="Chat Upgrade App", page_icon="💬")
st.title("💬 Chat Upgrade App")
st.write("Type any message — get an upgraded version instantly")
st.markdown("---")

mode = st.radio("Who are you talking to?",
["❤️ Love Mode", "👨‍👩‍👧 Family Mode", "👫 Friends Mode"],
horizontal=True)

user_message = st.text_area("Type your message here:",
placeholder="Example: good morning, i miss you, how are you",
height=120)

tones = {
"❤️ Love Mode": "Rewrite this as a deeply romantic and loving text message. Give 3 short versions. Only return the 3 versions nothing else.",
"👨‍👩‍👧 Family Mode": "Rewrite this as a warm caring and respectful family message. Give 3 short versions. Only return the 3 versions nothing else.",
"👫 Friends Mode": "Rewrite this as a fun casual and witty message to a best friend. Give 3 short versions. Only return the 3 versions nothing else."
}

if st.button("✨ Upgrade My Message"):
    if user_message.strip():
        with st.spinner("AI is upgrading your message..."):
            response = client.chat.completions.create(
                model="mistralai/Mixtral-8x7B-Instruct-v0.1",
                messages=[
                    {"role": "system", "content": tones[mode]},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=300
            )
            result = response.choices[0].message.content
            st.markdown("---")
            st.subheader("✅ Your Upgraded Messages:")
            st.markdown(result)
            st.info("Copy your favourite and paste it in your chat!")
    else:
        st.warning("Please type a message first!")
