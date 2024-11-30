import streamlit as st

# Đặt hình ảnh nền
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://your-image-url.jpg');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)

# Căn lề dòng chữ ở trung tâm
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <h1 style="color: white;">Dòng chữ của bạn</h1>
    </div>
    """, unsafe_allow_html=True)
