import re

import nltk


class Readability:

    def get_percentage_of_complex_words(self, text, number_of_complex_words):
        total_words_after_cleaning = len(text.split(' '))
        percentage_complex_words = (number_of_complex_words / total_words_after_cleaning) * 100
        return percentage_complex_words

    def get_fog_index(self, text, number_of_complex_words):
        total_words_after_cleaning = len(text.split(' '))
        num_sentences = text.count('.')
        average_sentence_length = total_words_after_cleaning / num_sentences
        percentage_complex_words = self.get_percentage_of_complex_words(text, number_of_complex_words)
        return 0.4 * (average_sentence_length + percentage_complex_words)


class TextCount:

    def _count_syllables(self, word):
        exempted_letters = "aeiouy"
        word = word.lower()
        syllable_count = 0

        if len(word) <= 3:
            return 1

        new_word = word
        for i in range(len(word) - 1):
            if word[i] in exempted_letters and word[i + 1] in exempted_letters:
                new_word = new_word[:i] + new_word[i + 1:]

        if word[0] in exempted_letters:
            syllable_count += 1

        for i in range(1, len(word)):
            if word[i] in exempted_letters and word[i - 1] not in exempted_letters:
                syllable_count += 1

        if word.endswith("e") and not word.endswith("le"):
            syllable_count -= 1

        syllable_count = max(1, syllable_count)
        return syllable_count

    def avg_syllable_count(self, text):
        syllable_count = 0
        words = text.split(' ')
        for word in words:
            syllable_count += self._count_syllables(word)
        return syllable_count / len(words)

    def number_of_complex_words(self, text):
        cleaned_words = text.split()
        complex_word_count = sum(1 for word in cleaned_words if self._count_syllables(word) > 2)
        return complex_word_count

    def count_personal_pronouns(self, text):
        words = nltk.word_tokenize(text)
        text = " ".join(words)
        pronoun_regex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b', re.I)
        pronouns = pronoun_regex.findall(text)
        print(pronouns)
        pronoun_count = len(pronouns)
        return pronoun_count

    def get_avg_word_length(self, text):
        tokens = nltk.word_tokenize(text)
        total_words_after_cleaning = len(text.split(' '))
        avg_word_length = sum(len(word) for word in tokens) / total_words_after_cleaning
        return avg_word_length

    def avg_sentence_length(self, text):
        sentences = text.split('.')
        total_word_count = 0
        for sentence in sentences:
            word_count = len(sentence.split(' '))
            total_word_count += word_count
        num_sentences = len(sentences)
        return word_count / num_sentences

    def avg_words_per_sentence(self, text):
        num_sentences = text.count('.')
        total_words_after_cleaning = len(text.split(' '))
        avg_of_words_per_sentence = total_words_after_cleaning / num_sentences
        return avg_of_words_per_sentence