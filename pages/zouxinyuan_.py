'''myspace'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('myspace', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    st.write(':green[这 是 我的兴趣推荐]')
    mymp3 = '望辰-杨紫'
    st.audio(mymp3, format='audio/mp3', start_time=0)
def page_2():
    '''我的图片处理工具'''
    st.write(':green[这 是 我的图片处理工具]')
    uploaded_file = st.file_uploader('shangchuantupian',type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
def page_3():
    '''我的智慧词典'''
    st.write(':lightgreen[这 是 我的智慧词典]')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
    else:
        st.write('NOTHING')
def img_change(img, rc, gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(height):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]             
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    tab1, tab2,  tab3, tab4  = st.tabs(["own", "change1", "change2", "change3"])
    with tab1:
        st.image(img)
    with tab2:
        st.image(img_change(img, 0 ,2, 1))
    with tab3:
        st.image(img_change(img, 1 ,2, 0))       
    with tab4:
        st.image(img_change(img, 1 ,0, 2))
            
    return img
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2() 
elif page == '我的智慧词典':
    page_3() 
else:
    page_4() 
