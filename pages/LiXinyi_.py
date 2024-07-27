'''我的主页 '''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write(':orange["这是我的兴趣推荐"]')
    st.image("排球少年（海报）.jpg")
    with open("fly high.mp3", 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='mp3', start_time=0)
    st.write(':agate red["致我所爱的他们"]')
    st.image("排球少年.jpg")
    st.image('排球少年.jpg')

def page_2():
    '''我的图片处理工具'''
    pass

def page_3():
    '''我的智慧词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '':
    page_2()
elif page == '':
    page_3()
elif page == '':
    page_4()