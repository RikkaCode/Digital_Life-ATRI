import os
from docx import Document

# 定义将要合并的TXT文件所在的文件夹
txt_folder = ''  # 将其替换为包含TXT文件的文件夹路径

output_docx = 'ATRI-my dear moments.docx'

doc = Document()

# 遍历TXT文件夹中的所有文件
for filename in os.listdir(txt_folder):
    if filename.endswith('.txt'):
        txt_path = os.path.join(txt_folder, filename)
        with open(txt_path, 'r', encoding='utf-8') as txt_file:
            txt_content = txt_file.read()
            # 将TXT内容添加到Word文档中
            doc.add_paragraph(txt_content)

# 保存合并后的Word文档
doc.save(output_docx)

print(f'合并完成，生成的Word文档保存在 {output_docx}')
