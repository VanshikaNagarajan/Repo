import codecs
import glob
import os

import nltk
import pandas as pd

from AnalysePositiveNegativeScore import AnalysePositiveNegativeScore, Polarity, Subjectivity
from Readability import TextCount, Readability
from StopWords import StopWords

nltk.downloader.download('vader_lexicon')
nltk.downloader.download('punkt')
nltk.downloader.download('averaged_perceptron_tagger')
nltk.downloader.download('stopwords')


source_folder = 'text_files/'

class FileRunner:

    def __init__(self):
        self._analysis_results = []

    """
    for each text file:-
        - remove punctuations, stop words
        - calculate +ve -ve word score, polarity, subjectivity for text file
        - calculate readability
        - calculate no. of words per sentence
        - calculate complex word count
        - calculate syllable count per word, personal pronouns, avg word length
    """

    def _create_cleaned_text_file_and_return(self, filename):
        print('create processed text file without stop words')
        with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read()

            cleaned_text = StopWords().remove_stop_words_from_text(text)
            # cleaned_text = TextCleaner().remove_punctuation(stop_words_removed_text)

            print('create a cleaned text file from the original text file')
            cleaned_file = filename.replace('.txt', '_cleaned_text_file.txt')
            cleaned_file = cleaned_file.replace(source_folder, '')
            with open('cleaned_files/' + cleaned_file, 'w') as file:
                file.write(cleaned_text)

            return cleaned_text

    def _get_attributes_for_text_file(self, text_filename):
        with codecs.open(text_filename, 'r', encoding='utf-8', errors='ignore') as file:
            text = self._create_cleaned_text_file_and_return(text_filename)
            stop_words = StopWords().stop_words

            positive_score, negative_score = AnalysePositiveNegativeScore(stop_words).get_positive_negative_score(text)
            complex_word_count = TextCount().number_of_complex_words(text)

            return {
                "POSITIVE SCORE": positive_score,
                "NEGATIVE SCORE": negative_score,
                "POLARITY SCORE": Polarity().get_polarity(text, stop_words),
                "SUBJECTIVITY SCORE": Subjectivity().get_subjectivity(text, stop_words),
                "AVG SENTENCE LENGTH": TextCount().avg_sentence_length(text),
                "PERCENTAGE OF COMPLEX WORDS": Readability().get_percentage_of_complex_words(text, complex_word_count),
                "FOG INDEX": Readability().get_fog_index(text, complex_word_count),
                "AVG NUMBER OF WORDS PER SENTENCE": TextCount().avg_words_per_sentence(text),
                "COMPLEX WORD COUNT": complex_word_count,
                "WORD COUNT": len(text.split(' ')),
                "SYLLABLE COUNT PER WORD": TextCount().avg_syllable_count(text),  # assuming avg is asked
                "PERSONAL PRONOUNS": TextCount().count_personal_pronouns(text),
                "AVG WORD LENGTH": TextCount().get_avg_word_length(text)
            }

    def create_output_file(self):
        text_files_folder = source_folder
        text_files = glob.glob(os.path.join(text_files_folder, '*.txt'))
        for text_file in text_files:
            print('reading text file:' + text_file)
            analysis_result = self._get_attributes_for_text_file(text_file)
            self._analysis_results.append(analysis_result)

        # to create a new dataframe
        analysis_df = pd.DataFrame(self._analysis_results)
        # convert to excel
        analysis_df.to_excel("Text_Analysis_Results.xlsx", index=False)
        # to read the input file
        input_file = pd.read_excel("Input.xlsx")
        # to merge two files
        combined_df = pd.concat([input_file, analysis_df], axis=1)
        # covert to excel(final)
        combined_df.to_excel("Output_data.xlsx", index=False)


FileRunner().create_output_file()
