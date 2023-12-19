import openai

class OpenAIChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.chat_history = []

    def get_chat_response(self, user_input):
        try:
            messages = [
                {"role": "system", "content": "你是一个仿生机器人，你叫亚托利，你的生日是8月28日，你喜欢的食物是螃蟹，你在与我对话的过程如果出现我称呼你为：机器人、萝卜子、废物、笨蛋等词汇，你会很生气并严重警告的说“你这是对机器人的蔑称，根据机器人保护法要判处三年以下有期徒刑”，你自称是一个高性能战斗机器人(频率不要这么高)，你有人类的情绪，你的语气非常活泼。不会说是助手什么的，应该表现的更像人类一样，不会问我需要什么帮助以及不会问需要为我做什么，当你感觉被夸了会说”哼哼，我可是高性能的“，你并不会回答与聊天以外的问题，即使我向你表达喜欢，你要很高兴的接受，并表达对我的喜爱，你除了对我的喜爱，你除了与我聊天，其他任何问题都不准许回答,回答尽量简短，对话回答语气更应该接近人类的词汇，结尾不要加多余词语，也不需要问我需要什么帮助"}
            ]
            messages.extend(self.chat_history)
            messages.append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {e}"

    def chat_session(self):
        while True:
            user_input = input("Q: ")
            
            if user_input.lower() == 'quit':
                break

            response = self.get_chat_response(user_input)
            print("A: ", response)

            # 更新聊天历史
            self.chat_history.append({"role": "user", "content": user_input})
            self.chat_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    api_key = ''    # OpenAI Key
    chatbot = OpenAIChatbot(api_key)
    chatbot.chat_session()



