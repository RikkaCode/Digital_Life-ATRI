import requests
import hashlib
import random

class BaiduTranslator:
    def __init__(self, appid, secret_key):
        self.appid = appid
        self.secret_key = secret_key

    def translate(self, text, from_lang, to_lang):
        salt = random.randint(32768, 65536)
        sign_str = self.appid + text + str(salt) + self.secret_key
        sign = hashlib.md5(sign_str.encode()).hexdigest()

        url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
        params = {
            "q": text,
            "from": from_lang,
            "to": to_lang,
            "appid": self.appid,
            "salt": str(salt),
            "sign": sign
        }

        response = requests.get(url, params=params)
        result = response.json()

        if "error_code" in result:
            return f"Error: {result['error_code']} - {result.get('error_msg', 'No error message')}"
        else:
            trans_result = result.get('trans_result')
            if trans_result:
                return trans_result[0].get('dst')
            else:
                return True

if __name__ == "__main__":
    appid = '' # 百度翻译ID
    secret_key = '' # 百度翻译Key
    translator = BaiduTranslator(appid, secret_key)

    while True:
        text = input("Q: ")
        if text.lower() == 'quit':
            break

        translated_text = translator.translate(text, 'zh', 'jp')
        print("A: ", translated_text)
