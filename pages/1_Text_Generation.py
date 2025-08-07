import streamlit as st
import cohere

st.set_page_config(page_title="AI Text Generator", page_icon="📝", layout="centered")

# ---------- CSS Styling ----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #1f1c2c, #928dab);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 3em;
        color: #00ffd5;
        text-shadow: 0 0 20px #00ffd5;
        margin-bottom: 1rem;
    }
    .stTextArea textarea {
        border-radius: 12px;
        font-size: 1.1em;
    }
    .stButton > button {
        background-color: #00ffd5;
        color: black;
        font-weight: bold;
        font-size: 1.1em;
        border-radius: 10px;
        padding: 10px 24px;
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #00b39f;
        color: white;
    }
    .result-box {
        background-color: #2d2d44;
        padding: 20px;
        border-radius: 12px;
        font-size: 1.15em;
        color: #ffffff;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.3);
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.title("📝 AI Text Generator")

prompt = st.text_area("💬 Enter your prompt:", height=150)

if st.button("🚀 Generate"):
    if prompt.strip() == "":
        st.warning("⚠️ Please enter a valid prompt.")
    else:
        with st.spinner("Thinking like an AI..."):
            co = cohere.Client("oi9gABZJIn2YL5aCDHAiiqVOIObCvvYUR1IKJLI0")
            response = co.generate(prompt=prompt, max_tokens=100)
            result = response.generations[0].text.strip()

            st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)

            st.download_button("⬇️ Download", data=result, file_name="generated.txt", mime="text/plain")
