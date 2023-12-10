class StopWords:

    def __init__(self):
        self.stop_words = set()

        # to keep all the stop words text file in stop_word_files
        stop_word_files = ['StopWords_Auditor.txt', 'StopWords_Currencies.txt', 'StopWords_DatesandNumbers.txt',
                           'StopWords_Generic.txt', 'StopWords_GenericLong.txt', 'StopWords_Geographic.txt',
                           'StopWords_Names.txt']

        # to read the file
        for stop_word_file in stop_word_files:
            with open('StopWords/' + stop_word_file, "r", encoding="ISO-8859-1") as stop_words_file:
                self.stop_words.update(stop_words_file.read().split())

    def remove_stop_words_from_text(self, text):
        words = text.split()
        cleaned_words = [word for word in words if word.lower() not in self.stop_words]
        cleaned_text = ' '.join(cleaned_words)
        return cleaned_text
