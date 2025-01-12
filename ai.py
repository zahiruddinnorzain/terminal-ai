import argparse
import requests
import json
from rich.console import Console
from rich.markdown import Markdown
import rich
import envdata

#==================================
# python3 ai.py --q 'tell me a joke'
#==================================

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Ask AI in your terminal.')
parser.add_argument('--q', type=str, required=True, help='Your question to AI')

# Parse the arguments
args = parser.parse_args()

url = 'https://api.groq.com/openai/v1/chat/completions'

# API Key (Replace with your Groq AI API key if needed)
api_key = envdata.token

# API request payload
payload = {
    "messages": [
        {
            "role": "user",
            "content": args.q
        }
    ],
    "model": envdata.model,
    "temperature": 1,
    "max_tokens": 1024,
    "top_p": 1,
    "stream": False,
    "stop": "null"
}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
# Make the request to the AI API
try:
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        response_result = response.json()
        jawapan = response_result['choices'][0]['message']['content']

        # print('\nANSWERS:\n\n' + jawapan)

        # console = Console()
        # console.print(jawapan)

        markdown = Markdown(jawapan)
        rich.print(markdown)

    else:
        print(f'Error: {response.status_code} - {response.text}')
except Exception as e:
    print(f'Error during API call: {e}')