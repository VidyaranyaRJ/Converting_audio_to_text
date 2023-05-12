import requests
import json

# Set your API key and the text to be translated
api_key = "your_deepl_api_key"
#text = 'Hello, how are you?'
with open('audio_to_text.txt', 'r') as f:
    text = f.read()
url = 'https://api-free.deepl.com/v2/translate'
params = {
    'auth_key': api_key,
    'text': text,
    'target_lang': 'ES'
}

# Send the translation request and get the response
response = requests.post(url, data=params)
response_json = json.loads(response.text)

# Extract the translated text from the response
translation = response_json['translations'][0]['text']

# Save the translated text to a new text file
with open('english_to_spanish_text.txt', 'w') as f:
    f.write(translation)