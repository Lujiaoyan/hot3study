'''mty的网站'''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write('这是我的兴趣推荐')
    st.image('miaotianyi_缴剑.jpg')
    st.image('miaotianyi_散双杰.jpg')
    st.image('miaotianyi_双杰.jpg')
    st.image('miaotianyi_听学.jpg')
    st.image('miaotianyi_忘羡.jpg')
    st.image('miaotianyi_魏婴.png')
    st.video('miaotianyi_广告.mp4')
with open('miaotianyi_何以歌.mp3', 'rb') as f:
    mymp3 = f.read()
st.audio(mymp3, format='audio/mp3', start_time=0)

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

elif page == '我的图片处理工具':
    page_2()

elif page == '我的智慧词典':
    page_3()

elif page == '我的留言区':
    page_4()