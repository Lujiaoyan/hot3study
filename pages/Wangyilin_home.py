'''我的主页'''

import streamlit as st
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    '''我的兴趣推荐'''
    st.write(':red[这是我的兴趣推荐]')
    st.write("这是一首好听的音乐")
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time = 0)
    st.write("这是我喜欢的一张二战地图")
    st.image("b9b1e177eb8ea9123f644f3ac65d026da9387817.jpg")
    st.write("我喜欢编程打篮球跑步和游泳，变成让我充盈生活，运动锻炼身体")
    st.write(":blue[我最喜欢环太1这部电影，我喜欢看八十天环游地球这本书非常有意思，我最难忘的一次旅行是去四川玩，非常酷，火锅很好吃。]")
    st.image("476a71397eb85426c6167097dba97c0c.jpeg")
def page2():
    '''我的图片处理工具'''
    pass
def page3():
    '''我的智慧词典'''
    pass
def page4():
    '''我的留言区'''
    pass

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()