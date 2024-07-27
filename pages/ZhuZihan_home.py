'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '我的兴趣推荐'
    st.write(":red[这是我的兴趣推荐]")
    st.write(":red[一.音乐篇]")
    st.write("乐者，悦耳之声也。佳乐，余音绕梁，三日不绝也。好（hào）乐者闻乐，沉于其中。少人不沉沦也。")
    with open('zhuzihan霞光.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    with open('zhuzihan海棠不言_编程猫的梦想.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    
    st.write(":red[二.图片篇]")
    st.write("景者，美丽事物也。美景，悦人心。人见之，流连忘返也。")
    st.image("zhuzihan天象奇景.jpg")
    st.image("zhuzihan微信图片_20240726195221.jpg")
    st.image("zhuzihan微信图片_20240726195239.jpg")
    st.write(":red[复制下方链接进入免费图片网站]")
    st.write("https://www.pexels.com/zh-cn/")
    
    st.write(":red[三.游戏篇]")
    st.write("游戏者，闲时娱乐也。")
    st.write("https://kbhgames.com/")
    st.write("点击进入游戏界面")

    st.write(":red[四.我的旅游篇]")
    st.write("读万卷书，行万里路。")
    st.image("zhuzihan微信图片_20240726222954.jpg")
    st.image("zhuzihan微信图片_20240726223002.jpg")
    st.image("zhuzihan微信图片_20240726223512.jpg")
    st.image("zhuzihan微信图片_20240726223520.jpg")
    st.image("zhuzihan微信图片_20240726223525.jpg")
    st.image("zhuzihan微信图片_20240726223530.jpg")
    st.image("zhuzihan微信图片_20240726223535.jpg")
    st.image("zhuzihan微信图片_20240726223540.jpg")
    st.image("zhuzihan微信图片_20240726223549.jpg")
    st.image("zhuzihan微信图片_20240726223635.jpg")
    st.image("zhuzihan微信图片_20240726224541.jpg")
    st.image("zhuzihan微信图片_20240726223555.jpg")
    st.image("zhuzihan微信图片_20240726223605.jpg")
    st.write(".........(此处省略100张图片。)")

    st.write(":red[五.我的荣誉]")
    st.video("zhuzihan_WeChat_20240726225901.mp4")


def page_2():
    "我的图片处理工具"
    pass

def page_3():
    "我的智慧词典"
    pass

def page_4():
    '''我的留言区'''
    pass

if page=="我的兴趣推荐":
    page_1()
elif page =='我的图片处理工具':
    page_2()
elif page =='我的智慧词典':
    page_3()
elif page =='我的留言区':
    page_4()

