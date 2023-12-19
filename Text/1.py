new_doc = Document()

for paragraph in doc.paragraphs:
    if "ATRI：" in paragraph.text or "夏生：" in paragraph.text:
        new_doc.add_paragraph(paragraph.text)


new_doc_path = '/mnt/data/ATRI_and_夏生_dialogues.docx'
new_doc.save(new_doc_path)

new_doc_path


