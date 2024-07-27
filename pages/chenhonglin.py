'''我的主页'''
import streamlit as st

page =st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])
def page1():
    with open('霞光.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.write('这是我的兴趣推荐一些好玩的steam游戏')
    st.image('陈泓霖_a.png')
    st.write('杀戮尖塔')
    st.image('陈泓霖_b.png')
    st.write('泰拉瑞亚')
    st.image('陈泓霖_c.png')
    st.write('小骨英雄杀手')    
    st.image('陈泓霖_d.png')
    st.write('全面战争模拟器')    
    st.image('陈泓霖_e.png')
    st.write('环世界')
    pass
def page2():
    pass
def page3():
    pass
def page4():
    pass

if page=='我的兴趣推荐':
    page1()
elif page=='我的图片处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
elif page=='我的留言区':
    page4()