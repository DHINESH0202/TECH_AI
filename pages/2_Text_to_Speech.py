import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Text to Speech", page_icon="🔊", layout="centered")

# ---------- CSS Styling ----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 3em;
        color: #ffd369;
        text-shadow: 0 0 15px #ffd369;
        margin-bottom: 1rem;
    }
    .stTextArea textarea {
        border-radius: 12px;
        font-size: 1.1em;
    }
    .stButton > button {
        background-color: #ffd369;
        color: black;
        font-weight: bold;
        font-size: 1.1em;
        border-radius: 10px;
        padding: 10px 24px;
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #ffc107;
        color: white;
    }
    .result-audio {
        background-color: #2d2d44;
        padding: 20px;
        border-radius: 12px;
        font-size: 1em;
        color: #ffffff;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.3);
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.title("🎤 Text to Speech Converter")

text_input = st.text_area("📝 Enter text to convert:", height=150)

if st.button("🔊 Convert"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Creating your audio..."):
            tts = gTTS(text_input)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)
                st.success("✅ Audio Generated Successfully!")
                st.audio(tmp_file.name, format="audio/mp3")
                with open(tmp_file.name, "rb") as file:
                    st.download_button(
                        label="⬇️ Download Audio",
                        data=file,
                        file_name="output_speech.mp3",
                        mime="audio/mp3"
                    )
