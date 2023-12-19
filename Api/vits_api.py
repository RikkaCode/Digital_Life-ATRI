import requests
import os
import re

# 基础配置
base_url = "http://127.0.0.1:23456" # vits-api地址
absolute_path = os.path.dirname(__file__)

audio_folder = os.path.join(absolute_path, "../Audio/VITS/")
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# 保存音频文件的函数
def save_audio_file(response):
    fname = re.findall("filename=(.+)", response.headers["Content-Disposition"])[0]
    path = os.path.join(audio_folder, fname)
    with open(path, "wb") as f:
        f.write(response.content)
    print(f"Saved audio to {path}")
    return path

# Bert-VITS2语音合成
def voice_bert_vits2(text):
    url = f"{base_url}/voice/bert-vits2"
    data = {
        "text": text,
        "id": 0,
        "format": "wav"
    }
    try:
        res = requests.post(url, json=data)
        res.raise_for_status()
        return save_audio_file(res)
    except Exception as e:
        print(f"Bert-vits2 error: {e}")
        return None

# VITS语音合成 - 使用GET请求
def voice_vits(text):
    url = f"{base_url}/voice/vits"
    params = {
        "text": text,
        "id": 0,
        "format": "wav"
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        return save_audio_file(res)
    except Exception as e:
        print(f"VITS error: {e}")
        return None

# 语音合成主函数，优先使用Bert-VITS2
def voice_synthesis(text):
    bert_result = voice_bert_vits2(text)
    if bert_result is not None:
        return bert_result
    else:
        print("Fallback to VITS")
        return voice_vits(text)

# 用户输入文本并获取语音
if __name__ == '__main__':
    text = input("请输入要合成的文本: ")
    voice_synthesis(text)
