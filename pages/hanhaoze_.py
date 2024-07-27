'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write('''这是我的兴趣推荐[如下↓↓↓]''')
    st.video('https://show.ybccode.com/common_static/galaxy/solar.mp4')
    st.write('''太阳系（英文：Solar system）是一个受太阳引力约束在一起的天体系统，
             包括太阳、行星及其卫星、矮行星、小行星、彗星和星际物质，太阳系位于银河系
             中心大约2.4～2.7光年的位置。''')
    st.write('''在直接围绕太阳运动的天体中，最大的八颗被称为行星，
             太阳系包括8大行星：水星、金星、地球、火星、木星、土星、天王星、海王星（由离太阳从近到远的顺序），
             八大行星逆时针围绕太阳公转。其余的天体要比行星小很多，比如矮行星、太阳系小行星和彗星。''')
    
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
