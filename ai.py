import argparse
import requests
import json

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
api_key = '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'

# API request payload
payload = {
    "messages": [
        {
            "role": "user",
            "content": args.q
        }
    ],
    "model": "llama3-8b-8192",
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
        print('\nANSWERS:\n\n' + response_result['choices'][0]['message']['content'])
    else:
        print(f'Error: {response.status_code} - {response.text}')
except Exception as e:
    print(f'Error during API call: {e}')