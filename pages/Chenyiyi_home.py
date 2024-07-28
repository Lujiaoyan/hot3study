'''Chenyiyi的网站'''
from ast import Import
from PIL import Image
import streamlit as st
import qrcode
from cryptography.fernet import Fernet
from io import BytesIO
import base64  


page= st.sidebar.radio('首页',['兴趣推荐', '图片处理工具', '文字处理工具', '数据处理工具','智慧词典', '留言区'])
def page1():
    st.balloons()
    st.title("兴趣推荐")
    st.markdown('开始阅读之前，不妨先听听**我最喜欢的歌曲**吧~')
    # 打开音频文件
    audio_file = open('D:\home\我的网络根据地\Chenyiyi_music.mp3', 'rb')
    audio_bytes = audio_file.read()

    # 使用st.audio函数播放音频
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("我的爱好是**写代码**和**阅读**")
    # 使用Tabs来显示原图和修改后的图
    taba, tabb = st.tabs(["编程", "阅读"])
    with taba:
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
    with tabb:
        st.markdown('### 总述')
        st.markdown('我热爱阅读文学作品，比较喜欢小说、散文')
        st.markdown('当然也很喜欢科幻文学作品，特别推荐《三体》《流浪地球》')
        st.image("D:\home\我的网络根据地\Chenyiyi_image2.jpg")
        st.markdown('书籍是人类进步的阶梯，希望你也能阅读起来！')

from PIL import Image, ImageEnhance
import io
from PIL import Image, ImageFilter
def apply_filter(img, filter_type):
    if filter_type == '模糊':
        return img.filter(ImageFilter.BLUR)
    elif filter_type == '锐化':
        return img.filter(ImageFilter.SHARPEN)
    elif filter_type == '边缘增强':
        return img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == '高斯模糊':
        return img.filter(ImageFilter.GaussianBlur(radius=2))
    elif filter_type == '浮雕效果':
        return img.filter(ImageFilter.EMBOSS)
    else:
        return img
