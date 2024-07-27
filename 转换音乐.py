import media_tool     # 导入工具库
from pydub import AudioSegment     # 导入AudioSegment类
from pydub.playback import play     # 导入播放模块

# 添加可交互信息
source = input("请输入要转换的音频文件名：")
result = input("请输入转换后的音频文件：")

# 读取用户输入的音频文件
sound = AudioSegment.from_file(source, format=source.split(".")[-1])

#play(sound)    # 播放音乐

# 导出格式转换后的音频文件
sound.export(result, format=result.split(".")[-1])
