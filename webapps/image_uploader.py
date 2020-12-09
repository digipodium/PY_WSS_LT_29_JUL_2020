import streamlit as st
from PIL import Image, ImageFilter

allowed_files = ['jpg','png','bmp','jpeg']
st.sidebar.title('Image Editor')
file = st.file_uploader("Upload an image here", type=allowed_files)
if file:
    st.image(file.read(),use_column_width=True) # take file, read the bytes
    img = Image.open(file)
    size = img.size
    mode = img.mode
    format = img.format

    st.sidebar.header('image info')
    st.sidebar.error(f'Resolution : {size}')
    st.sidebar.warning(f'Mode : {mode}')
    st.sidebar.success(f'format : {format}')
