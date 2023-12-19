from Api.openai_api import OpenAIChatbot
from Api.baidu_api_text import BaiduTranslator
from Api.vits_api import voice_vits
import pygame

class IntegratedChatbot:
    def __init__(self, openai_api_key, baidu_appid, baidu_secret_key):
        self.chatbot = OpenAIChatbot(openai_api_key)
        self.translator = BaiduTranslator(baidu_appid, baidu_secret_key)

    def play_audio(self, file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 等待音频播放完成
            pygame.time.Clock().tick(10)

    def chat_and_translate(self):
        while True:
            user_input = input("Q: ")
            if user_input.lower() == 'quit':
                break

            # 从 OpenAI 获取回答
            openai_response = self.chatbot.get_chat_response(user_input)
            print("ATRI: ", openai_response)

            # 将 OpenAI 的回答翻译成日语
            translated_response = self.translator.translate(openai_response, 'zh', 'jp')
            # print("翻译结果: ", translated_response)

            # 使用VITS生成语音并播放
            audio_file_path = voice_vits(translated_response)  # 返回音频文件的路径
            if audio_file_path:
                self.play_audio(audio_file_path)

if __name__ == "__main__":
    openai_api_key = ''
    baidu_appid = ''
    baidu_secret_key = ''

    chatbot = IntegratedChatbot(openai_api_key, baidu_appid, baidu_secret_key)
    chatbot.chat_and_translate()
