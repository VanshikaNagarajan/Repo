import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

file = 'your file'
input_file = pd.read_excel(file)

if not os.path.exists("text_files"):
    os.makedirs("text_files")


# function to extract text and title from the url with the url id
def extract_content(url, url_id):
    # to check if the url is accessible
    print("requesting site: " + url)
    response = requests.get(url)
    if response.status_code != 200:
        title = "Error"
        text = f"Error: Unable to access {url}\n"
        print(f"Error: Unable to access URL_ID {url_id} - {url}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Title not found"
        text = ''
        paragraphs = soup.find_all('p')
        print('to getting paras')
        for paragraph in paragraphs:
            text += paragraph.get_text() + '\n'

    print('to create a separate text file for every url id')
    with open(f"text_files/{url_id}.txt", 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n")
        file.write(f"Text:\n{text}\n")


for index, row in input_file.iterrows():
    print('to get content for file: ' + str(index))
    url = row['URL']
    url_id = row['URL_ID']
    extract_content(url, url_id)