def page2():
    st.title("图片处理工具")
    # 图片增加滤镜功能
    st.markdown('### 图片增加滤镜')
    filter_file = st.file_uploader('上传图片进行滤镜处理', type=['png', 'jpg', 'jpeg'], key='filter_upload')
    filter_type = st.selectbox('选择滤镜类型', ['原图', '模糊', '锐化', '边缘增强', '高斯模糊', '浮雕效果'])
    
    tab_filter_original, tab_filter_modified = st.tabs(["原图", "滤镜后"])
    if filter_file:
        img_filter = Image.open(filter_file)
        with tab_filter_original:
            st.image(img_filter, caption="原始图片")
        
        if filter_type != '原图':
            filtered_img = apply_filter(img_filter, filter_type)
        else:
            filtered_img = img_filter
        
        with tab_filter_modified:
            st.image(filtered_img, caption="滤镜后的图片")
        
        # 保存处理后图片以便下载
        filtered_img_bytes = img_to_bytes(filtered_img)
        st.download_button("下载处理后的图片", filtered_img_bytes, f"{filter_type}_image.png")
    
    # 图片换色功能
    st.markdown('### 图片换色')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'], key='color_change_upload')
    
    # 滑块和恢复默认值按钮
    a = st.slider(label='请输入参数1', min_value=0, max_value=3, value=0, step=1, help="请输入参数1")
    if st.button('重置参数1', key='reset_a'):
        a = 0
    b = st.slider(label='请输入参数2', min_value=0, max_value=3, value=0, step=1, help="请输入参数2")
    if st.button('重置参数2', key='reset_b'):
        b = 0
    c = st.slider(label='请输入参数3', min_value=0, max_value=3, value=0, step=1, help="请输入参数3")
    if st.button('重置参数3', key='reset_c'):
        c = 0
    
    tab1, tab2 = st.tabs(["原图", "修改后"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        with tab1:
            st.image(img, caption="原始图片")
            original_img_bytes = img_to_bytes(img)  # 保存原始图片以便下载
            st.download_button("下载原始图片", original_img_bytes, "original_image.png")
            
        modified_img = img_change(img.copy(), a, b, c)
        with tab2:
            st.image(modified_img, caption="修改后的图片")
            modified_img_bytes = img_to_bytes(modified_img)  # 保存修改后图片以便下载
            st.download_button("下载修改后图片", modified_img_bytes, "modified_image.png")
    else:
        st.warning("请上传图片以使用工具。")
    
    # 图片灰度图转换功能
    st.markdown('### 图片灰度图转换')
    grayscale_file = st.file_uploader('上传图片进行灰度转换', type=['png', 'jpg', 'jpeg'], key='grayscale_upload')
    brightness = st.slider('调整亮度', min_value=0, max_value=100, value=50, step=1, help="调整图片的亮度")
    if st.button('重置亮度', key='reset_brightness'):
        brightness = 50
    
    tab3, tab4 = st.tabs(["原图", "灰度图"])
    if grayscale_file:
        img_gray = Image.open(grayscale_file).convert('L')
        with tab3:
            st.image(img_gray, caption="原始图片")
            original_gray_img_bytes = img_to_bytes(img_gray)  # 保存原始灰度图片以便下载
            st.download_button("下载原始灰度图", original_gray_img_bytes, "original_gray_image.png")
        
        with tab4:
            if brightness != 50:
                adjusted_img_gray = adjust_brightness(img_gray, brightness)
                st.image(adjusted_img_gray, caption="灰度图")
                adjusted_gray_img_bytes = img_to_bytes(adjusted_img_gray)  # 保存调整后灰度图以便下载
                st.download_button("下载调整后的灰度图", adjusted_gray_img_bytes, "adjusted_gray_image.png")
            else:
                st.image(img_gray, caption="灰度图")
                original_gray_img_bytes = img_to_bytes(img_gray)  # 保存原始灰度图以便下载
                st.download_button("下载灰度图", original_gray_img_bytes, "gray_image.png")
    else:
        st.warning("请上传图片进行灰度图转换。")
    
    # 图片添加水印功能
    st.markdown('### 图片添加水印')
    base_image_file = st.file_uploader('上传主图', type=['png', 'jpg', 'jpeg'], key='base_image')
    watermark_file = st.file_uploader('上传水印图', type=['png', 'jpg', 'jpeg'], key='watermark_image')
    
    opacity = st.slider('水印透明度', min_value=0, max_value=100, value=50, step=1)
    size = st.slider('水印大小', min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    position = st.selectbox('水印位置', ['左上', '右上', '左下', '右下', '中心'])
    
    if base_image_file and watermark_file:
        base_image = Image.open(base_image_file).convert("RGBA")
        watermark = Image.open(watermark_file).convert("RGBA")
        
        # 调整水印大小
        watermark = watermark.resize((int(watermark.width * size), int(watermark.height * size)))
        
        # 设置水印透明度
        alpha = watermark.split()[3]
        alpha = alpha.point(lambda p: p * (opacity / 100.0))
        watermark.putalpha(alpha)
        
        # 计算水印位置
        if position == '左上':
            position = (0, 0)
        elif position == '右上':
            position = (base_image.width - watermark.width, 0)
        elif position == '左下':
            position = (0, base_image.height - watermark.height)
        elif position == '右下':
            position = (base_image.width - watermark.width, base_image.height - watermark.height)
        else:  # 中心
            position = ((base_image.width - watermark.width) // 2, (base_image.height - watermark.height) // 2)
        
        # 添加水印
        base_image.paste(watermark, position, watermark)
        
        # 显示原图与水印添加后的图
        tab5, tab6 = st.tabs(["原图", "修改后"])
        
        with tab5:
            st.image(base_image, caption="原始主图")
            original_watermark_img_bytes = img_to_bytes(base_image)  # 保存原始主图以便下载
            st.download_button("下载原始主图", original_watermark_img_bytes, "original_base_image.png")
        
        with tab6:
            st.image(base_image, caption="添加水印后的图片")
            watermarked_img_bytes = img_to_bytes(base_image)  # 保存带水印后的图以便下载
            st.download_button("下载带水印的图片", watermarked_img_bytes, "watermarked_image.png")
    else:
        st.warning("请上传主图和水印图。")
def img_change(img, rc, bc, gc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            if len(img_array[x, y]) == 4:  # 检查像素值是否包含四个元素
                r, g, b, a = img_array[x, y]  # 分别取出RGBA值
                img_array[x, y] = (b, g, r, a)  # 重新赋值，保持 alpha 通道不变
            else:
                r, g, b = img_array[x, y]  # 对于RGB图片，正常处理
                img_array[x, y] = (b, g, r)
    return img

def adjust_brightness(image, brightness):
    enhancer = ImageEnhance.Brightness(image)
    factor = 0.1 + (brightness / 50.0)
    adjusted_image = enhancer.enhance(factor)
    return adjusted_image

def img_to_bytes(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr.getvalue()


def page3():
    st.title("智慧词典")
def page4():
    st.title("留言区")
def generate_key():  
    # 生成密钥  
    return Fernet.generate_key()  
  
def encrypt_text(text, key):  
    # 加密文本  
    cipher_suite = Fernet(key)  
    encrypted_text = cipher_suite.encrypt(text.encode('utf-8'))  
    return encrypted_text  
  
def decrypt_text(encrypted_text, key):  
    # 解密文本  
    cipher_suite = Fernet(key)  
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode('utf-8')  
    return decrypted_text  
  
def text_to_qrcode(text):  
    # 生成二维码  
    qr = qrcode.QRCode(  
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )  
    qr.add_data(text)  
    qr.make(fit=True)  
    img = qr.make_image(fill='black', back_color='white')  
    buffer = BytesIO()  
    img.save(buffer, format="PNG")  
    img_str = base64.b64encode(buffer.getvalue()).decode()  
    return f"data:image/png;base64,{img_str}"  
  
def page5():
    st.title("文字处理工具")  
  
    # 加密部分  
    st.subheader("加密工具")  
    text = st.text_area("输入文本进行加密")  
    if st.button("加密文本"):  
        key = generate_key()  # 每次运行都会生成新密钥  
        encrypted_text = encrypt_text(text, key)  
        encrypted_text_decoded = encrypted_text.decode('utf-8')  
        key_decoded = key.decode('utf-8')  
          
        # 将加密文本和密钥存储到会话状态中  
        st.session_state.encrypted_text = encrypted_text_decoded  
        st.session_state.key = key_decoded  
          
        # 显示加密文本和密钥  
        st.write("加密后的文本：", encrypted_text_decoded)  
        st.write("密钥：", key_decoded)  
          
        # 添加复制按钮  
        st.write("""  
            <button onclick="navigator.clipboard.writeText('{}')">复制加密文本</button>  
            <button onclick="navigator.clipboard.writeText('{}')">复制密钥</button>  
        """.format(encrypted_text_decoded, key_decoded), unsafe_allow_html=True)  
  
    # 解密部分  
    st.subheader("解密工具")  
    encrypted_input = st.text_area("输入要解密的文本（请确保是加密文本）")  
    key_input = st.text_input("输入用于解密的密钥")  
    if st.button("解密文本"):  
        try:  
            decrypted_text = decrypt_text(encrypted_input.encode('utf-8'), key_input.encode('utf-8'))  
            st.write("解密后的文本：", decrypted_text)  
        except Exception as e:  
            st.error(f"解密失败：{e}")  
  
    # 二维码转换部分  
    st.subheader("文本转二维码工具")  
    text_for_qrcode = st.text_area("输入要转换为二维码的文本")  
    if st.button("生成二维码"):  
        img = text_to_qrcode(text_for_qrcode)  
        # 显示二维码图片  
        st.image(img, use_column_width=True)  
import numpy as np  
import matplotlib.pyplot as plt  
  
def plot_function(func_str, x_range):  
    """  
    根据函数表达式和x的范围绘制函数图像。  
    """  
    x = np.linspace(x_range[0], x_range[1], 400)  
    y = eval(func_str)  
    plt.figure(figsize=(10, 6))  
    plt.plot(x, y)  
    plt.title('Function Plot')  
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.grid(True)  
    st.pyplot()  
  
def page6():  
    st.title("数据处理工具")  
      
    # 获取用户输入的函数表达式和x的范围  
    func_input = st.text_input("请输入函数表达式，例如 'x**2' 或 'np.sin(x)':")  
    x_min = st.number_input("请输入x的最小值：", value=-10.0)  
    x_max = st.number_input("请输入x的最大值：", value=10.0)  
      
    # 检查输入是否有效  
    if func_input and x_min < x_max:  
        try:  
            # 尝试绘制函数图像  
            plot_function(func_input, (x_min, x_max))  
        except Exception as e:  
            st.error(f"无法绘制函数图像：{e}")  
    else:  
        st.write("请输入有效的函数表达式和x的范围。")  

if page == "兴趣推荐":
    page1()
elif page == "图片处理工具":
    page2()
elif page == "智慧词典":
    page3()
elif page == "留言区":
    page4()
elif page == "文字处理工具":
    page5()
elif page == "数据处理工具":
    page6()
