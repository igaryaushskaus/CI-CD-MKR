import pytest
from count_words_sentences import count_words_sentences

@pytest.mark.parametrize("file_content, expected_words, expected_sentences", [
    ("This is a test sentence.", 5, 1),
    ("This is another test sentence. And this is the second one.", 11, 2),
])
def test_count_words_sentences(file_content, expected_words, expected_sentences):
    with open('example.txt', 'w', encoding='utf-8') as file:
        file.write(file_content)

    words, sentences = count_words_sentences('example.txt')
    assert words == expected_words
    assert sentences == expected_sentences