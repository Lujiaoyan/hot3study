'''myspace'''
import streamlit as st
page = st.sidebar.radio('myspace', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    st.write(':lightgreen[This 是 我的兴趣推荐]')
def page_2():
    '''我的图片处理工具'''
    st.write(':lightgreen[This 是 我的图片处理工具]')
def page_3():
    '''我的智慧词典'''
    st.write(':lightgreen[This 是 我的智慧词典]')

def page_4():
    '''我的留言区'''
    st.write(':lightgreen[This 是 我的留言区]')
    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2() 
elif page == '我的智慧词典':
    page_3() 
else:
    page_4() 