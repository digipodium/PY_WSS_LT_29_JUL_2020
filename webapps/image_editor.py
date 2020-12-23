import streamlit as st
from PIL import Image

editing_options = ['resize','transpose','convert']
allowed_files = ['jpg','png','bmp','jpeg']

# UI
st.sidebar.title('Image Editor')
file = st.file_uploader("Upload an image here", type=allowed_files)
choice = st.sidebar.selectbox('select an editing option',options=editing_options)
img_box = st.empty()
# logic
if file:
    img_box.image(file.read(),use_column_width=True) # take file, read the bytes
    img = Image.open(file)
    size = img.size
    mode = img.mode
    format = img.format

    st.sidebar.header('image info')
    st.sidebar.error(f'Resolution : {size}')
    st.sidebar.warning(f'Mode : {mode}')
    st.sidebar.success(f'format : {format}')

if file:
    if choice =='resize':
        img = Image.open(file)
        st.sidebar.subheader('enter image size')
        x = st.sidebar.number_input('Width',64,2000,value=img.width)
        y = st.sidebar.number_input('Height',64,2000,value=img.height)
        if st.sidebar.button("resize image"):
            rsz_img = img.resize((x,y))
            img_box.image(rsz_img,caption='resized image')
    elif choice == 'transpose':
        pass
    elif choice == 'convert':
        pass
    else:
        st.error("no option provided")
