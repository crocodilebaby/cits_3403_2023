import requests
import json
import os


def query_gpt(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    payload = json.dumps(data)
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=15)
        data = response.json()
        print(data)
        answer = data['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    prompt = "How do I get the ASCII value of a character as an int in Python?"
    answer = query_gpt(prompt)
    print(answer)

