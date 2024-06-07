import requests
import bs4
import openai
from summarizer import Summarizer

# OpenAI API key
openai.api_key = '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'

# Episode's url
url = "https://lexfridman.com/podcast/"

def get_most_recent_transcript_link(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    most_recent_podcast = soup.find(class_='guest')
    transcript_link = most_recent_podcast.find('a', string='Transcript')
    return transcript_link.get('href')

def get_most_recent_transcript_text(href_value):
    sec_response = requests.get(href_value)
    sec_soup = bs4.BeautifulSoup(sec_response.text, 'html.parser')
    text_content = sec_soup.body.get_text(separator='\n')
    return text_content

def summarize_text(transcript_text):
    prompt = f"Summarize the following transcript from the Lex Fridman Podcast:\n{transcript_text}"
    response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",  # Choose an appropriate model
          messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": prompt}
    ]
    )
    summary = response['choices'][0]['message']['content']
    return summary

def main():
    url = "https://lexfridman.com/podcast/"
    href_value = get_most_recent_transcript_link(url)
    transcript_text = get_transcript_text(href_value)
    summary = summarize_text(transcript_text)
    print("Generated Summary:", summary)


main()




