##  项目介绍

使用百度翻译API、百度语音翻译API、VITS、NLP等接口集成的一个虚拟对话系统。



开源仓库

- [Gitee](https://gitee.com/LiuHua_code/digital_-life-atri)
- [Github](https://github.com/LiuHua20/Digital_Life-ATRI)



##  使用说明

- 环境：Python3.12

  下载相关库：

  `pip install openai==0.28`

  `pip install pygame`

  `pip install requests`

  `pip install random`

  `pip install tkinter`

  其余有用到请自行下载

  

- 本项目依赖前置vits-simple-api(https://github.com/Artrajz/vits-simple-api)

- 相关参数说明(请自行申请)：

- 运行语音对话系统：

  `python app_sound.py`

  运行文字对话系统(简易UI界面)：

  `python app_gui.py`

-     openai_api.py里的content参数可自行设置Prompt
      
      Key说明
      # OpenAI API　Key
      openai_api_key = ''
      # Baidu ID
      baidu_speech_appid = ''
      # Baidu API Key
      baidu_speech_api_key = ''
      # Baidu Speech API Key
      baidu_speech_secret_key = ''
      # Baidu Translate ID
      baidu_translate_appid = ''
      # Baidu Translate Key
      baidu_translate_secret_key = '' 



​	感谢Artrajz大佬开源的vits-api系统