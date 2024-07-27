"'wanglinglan 的网站'"
import  streamlit as st

page = st.sidebar.radio("我的首页",['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    "'我的兴趣推荐'"
    st.write(":blue[这是我的兴趣推荐]")
    st.write("以下分为三个板块")
    st.write("一、兴趣分享")
    st.image("鹦鹉.jpg")
    st.image("斑猫.jpg")
    st.image("非遗.jpg")
    
    st.write("二、课外奖状")
    st.image("奖状.jpg")
    st.image("奖状2.jpg")
    
    st.write("三、本人作文")
    st.image("作文1.jpg")
    st.image("作文2.jpg")
    st.image("作文3.jpg")
    st.image("作文4.jpg")
    st.image("作文5.jpg")
    st.image("作文6.jpg")
    st.image("作文7.jpg")
    st.image("作文8.jpg")
    st.write(":red[未完待续！！！]")
    
def page_2():
    "'我的图片处理工具'"
    pass
def page_3():
    "'我的智慧词典'"
    pass
def page_4():
    "'我的留言区'"
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()


