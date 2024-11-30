import streamlit as st

# Đặt hình ảnh nền
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20230408/pngtree-rainbow-curves-abstract-colorful-background-image_2164067.jpg');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)

# Căn lề dòng chữ ở trung tâm
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <h1 style="color: white;">Chị Hà Thối</h1>
    </div>
    """, unsafe_allow_html=True)
