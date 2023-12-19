import sounddevice as sd
import numpy as np
import requests
import base64
import json
import io

class BaiduSpeechRecognizer:
    def __init__(self, app_id, api_key, secret_key):
        self.app_id = app_id
        self.api_key = api_key
        self.secret_key = secret_key

    def get_access_token(self):
        url = 'https://openapi.baidu.com/oauth/2.0/token'
        params = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.secret_key
        }
        response = requests.get(url, params=params)
        return response.json()['access_token']

    def recognize_speech(self, audio_data, token, sample_rate=16000):
        # 将音频数据转换为base64并发送给百度语音识别API
        speech_base64 = base64.b64encode(audio_data).decode('utf-8')
        speech_length = len(audio_data)

        headers = {'Content-Type': 'application/json'}
        data = {
            'format': 'pcm',
            'rate': sample_rate,
            'channel': 1,
            'cuid': self.app_id,
            'token': token,
            'dev_pid': 1537,
            'speech': speech_base64,
            'len': speech_length
        }

        response = requests.post('http://vop.baidu.com/server_api', headers=headers, data=json.dumps(data))
        return response.json()

    @staticmethod
    def record_audio(duration=5, sample_rate=16000):
        # 录制音频
        print("开始录音，时长{}秒...".format(duration))
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        print("录音结束")
        return np.int16(audio).flatten()

def main():
    app_id = '' # 百度语音翻译ID
    api_key = ''    # 百度语音翻译ApiKey
    secret_key = '' # 百度语音翻译Key

    # 创建百度语音识别器实例
    recognizer = BaiduSpeechRecognizer(app_id, api_key, secret_key)

    # 录制音频
    audio_data = BaiduSpeechRecognizer.record_audio(duration=5)
    
    # 将NumPy数组转换为字节流
    audio_bytes = io.BytesIO()
    np.save(audio_bytes, audio_data, allow_pickle=False)
    audio_bytes = audio_bytes.getvalue()

    # 获取token并进行语音识别
    token = recognizer.get_access_token()
    response = recognizer.recognize_speech(audio_bytes, token)

    if response.get('result'):
        print("语音翻译：", response['result'][0])
    else:
        print("识别失败，未得到结果")

if __name__ == '__main__':
    main()
