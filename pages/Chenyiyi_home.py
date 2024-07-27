'''Chenyiyi的网站'''
import streamlit as st

page= st.sidebar.radio('首页',['兴趣推荐', '图片处理工具', '智慧词典', '留言区'])
def page1():
    st.title("兴趣推荐")
    st.markdown('开始阅读之前，不妨先听听**我最喜欢的歌曲**吧~')
    # 打开音频文件
    audio_file = open('D:\home\我的网络根据地\Chenyiyi_music.mp3', 'rb')
    audio_bytes = audio_file.read()

    # 使用st.audio函数播放音频
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("我的爱好是**写代码**和**阅读**")
    sex = st.selectbox(
        label='点击选择框切换选项查看兴趣介绍',
        options=('阅读','编程'),
        index = 1,
        format_func = str,
        help='点击对应的选项查看'
        )
    if sex =='编程':
        st.markdown('### 总述')
        st.markdown('我~~熟练~~掌握***python***、***html***和***css***，目前还在学习C++')
        st.markdown('[****跳转至github主页****](https://github.com/cyyChenYiyi/ "github主页")')
        st.markdown('### 项目')
        st.markdown("#### ClassGuardian")
        st.markdown('[****跳转至项目github主页****](https://github.com/cyyChenYiyi/ClassGuardian "ClassGuardian github主页")')
        st.markdown('基于python+html，实现了以下功能：')
        st.markdown('1、一键给教室电脑上锁，防止学生课间偷玩电脑')
        st.markdown('2、教师只需拿出手机扫码即可关闭锁机')
        st.markdown('3、显示距离上课时间等小功能')
        st.image("D:\home\我的网络根据地\Chenyiyi_image1.png")
        st.markdown("#### blog")
        st.markdown('[****跳转至项目github主页****](https://github.com/cyyChenYiyi/cyychenyiyi.github.io "项目github主页")')
        st.markdown('基于开源项目Gmeek，实现了blog')
        st.markdown('> 剩余部分老旧项目暂不展示')
    elif sex =='阅读':
        st.markdown('### 总述')
        st.markdown('我热爱阅读文学作品，比较喜欢小说、散文')
        st.markdown('当然也很喜欢科幻文学作品，特别推荐《三体》《流浪地球》')
        st.image("D:\home\我的网络根据地\Chenyiyi_image2.jpg")
        st.markdown('书籍是人类进步的阶梯，希望你也能阅读起来！')
    else:
        st.write('请您先选择')
def page2():
    st.title("图片处理工具")
def page3():
    st.title("智慧词典")
def page4():
    st.title("留言区")
if page == "兴趣推荐":
    page1()
elif page == "图片处理工具":
    page2()
elif page == "智慧词典":
    page3()
elif page == "留言区":
    page4()