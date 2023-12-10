Output is in Output_data.xlsx

# Files
- Data Extraction.py crawls the web using bs4 & creates corresponding text files inside text_files folder
- Data Analysis.py reads each file from text_files_folder & creates a cleaned_files with text without stop words.
   - It then calculates each clean text attributes & stores into a pandas dataframe.
   - Dataframe is then written to Output_data.xlsx

# Steps to run
- Make folders 'text_files', 'cleaned_files' if not exists in root directory
- Get dependencies using requirements.txt
- Accept nltk ssl certificates as shown here (https://stackoverflow.com/a/59530679)
- Run python3 Data\ Extraction.py to create clean text to work with
- Run python3 Data\ Analysis.py to create Output_data.xlsx