import numpy as np
from typing import List, Dict

class GloveModel:
    def __init__(self, glove_file: str):
        self.embeddings = {}
        self.load_glove_model(glove_file)

    def load_glove_model(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                values = line.split()
                word = values[0]
                vector = np.array(values[1:], dtype='float32')
                self.embeddings[word] = vector

    def find_similar_words(self, word: str, top_n: int = 10) -> List[str]:
        if word not in self.embeddings:
            return []

        word_vector = self.embeddings[word]
        similarities = {
            other_word: np.dot(word_vector, vector) / (np.linalg.norm(word_vector) * np.linalg.norm(vector))
            for other_word, vector in self.embeddings.items()
        }
        similar_words = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
        return [word for word, _ in similar_words[1:top_n+1]]  # Exclude the word itself

glove_model = GloveModel("glove.6B.100d.txt")

def get_similar_words(word: str) -> Dict:
    similar_words = glove_model.find_similar_words(word)
    return {"word": word, "similar_words": similar_words}
