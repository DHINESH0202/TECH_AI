import streamlit as st

st.set_page_config(
    page_title="Tech AI",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS
st.markdown("""
<style>
@keyframes slide-in {
  0% {opacity: 0; transform: translateY(-30px);}
  100% {opacity: 1; transform: translateY(0);}
}

.animated-title {
  font-size: 3.5rem;
  font-weight: 800;
  text-align: center;
  color: #38bdf8;
  margin-top: 50px;
  animation: slide-in 1s ease-out;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background-color: #0f172a;
    color: #ffffff;
}
.main {
    padding: 3rem;
}
h1, h2, h3 {
    text-align: center;
}
.title {
    font-size: 4rem;
    font-weight: bold;
    background: -webkit-linear-gradient(#00d4ff, #090979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-top: 50px;
}
.description {
    text-align: center;
    font-size: 1.5rem;
    color: #cbd5e1;
    margin-bottom: 40px;
}
.feature-card {
    background-color: #1e293b;
    padding: 1.5rem;
    border-radius: 1rem;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    transition: transform 0.2s ease-in-out;
}
.feature-card:hover {
    transform: scale(1.02);
}
</style>

<div class='animated-title'>
  Welcome to Tech AI 🚀
</div>
""", unsafe_allow_html=True)

# Description
st.markdown("""
    <div class='description'>
        Your All-in-One AI Assistant for <strong>Text Generation</strong> and <strong>Text to Speech</strong> tasks. 🤖
    </div>
""", unsafe_allow_html=True)

# Features
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class='feature-card'>
            <h2>Text Generation 🌍</h2>
            <p>Generate content, ideas, summaries, and creative writing using cutting-edge AI.</p>
            <a href="/Text_Generation" target="_self">Go to Text Generation →</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='feature-card'>
            <h2>Text to Speech 🎧</h2>
            <p>Convert your text into clear and natural speech using powerful voice synthesis.</p>
            <a href="/Text_to_Speech" target="_self">Go to Text to Speech →</a>
        </div>
    """, unsafe_allow_html=True)

# Footer note
st.markdown("""
    <br><br>
    <p style='text-align: center; font-size: 0.9rem; color: #64748b;'>
        Built with ❤️ by Dhinesh using Streamlit & Cohere API
    </p>
""", unsafe_allow_html=True)
