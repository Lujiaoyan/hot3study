'''wangning的网站'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write('这是我的兴趣爱好')
    st.write('[太空杀]')
    st.image("TKX.jpg")
    st.image("TKX2.jpg")
    st.image("TKX3.jpg")

def page_2():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,1,0,2))

def page_3():    
    '''我的智慧词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具' :
    page_2()
elif page == '我的图片处理工具' :
    page_3()
elif page == '我的智慧词典' :
    page_4()

