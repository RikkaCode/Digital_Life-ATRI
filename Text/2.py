with io.open('/mnt/data/ATRI_and_夏生_dialogues_utf8.txt', 'r', encoding='utf-8') as file:
    dialogues = file.readlines()


formatted_data = []
current_dialogue = {"prompt": "", "completion": ""}

for line in dialogues:
    if "夏生：" in line:
        # If the current dialogue has a prompt and a completion, add it to the list and start a new one
        if current_dialogue["prompt"] and current_dialogue["completion"]:
            formatted_data.append(current_dialogue)
            current_dialogue = {"prompt": "", "completion": ""}
        current_dialogue["prompt"] += line
    elif "ATRI：" in line:
        current_dialogue["completion"] += line


if current_dialogue["prompt"] and current_dialogue["completion"]:
    formatted_data.append(current_dialogue)


fine_tuning_file_path = '/mnt/data/ATRI_and_夏生_dialogues_fine_tuning.jsonl'
with open(fine_tuning_file_path, 'w', encoding='utf-8') as file:
    for dialogue in formatted_data:
        file.write(json.dumps(dialogue) + "\n")

fine_tuning_file_path


with open(fine_tuning_file_path, 'r', encoding='utf-8') as file:
    jsonl_lines = file.readlines()


corrected_jsonl_lines = [json.loads(line) for line in jsonl_lines]
corrected_jsonl_lines = [json.dumps(line, ensure_ascii=False) for line in corrected_jsonl_lines]


corrected_file_path = '/mnt/data/ATRI_and_夏生_dialogues_fine_tuning_corrected.jsonl'
with open(corrected_file_path, 'w', encoding='utf-8') as file:
    for line in corrected_jsonl_lines:
        file.write(line + "\n")

corrected_file_path




