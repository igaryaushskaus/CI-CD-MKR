import re

def count_words_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        sentences = re.split(r'[.!?]+', text)

        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(words), len(sentences)

