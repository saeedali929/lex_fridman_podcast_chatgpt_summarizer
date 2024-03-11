import requests
url = "https://lexfridman.com/podcast/"
response = requests.get("https://lexfridman.com/podcast/")
import bs4
soup = bs4.BeautifulSoup(response.text, 'html.parser')
most_recent_podcast = soup.find(class_ ='guest')
transcript_link = most_recent_podcast.find('a', string= 'Transcript')
href_value = transcript_link.get('href')
sec_response = requests.get(href_value)
sec_soup = bs4.BeautifulSoup(sec_response.text, 'html.parser')
text_content = sec_soup.body.get_text(separator='\n') 

from summarizer import Summarizer

import openai

# Set your OpenAI API key
openai.api_key = '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'

# Assuming 'text_content' contains the transcript text
transcript_text = sec_soup.body.get_text(separator='\n')

# Prompt ChatGPT with the transcript for a summary using openai.ChatCompletion.create
prompt = f"Summarize the following transcript:\n{transcript_text}"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Choose an appropriate model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
)

# Extract the generated summary from the response
summary = response['choices'][0]['message']['content']
print("Generated Summary:", summary)


