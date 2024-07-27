'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的主页',['我喜欢的游戏', '24点计算器', '我的智慧词典', '我的留言区'])

def page_1():
    st.write('我喜欢的游戏:')
    st.write(':red[Heroes of might and magic 3]')
    st.audio('GRASS.MP3')
    st.image('MuMap.bmp')   
def page_2():
    st.write(':red[啥都没有捏···]')
def page_3():
    st.write(':red[啥都没有捏···]')
def page_4():
    st.write(':red[啥都没有捏···]')
    
if page == '我喜欢的游戏':
    page_1()
elif page == '24点计算器':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
else :
    pass
