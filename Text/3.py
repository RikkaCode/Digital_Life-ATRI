chat_formatted_jsonl_data = []

for line in lines:
    entry = json.loads(line)
    prompt = entry['prompt'].replace("夏生：", "").strip()
    completion = entry['completion'].replace("ATRI：", "").strip()

    # Creating a new JSON entry in the chat-completion format
    new_chat_entry = {
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": completion}
        ]
    }
    chat_formatted_jsonl_data.append(json.dumps(new_chat_entry, ensure_ascii=False))

# Joining all the reformatted entries into a single string
chat_formatted_jsonl_data_str = "\n".join(chat_formatted_jsonl_data)

# Save the reformatted data to a new file
chat_formatted_jsonl_file_path = '/mnt/data/ATRI_chat_formatted.jsonl'
with open(chat_formatted_jsonl_file_path, 'w', encoding='utf-8') as file:
    file.write(chat_formatted_jsonl_data_str)

chat_formatted_jsonl_file_path

