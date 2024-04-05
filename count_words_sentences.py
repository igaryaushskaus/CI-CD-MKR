import re

def count_words_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        sentences = re.split(r'[.!?]+', text)

        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(words), len(sentences)

if __name__ == "__main__":
    file_path = "example.txt"
    word_count, sentence_count = count_words_sentences(file_path)
    print(f"Кількість слів: {word_count}")
    print(f"Кількість речень: {sentence_count}")