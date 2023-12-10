import nltk


class AnalysePositiveNegativeScore:

    def __init__(self, stop_words):
        print('create a dictionary for positive and negative words keeping in mind of the stop words')

        self.positive_words = set()
        with open('MasterDictionary/positive-words.txt', 'r', encoding='utf-8') as file:
            for word in file:
                word = word.strip().lower()
                if word not in stop_words:
                    self.positive_words.add(word)
            # positive_words = set(word.strip() for word in file)

        self.negative_words = set()
        with open('MasterDictionary/negative-words.txt', 'r', encoding='ISO-8859-1') as file:
            for word in file:
                word = word.strip().lower()
                if word not in stop_words:
                    self.negative_words.add(word)
            # negative_words = set(word.strip() for word in file)

    def get_positive_negative_score(self, text):
        tokens = nltk.word_tokenize(text)
        positive_score = sum(1 for word in tokens if word.lower() in self.positive_words)
        negative_score = sum(1 for word in tokens if word.lower() in self.negative_words)
        return positive_score, negative_score


class Polarity:

    def get_polarity(self, text, stop_words):
        positive_score, negative_score = AnalysePositiveNegativeScore(stop_words).get_positive_negative_score(text)
        return (positive_score - negative_score) / (positive_score + negative_score + 0.000001)


class Subjectivity:

    def get_subjectivity(self, text, stop_words):
        total_words_after_cleaning = len(text.split(' '))
        positive_score, negative_score = AnalysePositiveNegativeScore(stop_words).get_positive_negative_score(text)
        return (positive_score + negative_score) / (total_words_after_cleaning + 0.000001)
