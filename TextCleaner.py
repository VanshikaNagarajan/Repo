import string


class TextCleaner:

    def remove_punctuation(self, text):
        # to remove punctutation
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text
