import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

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
"❤️ Love Mode": "Rewrite this as a deeply romantic and loving text message. Give 3 short versions.",
"👨‍👩‍👧 Family Mode": "Rewrite this as a warm, caring and respectful family message. Give 3 short versions.",
"👫 Friends Mode": "Rewrite this as a fun, casual and witty message to a best friend. Give 3 short versions."
}

if st.button("✨ Upgrade My Message"):
    if user_message.strip():
        with st.spinner("AI is upgrading your message..."):
            response = model.generate_content(
                f"{tones[mode]}\n\nOriginal message: {user_message}"
            )
            st.markdown("---")
            st.subheader("✅ Your Upgraded Messages:")
            st.markdown(response.text)
            st.info("Copy your favourite and paste it in your chat!")
    else:
        st.warning("Please type a message first!")
